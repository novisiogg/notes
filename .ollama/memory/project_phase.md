---
name: Current project phase
description: Phase 3.2b in progress — ready to write phase3_2.py
type: project
---

**Current phase**: Phase 3.2b — Persistent Chat Memory

**Status**: Planning/prep complete, implementation pending.

**Completed this session**:
- HTTP/deep-dive concepts reviewed and saved to notes.md
- `mock_server.py` written and ready for testing
- Payload structure clarified (`{"model": ..., "messages": history}`)
- Requirements for persistence fully understood

**What exists**:
- `mock_server.py` — ready to run
- `phase3_2.py` — needs to be written from scratch

**What needs to be built** in `phases/phase3_2.py`:
- `ChatAgent` class inheriting from `ConfigManager`
- `self.history` list tracking conversation turns
- `get_reply()` with HTTP POST (model + messages in payload, mock fallback)
- `run()` loop with commands: chat, clear, status, quit, save history, load history
- Auto-load from `chat_history.json` on startup (if file exists)
- Auto-save to `chat_history.json` on graceful quit
- `save_history()` and `load_history()` manual commands
- Enhanced `show_status()` showing file path, message count, size

**Key files**:
- Template/reference: `phase3_1.py` for base ChatAgent structure
- Config parent: `phase2_3.py` (ConfigManager)
- Test server: `mock_server.py` (run in separate terminal)
- History file: `chat_history.json` (created on first save)
