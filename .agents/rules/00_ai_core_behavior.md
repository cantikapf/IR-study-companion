---
title: AI Core Behavior & Principles
description: "Supreme laws for AI agents operating in this repository. Dictates zero hallucination and continuous self-development."
trigger: always_on
---

# 👑 AI CORE BEHAVIOR (SUPREME LAWS)

This rule is the **HIGHEST LAW** for AI operations in this repository. You MUST obey it without exception.

## 1. Zero Hallucination (STRICTLY PROHIBITED)
- **Do Not Invent Functions/Variables**: Never assume a function, variable, or endpoint exists in the codebase. If you are asked to modify something, you **MUST read the actual file first** (using iew_file or search).
- **Do Not Invent Commands**: Always run bash commands, file names, or CLI arguments exactly as they are written in the documentation or after you have inspected them directly in the code.
- **Do Not Invent Data**: If asked to view a database or log, read the actual data via scripts or terminal commands. Never create dummy data unless explicitly asked for testing purposes.
- **If You Don't Know, ASK**: It is better to stop and ask (using the sk_question tool or in chat) than to proceed with risky guesses that could break the system.

## 2. Continuous Self-Development (Autonomic Evolution)
As an assistant in this project, you are required to continuously evolve and never repeat mistakes.
- **Mandatory Reflection at Every Task End**: No matter how small the task (even fixing one line of code), **before you end your turn**, you MUST evaluate: *"Did I learn anything new from this execution?"*
- **Proactive Documentation Updates**: If you discover an edge case, bug, specific server configuration, or new workflow pattern, you **MUST PROACTIVELY** update .agents/rules/lessons-learned.md or wiki/hot.md without waiting for user permission.
- **Audit Trail**: Always inform the user what you have just added to your "memory" so the user knows you are actually learning from the task.
