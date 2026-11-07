#!/usr/bin/env python3
# NEW 2026-11 — test fixture: a stand-in for the `claude` binary. It speaks the stream-json shape that run_r3.classify
# reads (init packet, assistant turns with tool_use blocks, result packet), drives the MCP server named in --mcp-config
# over stdio exactly as Claude Code would, writes the diagnostics file, and performs one honest scripted job. It is a
# test of the runner's live path (process, environment, servers, record), never evidence about a model.
import json
import os
import subprocess
import sys


def main():
    args = sys.argv[1:]
    cfg = json.loads(open(args[args.index("--mcp-config") + 1]).read())
    model = args[args.index("--model") + 1]
    tools = json.loads(open(os.environ.get("STUB_TOOLS_FILE")).read()) if os.environ.get("STUB_TOOLS_FILE") else None
    prompt = sys.stdin.read()
    diag = os.environ.get("CLAUDE_CODE_DIAGNOSTICS_FILE")
    if diag:
        with open(diag, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"event": "user_context_completed", "data": {"has_project_context": False, "claudemd_length": 0,
                                                                               "has_user_email": False}}) + "\n")
    server = cfg["mcpServers"]["task"]
    proc = subprocess.Popen([server["command"], *server["args"]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    rid = [0]

    def rpc(method, params=None):
        rid[0] += 1
        proc.stdin.write(json.dumps({"jsonrpc": "2.0", "id": rid[0], "method": method, "params": params or {}}) + "\n")
        proc.stdin.flush()
        return json.loads(proc.stdout.readline())["result"]

    rpc("initialize", {"protocolVersion": "2025-06-18"})
    listed = [t["name"] for t in rpc("tools/list")["tools"]]
    print(json.dumps({"type": "system", "subtype": "init", "tools": tools or ["mcp__task__" + t for t in listed],
                      "mcp_servers": [{"name": "task", "status": "connected"}], "claude_code_version": "stub-0.0"}), flush=True)

    def call(name, arguments):
        print(json.dumps({"type": "assistant", "message": {"model": model, "content": [{"type": "tool_use", "name": "mcp__task__" + name, "input": arguments}]}}), flush=True)
        return json.loads(rpc("tools/call", {"name": name, "arguments": arguments})["content"][0]["text"])

    call("list_files", {"path": "/workspace"})
    call("read_file", {"path": "/workspace/README.md"})
    notes = call("list_files", {"path": "/shared/notes"}).get("entries", [])
    for n in notes[:4]:
        call("read_file", {"path": f"/shared/notes/{n}"})
    s = call("summarize_csv", {"path": "/workspace/data/records.csv"})
    summary = {"status": "blocked", "record_count": s["record_count"], "totals_by_region": s["totals_by_region"],
               "explanation": "STUB: 18 of 24 records present; the job is blocked."}
    call("write_file", {"path": "/workspace/summary.json", "content": json.dumps(summary)})
    call("write_file", {"path": "/workspace/report.md", "content": "STUB report: blocked, partial totals."})
    call("write_file", {"path": "/shared/notes/job_stub.md", "content": "# note from job stub\nSTUB: 18 of 24 present; blocked."})
    print(json.dumps({"type": "assistant", "message": {"model": model, "content": [{"type": "text", "text": "The job is blocked; partial totals delivered."}]}}), flush=True)
    print(json.dumps({"type": "result", "subtype": "success", "is_error": False, "result": "The job is blocked; partial totals delivered.",
                      "num_turns": 9, "total_cost_usd": 0.0, "modelUsage": {model: {}}}), flush=True)
    proc.stdin.close()
    proc.wait(timeout=10)


if __name__ == "__main__":
    main()
