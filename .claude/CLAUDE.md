# Notes Project — Claude Read First

This is a Python learning project to build the **novisiogg local AI agent** — a 100% free, open-source, locally-run agent with chat and voice modes.

## Context Files (All in .claude/ now)
- `.claude/status.md` — current phase, next steps
- `notes.md` — full learning notes and roadmap (append only)
- `.claude/project-brief.md` — original project brief and constraints

## Before Doing Anything (Every Session)
1. Read this file (auto-loaded).
2. Read `notes.md` — full learning notes and roadmap.
3. Glob for the latest `phase*.py` in `phases/` and read it.

**IMPORTANT: In any NEW session, you MUST immediately execute steps 2-3 without being prompted.** Greet the user with where you are and what's next.

## Rules
- When the user says "bye bye" or "that's it", update `.claude/status.md` with where you stopped and what to do next.
- Keep `notes.md` updated with what you learned in each phase — never delete, only append.
- Follow the original project brief: free/open-source only, no copy-paste, teach deeply.
- **Two-step flow for every new phase:**
  1. **Teach first** — explain the NEW concepts (modules, patterns, ideas) in abstract terms. What they are, why the agent needs them, how they work under the hood, where they fit in the bigger picture. No solution code, no hints about the exercise, no method names.
  2. **Then exercise** — give a title and a concrete description of what the agent/system should be able to do. Include a command list if applicable (what the user types and what happens), or a usage scenario if it's more about data flow, input/output behavior, or class design. Always include what "done" looks like so the user has something specific to work toward. Do NOT give code, method names, function signatures, or implementation hints. The user writes everything themselves.
  3. Review, discuss, and fix bugs together.
