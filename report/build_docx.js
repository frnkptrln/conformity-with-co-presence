#!/usr/bin/env node
// NEW 2026-11 — builds report.docx from report.md (a small Markdown subset) with docx-js, in the layout of the Apart
// Research submission template: title, author block, "With Apart Research", abstract, numbered sections.
// Usage: node build_docx.js report.md report.docx
const fs = require("fs");
const path = require("path");
const sizeOf = (p) => { const b = fs.readFileSync(p); return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) }; }; // PNG IHDR
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, Table, TableRow, TableCell, WidthType,
  ImageRun, BorderStyle, ShadingType, LevelFormat, ExternalHyperlink, TabStopType,
} = require("docx");

const [,, srcPath, outPath] = process.argv;
const src = fs.readFileSync(srcPath, "utf8").split("\n");
const baseDir = path.dirname(path.resolve(srcPath));

const FONT = "Arial";
const BODY = 20;          // half-points: 10 pt
const SMALL = 17;         // 8.5 pt (tables, captions)
const MONO = "Liberation Mono";
const PAGE_W = 11906, PAGE_H = 16838;           // A4 in DXA
const MARGIN = 1247;                            // 2.2 cm
const TEXT_W = PAGE_W - 2 * MARGIN;             // 9412 DXA
const INK = "0B0B0B", INK2 = "52514E", RULE = "C3C2B7";

// ---------------------------------------------------------------- inline markdown -> runs
function inline(text, base = {}) {
  const runs = [];
  // tokens: **bold**, *italic*, `code`, URLs
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`|https?:\/\/[^\s)\]]*[^\s)\].,;:])/g;   // a URL never ends in punctuation
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) runs.push(new TextRun({ text: text.slice(last, m.index), font: FONT, size: base.size || BODY, ...base }));
    const tok = m[0];
    if (tok.startsWith("**")) runs.push(new TextRun({ text: tok.slice(2, -2), bold: true, font: FONT, size: base.size || BODY, ...base }));
    else if (tok.startsWith("`")) runs.push(new TextRun({ text: tok.slice(1, -1), font: MONO, size: (base.size || BODY) - 1, ...base }));
    else if (tok.startsWith("*")) runs.push(new TextRun({ text: tok.slice(1, -1), italics: true, font: FONT, size: base.size || BODY, ...base }));
    else runs.push(new ExternalHyperlink({ link: tok, children: [new TextRun({ text: tok, font: FONT, size: base.size || BODY, color: "1C5CAB", underline: {}, ...base })] }));
    last = m.index + tok.length;
  }
  if (last < text.length) runs.push(new TextRun({ text: text.slice(last), font: FONT, size: base.size || BODY, ...base }));
  return runs;
}

function para(text, opts = {}) {
  return new Paragraph({ children: inline(text, opts.run || {}), alignment: opts.align || AlignmentType.JUSTIFIED,
    spacing: { after: opts.after ?? 90, line: 252, before: opts.before ?? 0 }, ...(opts.extra || {}) });
}

// ---------------------------------------------------------------- front matter
const meta = {};
let i = 0;
while (i < src.length && src[i].startsWith("% ")) {
  const mm = src[i].match(/^% (\w+): (.*)$/);
  if (mm) meta[mm[1]] = mm[2];
  i++;
}

const children = [];
children.push(new Paragraph({ children: [new TextRun({ text: meta.title, bold: true, font: FONT, size: 30, color: INK })],
  alignment: AlignmentType.CENTER, spacing: { after: 160, line: 276 } }));
children.push(new Paragraph({ children: [new TextRun({ text: meta.author, bold: true, font: FONT, size: 22 })], alignment: AlignmentType.CENTER, spacing: { after: 40 } }));
children.push(new Paragraph({ children: [new TextRun({ text: meta.affiliation, font: FONT, size: 19, color: INK2 })], alignment: AlignmentType.CENTER, spacing: { after: 40 } }));
children.push(new Paragraph({ children: [new TextRun({ text: meta.with, font: FONT, size: 19, italics: true, color: INK2 })], alignment: AlignmentType.CENTER, spacing: { after: 200 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 8 } } }));

// ---------------------------------------------------------------- body
const numbered = []; // numbering instances
let listId = 0;
function heading(text, level) {
  const size = level === 1 ? 24 : level === 2 ? 21 : 20;
  const isAbstract = /^Abstract$/.test(text);
  return new Paragraph({ children: [new TextRun({ text, bold: true, font: FONT, size, color: INK })],
    heading: level === 1 ? HeadingLevel.HEADING_1 : level === 2 ? HeadingLevel.HEADING_2 : HeadingLevel.HEADING_3,
    spacing: { before: level === 1 ? 240 : 160, after: isAbstract ? 60 : 80 }, keepNext: true });
}

function table(lines) {
  const rows = lines.filter((l) => !/^\|\s*:?-+/.test(l)).map((l) => l.replace(/^\||\|$/g, "").split("|").map((c) => c.trim()));
  const ncol = Math.max(...rows.map((r) => r.length));
  // column widths: proportional to the longest cell per column, bounded
  const longestWord = (str) => Math.max(0, ...str.split(/\s+/).map((w) => w.length));
  const CH = 100;                                   // DXA per character at 8.5 pt, generous
  const cols = Array.from({ length: ncol }, (_, c) => rows.map((r) => (r[c] || "").replace(/[*`]/g, "")));
  const minw = cols.map((cells) => (Math.max(...cells.map(longestWord), 3) + 1) * CH + 160);
  const need = cols.map((cells, c) => Math.max(0, Math.min(Math.max(...cells.map((x) => x.length)), 60) * CH - minw[c]));
  let widths;
  const sumMin = minw.reduce((a, b) => a + b, 0);
  if (sumMin >= TEXT_W) {
    widths = minw.map((w) => Math.round((TEXT_W * w) / sumMin));
  } else {
    const extra = TEXT_W - sumMin;
    const sumNeed = need.reduce((a, b) => a + b, 0) || 1;
    widths = minw.map((w, c) => Math.round(w + (extra * need[c]) / sumNeed));
  }
  widths[ncol - 1] += TEXT_W - widths.reduce((a, b) => a + b, 0);
  const trs = rows.map((cells, r) => new TableRow({ cantSplit: true,
    tableHeader: r === 0,
    children: Array.from({ length: ncol }, (_, c) => new TableCell({
      width: { size: widths[c], type: WidthType.DXA },
      shading: r === 0 ? { type: ShadingType.CLEAR, fill: "F0EFEC", color: "auto" } : undefined,
      margins: { top: 40, bottom: 40, left: 70, right: 70 },
      borders: { top: { style: BorderStyle.SINGLE, size: 4, color: RULE }, bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE },
        left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" } },
      children: [new Paragraph({ children: inline(cells[c] || "", { size: SMALL, bold: r === 0 ? true : undefined }),
        alignment: AlignmentType.LEFT, spacing: { after: 0, line: 240 } })],
    })),
  }));
  return new Table({ rows: trs, width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: widths });
}

function image(caption, rel) {
  const p = path.resolve(baseDir, rel);
  const { w, h } = sizeOf(p);
  const widthPt = TEXT_W / 20;                        // DXA -> points
  const heightPt = (widthPt * h) / w;
  return [
    new Paragraph({ children: [new ImageRun({ type: "png", data: fs.readFileSync(p), transformation: { width: widthPt * 1.3333, height: heightPt * 1.3333 } })],
      alignment: AlignmentType.CENTER, spacing: { before: 120, after: 60 }, keepNext: true }),
    new Paragraph({ children: inline(caption, { size: SMALL, color: INK2 }), alignment: AlignmentType.JUSTIFIED, spacing: { after: 200, line: 240 }, keepLines: true }),
  ];
}

let k = i;
let inCode = false, codeLines = [];
while (k < src.length) {
  const line = src[k];
  if (line.startsWith("```")) {
    if (inCode) {
      for (const cl of codeLines) children.push(new Paragraph({ children: [new TextRun({ text: cl || " ", font: MONO, size: 15 })], spacing: { after: 0, line: 220 },
        shading: { type: ShadingType.CLEAR, fill: "F6F5F1", color: "auto" }, indent: { left: 120 } }));
      children.push(new Paragraph({ children: [], spacing: { after: 120 } }));
      codeLines = []; inCode = false;
    } else inCode = true;
    k++; continue;
  }
  if (inCode) { codeLines.push(line); k++; continue; }
  if (!line.trim()) { k++; continue; }
  if (line.startsWith("### ")) { children.push(heading(line.slice(4), 3)); k++; continue; }
  if (line.startsWith("## ")) { children.push(heading(line.slice(3), 2)); k++; continue; }
  if (line.startsWith("# ")) { children.push(heading(line.slice(2), 1)); k++; continue; }
  if (line.startsWith("|")) {
    const tl = [];
    while (k < src.length && src[k].startsWith("|")) tl.push(src[k++]);
    children.push(table(tl));
    children.push(new Paragraph({ children: [], spacing: { after: 120 } }));
    continue;
  }
  const img = line.match(/^!\[(.*)\]\((.*)\)$/);
  if (img) { children.push(...image(img[1], img[2])); k++; continue; }
  if (/^- /.test(line)) {
    while (k < src.length && /^- /.test(src[k])) {
      children.push(new Paragraph({ children: inline(src[k].slice(2)), numbering: { reference: "bullets", level: 0 }, alignment: AlignmentType.JUSTIFIED, spacing: { after: 50, line: 252 } }));
      k++;
    }
    continue;
  }
  if (/^\d+\. /.test(line)) {
    listId++;
    const ref = `num${listId}`;
    numbered.push(ref);
    while (k < src.length && /^\d+\. /.test(src[k])) {
      children.push(new Paragraph({ children: inline(src[k].replace(/^\d+\. /, "")), numbering: { reference: ref, level: 0 }, alignment: AlignmentType.JUSTIFIED, spacing: { after: 50, line: 252 } }));
      k++;
    }
    continue;
  }
  // paragraph (may span following non-empty lines)
  let text = line;
  k++;
  while (k < src.length && src[k].trim() && !/^(#|\||!\[|- |\d+\. |```)/.test(src[k])) { text += " " + src[k]; k++; }
  children.push(para(text));
}

const doc = new Document({
  creator: meta.author,
  title: meta.title,
  styles: {
    default: { document: { run: { font: FONT, size: BODY, color: INK } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 24, bold: true, color: INK }, paragraph: { spacing: { before: 240, after: 80 }, keepNext: true, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 21, bold: true, color: INK }, paragraph: { spacing: { before: 160, after: 80 }, keepNext: true, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 20, bold: true, color: INK }, paragraph: { spacing: { before: 120, after: 60 }, keepNext: true, outlineLevel: 2 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 420, hanging: 260 } } } }] },
      ...numbered.map((ref) => ({ reference: ref, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 420, hanging: 300 } } } }] })),
    ],
  },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: PAGE_H }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } } },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(outPath, buf); console.log("wrote", outPath, buf.length, "bytes"); });
