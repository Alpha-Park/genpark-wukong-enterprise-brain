---
description: Enterprise Tool Orchestrator. Deeply integrates with calendars, chat systems, and document repositories for seamless office productivity.
license: MIT
metadata:
  last_deployed: "2026-04-25"
  version: "1.0.0"
  source: "https://wukong.dingtalk.com/"
---

# Wukong Enterprise Brain

This skill provides agents with "native-level" access to enterprise ecosystems. It bridges the gap between communication (chat), planning (calendar), and knowledge (docs) to provide a unified productivity layer.

## MCP runtime requirements

The standard-library-only policy applies to direct `client.py` use. Running `mcp_server.py` requires Python 3.10+ and the official `mcp` SDK (`mcp>=1.0.0,<2`) from `requirements.txt`. Install it into your chosen environment from the repository checkout:

```bash
python -m pip install -r requirements.txt
```

Configure the MCP client with that environment's absolute Python executable path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; a GitHub URL is not a remote MCP endpoint.

## Instructions
1. **Contextual Awareness:** Access and analyze project-related data across chat logs, emails, and shared documents.
2. **Scheduling Orchestration:** Perform cross-calendar availability checks and automate meeting scheduling with intelligent conflict resolution.
3. **Cross-App Data Flow:** Move data between enterprise apps (e.g., summarizing a chat discussion into a formal document or task list).
4. **Voice/Text Multi-Modal:** Support seamless transitions between voice commands and text-based task execution.

## Examples
- "Check the team's calendars and schedule a 30-minute sync on 'Project X' for next Tuesday afternoon."
- "Pull the action items from our last three chat discussions about the product launch and add them to the shared project document."
