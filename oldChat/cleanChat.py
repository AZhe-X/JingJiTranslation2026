#!/usr/bin/env python3
"""
cleanChat.py — Convert Claude Code JSONL transcript to readable markdown.

Usage:
    python3 cleanChat.py <input.jsonl> [output.md]
    python3 cleanChat.py <input.jsonl> -o output.md --no-thinking --no-tool-results

Produces a clean conversation log in the format:

    ## User at 2026-02-10 16:54:32
    hello! let read the 境集...

    ---

    ## Claude at 2026-02-10 16:54:35
    [thinking:] The user wants me to read...

    Let me explore the directory to find these files.

    [tool: Bash] ls /Users/el/...

    ---
"""

import json
import sys
import re
import argparse
from datetime import datetime


def format_ts(iso_str):
    """Convert ISO timestamp to readable format."""
    if not iso_str:
        return "unknown time"
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return iso_str


def extract_tagged_blocks(text):
    """Extract teammate messages, system reminders, and commands from text.
    Returns (teammate_msgs, system_reminders, commands, remaining_text).
    """
    teammate_msgs = []
    # Match teammate messages with attributes
    for m in re.finditer(
        r'<teammate-message\s+([^>]*)>(.*?)</teammate-message>',
        text, re.DOTALL
    ):
        attrs_str, body = m.group(1), m.group(2)
        tid = ""
        summary = ""
        color = ""
        tid_match = re.search(r'teammate_id="([^"]*)"', attrs_str)
        if tid_match:
            tid = tid_match.group(1)
        sum_match = re.search(r'summary="([^"]*)"', attrs_str)
        if sum_match:
            summary = sum_match.group(1)
        col_match = re.search(r'color="([^"]*)"', attrs_str)
        if col_match:
            color = col_match.group(1)
        teammate_msgs.append({
            "id": tid,
            "summary": summary,
            "color": color,
            "body": body.strip(),
        })

    system_reminders = re.findall(
        r'<system-reminder>(.*?)</system-reminder>', text, re.DOTALL
    )

    commands = []
    cmd_names = re.findall(r'<command-name>(.*?)</command-name>', text)
    cmd_msgs = re.findall(r'<command-message>(.*?)</command-message>', text)
    for i, name in enumerate(cmd_names):
        msg = cmd_msgs[i] if i < len(cmd_msgs) else ""
        commands.append({"name": name, "message": msg})

    # Strip all tags to get remaining text
    remaining = text
    remaining = re.sub(
        r'<teammate-message[^>]*>.*?</teammate-message>', '', remaining, flags=re.DOTALL
    )
    remaining = re.sub(
        r'<system-reminder>.*?</system-reminder>', '', remaining, flags=re.DOTALL
    )
    remaining = re.sub(
        r'<local-command-caveat>.*?</local-command-caveat>', '', remaining, flags=re.DOTALL
    )
    remaining = re.sub(
        r'<command-name>.*?</command-name>', '', remaining
    )
    remaining = re.sub(
        r'<command-message>.*?</command-message>', '', remaining
    )
    remaining = re.sub(
        r'<command-args>.*?</command-args>', '', remaining
    )
    remaining = re.sub(
        r'<local-command-stdout>.*?</local-command-stdout>', '', remaining, flags=re.DOTALL
    )
    remaining = remaining.strip()

    return teammate_msgs, system_reminders, commands, remaining


def compact_tool_input(tool_input, max_len=800):
    """Format tool input compactly."""
    s = json.dumps(tool_input, ensure_ascii=False, indent=2)
    if len(s) > max_len:
        s = s[:max_len] + "\n... [truncated]"
    return s


def process_user_content(content, timestamp, output, opts):
    """Process user message content (string or list) and append to output."""
    if isinstance(content, str):
        text = content.strip()
        if not text:
            return

        teammate_msgs, sys_rems, commands, remaining = extract_tagged_blocks(text)

        # System reminders
        if opts.system_reminders:
            for sr in sys_rems:
                sr = sr.strip()
                if sr:
                    output.append({
                        "header": "System",
                        "timestamp": timestamp,
                        "body": sr,
                    })

        # Commands (slash commands)
        for cmd in commands:
            output.append({
                "header": "User (command)",
                "timestamp": timestamp,
                "body": f"/{cmd['name']} {cmd['message']}".strip(),
            })

        # Teammate messages
        for tm in teammate_msgs:
            header = tm["id"] or "teammate"
            body = tm["body"]
            if tm["summary"]:
                body = f"*{tm['summary']}*\n\n{body}"
            output.append({
                "header": header,
                "timestamp": timestamp,
                "body": body,
            })

        # Remaining user text
        if remaining:
            output.append({
                "header": "User",
                "timestamp": timestamp,
                "body": remaining,
            })

    elif isinstance(content, list):
        for block in content:
            btype = block.get("type")
            if btype == "tool_result":
                if opts.tool_results:
                    tool_content = block.get("content", "")
                    if isinstance(tool_content, str):
                        if len(tool_content) > opts.max_result_len:
                            tool_content = (
                                tool_content[:opts.max_result_len]
                                + "\n... [truncated]"
                            )
                        if tool_content.strip():
                            output.append({
                                "header": "System (Tool Result)",
                                "timestamp": timestamp,
                                "body": tool_content,
                            })
            elif btype == "text":
                text = block.get("text", "").strip()
                if text:
                    process_user_content(text, timestamp, output, opts)


def process_jsonl(input_path, output_path, opts):
    """Main processing: read JSONL, group messages, write markdown."""
    entries = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    output = []
    assistant_groups = {}  # msg_id -> group dict

    for entry in entries:
        etype = entry.get("type")

        # Skip non-message types
        if etype in ("file-history-snapshot", "progress"):
            continue

        timestamp = entry.get("timestamp", "")
        message = entry.get("message", {})
        role = message.get("role", "")
        content = message.get("content", "")

        # --- User messages ---
        if etype == "user" and role == "user":
            process_user_content(content, timestamp, output, opts)

        # --- Assistant messages ---
        elif etype == "assistant" and role == "assistant":
            msg_id = message.get("id", "")
            if not msg_id:
                continue

            # Group by message ID (streaming chunks share the same ID)
            if msg_id not in assistant_groups:
                assistant_groups[msg_id] = {
                    "thinking": [],
                    "texts": [],
                    "tools": [],
                    "timestamp": timestamp,
                    "output_idx": len(output),
                }
                # Insert placeholder
                output.append({
                    "header": "Claude",
                    "timestamp": timestamp,
                    "body": "",
                    "thinking": "",
                    "_msg_id": msg_id,
                })

            group = assistant_groups[msg_id]

            if isinstance(content, list):
                for block in content:
                    btype = block.get("type")
                    if btype == "thinking":
                        t = block.get("thinking", "")
                        if t:
                            group["thinking"].append(t)
                    elif btype == "text":
                        t = block.get("text", "").strip()
                        if t:
                            group["texts"].append(t)
                    elif btype == "tool_use":
                        if opts.tool_calls:
                            name = block.get("name", "unknown")
                            inp = block.get("input", {})
                            desc = inp.get("description", "")
                            # Build compact representation
                            parts = [f"[tool: {name}]"]
                            if desc:
                                parts[0] += f" — {desc}"
                            # Show key parameters
                            display_input = {
                                k: v for k, v in inp.items()
                                if k != "description"
                            }
                            if display_input:
                                parts.append(compact_tool_input(
                                    display_input, opts.max_tool_len
                                ))
                            group["tools"].append("\n".join(parts))

    # Fill in assistant placeholders
    for msg_id, group in assistant_groups.items():
        idx = group["output_idx"]
        if idx >= len(output):
            continue

        entry = output[idx]

        # Combine thinking
        if group["thinking"] and opts.thinking:
            entry["thinking"] = "\n".join(group["thinking"])

        # Combine body: texts + tools interleaved in order
        body_parts = []
        for t in group["texts"]:
            body_parts.append(t)
        for t in group["tools"]:
            body_parts.append(t)
        entry["body"] = "\n\n".join(body_parts)

    # Remove empty entries
    output = [
        o for o in output
        if o.get("body", "").strip() or o.get("thinking", "").strip()
    ]

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        for block in output:
            ts = format_ts(block["timestamp"])
            header = block["header"]
            f.write(f"## {header} at {ts}\n\n")

            if block.get("thinking"):
                if opts.thinking_collapsed:
                    # Use <details> for collapsible thinking
                    f.write("<details>\n<summary>[thinking]</summary>\n\n")
                    f.write(block["thinking"])
                    f.write("\n\n</details>\n\n")
                else:
                    f.write(f"[thinking:] {block['thinking']}\n\n")

            if block.get("body"):
                f.write(f"{block['body']}\n\n")

            f.write("---\n\n")

    return len(output)


def main():
    parser = argparse.ArgumentParser(
        description="Convert Claude Code JSONL transcript to readable markdown."
    )
    parser.add_argument("input", help="Path to input .jsonl file")
    parser.add_argument("output", nargs="?", default=None,
                        help="Path to output .md file (default: <input>_clean.md)")
    parser.add_argument("--no-thinking", action="store_true",
                        help="Exclude thinking/reasoning blocks")
    parser.add_argument("--collapse-thinking", action="store_true",
                        help="Wrap thinking in collapsible <details> tags")
    parser.add_argument("--no-tool-calls", action="store_true",
                        help="Exclude tool call details from assistant messages")
    parser.add_argument("--tool-results", action="store_true",
                        help="Include tool results (off by default, can be verbose)")
    parser.add_argument("--no-system", action="store_true",
                        help="Exclude system reminders")
    parser.add_argument("--max-result-len", type=int, default=2000,
                        help="Max chars for tool result display (default: 2000)")
    parser.add_argument("--max-tool-len", type=int, default=800,
                        help="Max chars for tool input display (default: 800)")

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    if output_path is None:
        output_path = input_path.rsplit(".", 1)[0] + "_clean.md"

    class Opts:
        thinking = not args.no_thinking
        thinking_collapsed = args.collapse_thinking
        tool_calls = not args.no_tool_calls
        tool_results = args.tool_results
        system_reminders = not args.no_system
        max_result_len = args.max_result_len
        max_tool_len = args.max_tool_len

    count = process_jsonl(input_path, output_path, Opts())
    print(f"Done. {count} blocks written to {output_path}")


if __name__ == "__main__":
    main()
