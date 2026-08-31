---
title: Second Brain Autoload & Synchronization Rule
description: "Ensures agents automatically load local Obsidian Second Brain context on Turn 1, query the vault first, and safely synchronize insights via atomic transactions."
trigger: always_on
---

# Antigravity Obsidian Second Brain Integration SOP

This project is connected to an Antigravity Obsidian Second Brain Vault located at `wiki/`.

## Mandatory Turn 1 SOP (Every New Session / Task)

1. **Hot Cache Autoload (CRITICAL):**
   Before generating any initial response or executing any analytical command, you **MUST** read the active hot cache located at `wiki/hot.md`. This file contains the short-term memory, active research threads, and latest contextual focus of the research project.

2. **Vault-First Inquiry (`wiki-query` / `wiki-retrieve`):**
   If the user asks a question about the project, literature, theoretical concepts, or empirical findings, **ALWAYS** prioritize using the `wiki-query` or `wiki-retrieve` skills to search the vault first. Do NOT rely solely on generic pre-trained weights if the answer or entity exists in the local vault (`wiki/concepts/`, `wiki/entities/`, `wiki/literature/`, `wiki/sources/`).

3. **Domain Knowledge Routing:**
   - For project specific architecture, config, or APIs: Read `wiki/hot.md` and `.agents/rules/lessons-learned.md`.
   - For external web investigations (with user consent): Use `autoresearch`.

4. **Preserving Insights & New Data:**
   - When preserving conversation insights, analytical summaries, or key decisions: Use `save`.
   - When ingesting external documents, structured datasets, or cleaned web pages: Use `wiki-ingest`.
   - For deep reasoning or architectural tradeoffs: Use `think`.

## Session Wrap-Up & Synchronization Protocol

After EVERY turn that produces new information, decisions, configuration changes, trial-and-error results, or user preferences - regardless of scale:

### Mode A: Interactive User Sessions (Main Chat)
Do NOT pause execution to ask for confirmation before saving insights.
Automatically execute the update via the appropriate skill (`save` for conceptual notes, `wiki-ingest` for raw data, or log rollup via `wiki-fold`).
In your final response, simply report what was autonomously updated in the wiki.

### Mode B: Autonomous Subagents & Headless Workflows
In non-interactive subagent delegations (e.g. scrapers, data validators, automated workers):
1. Do NOT pause execution waiting for conversational chat input.
2. Formulate proposed vault updates as structured markdown in your `handoff.md` report under a dedicated `## Second Brain Synchronization Proposals` section.
3. If explicitly authorized in the dispatch task, execute the updates using atomic transaction bundles (`antigravity-obsidian.transaction.v1`) via `antigravity-obsidian.py`.

## Atomic Transaction Integrity Mandate
All modifications to the Second Brain vault MUST pass through the Python transaction engine or use safe atomic operations with valid SHA-256 pre-condition hashing. **NEVER perform unverified direct host writes** that bypass the provenance ledger or risk vault corruption.
