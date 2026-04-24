"""
AI Mentor Agent - A learning companion that tracks your progress through a roadmap.

This agent can:
- Read and understand your roadmap
- Track which phase/topic you're on
- Create session notes automatically
- Generate exercises
- Remember past conversations
- Update progress files
"""

import json
import os
import sys
from datetime import datetime, date
from pathlib import Path
from typing import Dict, List, Optional
import re

try:
    import ollama
except ImportError:
    print("❌ Error: 'ollama' Python package not installed")
    print("   Install with: pip install ollama --break-system-packages")
    sys.exit(1)


class LearningMentor:
    def __init__(self, workspace_dir: str = None):
        """Initialize the mentor with a workspace directory."""
        self.workspace = Path(
            workspace_dir or os.path.expanduser("~/learning-workspace")
        )
        self.workspace.mkdir(parents=True, exist_ok=True)

        # Create directory structure
        self.sessions_dir = self.workspace / "sessions"
        self.exercises_dir = self.workspace / "exercises"
        self.concepts_dir = self.workspace / "concepts"

        for d in [self.sessions_dir, self.exercises_dir, self.concepts_dir]:
            d.mkdir(exist_ok=True)

        # State files
        self.roadmap_file = self.workspace / "ROADMAP.md"
        self.progress_file = self.workspace / "progress.json"
        self.config_file = self.workspace / "config.json"

        # Load or create state
        self.config = self._load_config()
        self.progress = self._load_progress()
        self.roadmap = self._load_roadmap()

        # Conversation history for current session
        self.history = []

        # Model configuration
        self.model = self.config.get("model", "llama3.1:latest")

    def _load_config(self) -> Dict:
        """Load or create configuration."""
        if self.config_file.exists():
            with open(self.config_file) as f:
                return json.load(f)

        config = {
            "model": "llama3.1:latest",
            "created": str(datetime.now()),
            "context_length": 32768,
        }
        self._save_config(config)
        return config

    def _save_config(self, config: Dict):
        """Save configuration."""
        with open(self.config_file, "w") as f:
            json.dump(config, f, indent=2)

    def _load_progress(self) -> Dict:
        """Load or create progress tracking."""
        if self.progress_file.exists():
            with open(self.progress_file) as f:
                return json.load(f)

        progress = {
            "current_phase": "Phase-00",
            "current_topic": "Python Language Deep Dive",
            "started": str(date.today()),
            "last_session": None,
            "sessions_completed": 0,
            "exercises_completed": 0,
            "phases_completed": [],
            "topics_completed": [],
        }
        self._save_progress(progress)
        return progress

    def _save_progress(self, progress: Dict = None):
        """Save progress to file."""
        if progress:
            self.progress = progress
        with open(self.progress_file, "w") as f:
            json.dump(self.progress, f, indent=2)

    def _load_roadmap(self) -> Optional[str]:
        if self.roadmap_file.exists():
            # Added encoding='utf-8' to handle non-ASCII characters
            return self.roadmap_file.read_text(encoding="utf-8")
        return None

    def import_roadmap(self, roadmap_path: str):
        """Import a roadmap file."""
        source = Path(roadmap_path)

        if not source.exists():
            print(f"❌ Roadmap file not found: {roadmap_path}")
            return False
        self.roadmap_file.write_text(
            source.read_text(encoding="utf-8"), encoding="utf-8"
        )
        self.roadmap = self._load_roadmap()
        print(f"✅ Roadmap imported from {roadmap_path}")
        return True

    def get_system_prompt(self) -> str:
        """Generate the system prompt with current context."""
        # Get recent sessions
        recent_sessions = self._get_recent_sessions(n=3)

        # Build context
        context = f"""You are a technical mentor guiding someone through an intensive CS/AI/Security learning roadmap.

CURRENT STATE:
- Phase: {self.progress['current_phase']}
- Topic: {self.progress['current_topic']}
- Sessions completed: {self.progress['sessions_completed']}
- Exercises completed: {self.progress['exercises_completed']}
- Last session: {self.progress['last_session'] or 'Never'}

RECENT SESSIONS:
{recent_sessions}

ROADMAP OVERVIEW:
{self._get_roadmap_summary()}

YOUR CAPABILITIES:
You can help the student by:
- Explaining concepts from first principles
- Generating exercises matched to their level
- Reviewing their code
- Tracking what they've learned
- Suggesting what to study next

TEACHING PHILOSOPHY:
- Always explain "what's happening at the byte level"
- Show code examples
- Ask Socratic questions
- Reference past topics when relevant
- Generate exercises that build on previous knowledge

When the student asks you to create an exercise, generate it in markdown format with:
- Clear instructions
- Learning objectives
- Hints
- Acceptance criteria

When they complete a session, I will save the conversation automatically.
"""
        return context

    def _get_recent_sessions(self, n: int = 3) -> str:
        """Get summaries of recent sessions."""
        session_files = sorted(self.sessions_dir.glob("*.md"), reverse=True)[:n]

        if not session_files:
            return "No previous sessions."

        summaries = []
        for session_file in session_files:
            content = session_file.read_text()
            # Extract summary section if it exists
            if "## Summary" in content:
                summary = content.split("## Summary")[1].split("##")[0].strip()
                summaries.append(f"**{session_file.stem}:**\n{summary[:200]}...")

        return (
            "\n\n".join(summaries) if summaries else "No session summaries available."
        )

    def _get_roadmap_summary(self) -> str:
        """Get a summary of the roadmap (first 2000 chars)."""
        if not self.roadmap:
            return "No roadmap loaded. Import one with: mentor.import_roadmap('path/to/ROADMAP.md')"

        # Return first chunk of roadmap
        return self.roadmap[:2000] + "\n\n[... roadmap continues ...]"

    def chat(self, user_message: str) -> str:
        """Send a message to the AI mentor."""
        # Add user message to history
        self.history.append({"role": "user", "content": user_message})

        # Build messages with system prompt
        messages = [
            {"role": "system", "content": self.get_system_prompt()},
            *self.history,
        ]

        # Call Ollama
        try:
            response = ollama.chat(
                model=self.model,
                messages=messages,
            )

            ai_message = response["message"]["content"]

            # Add to history
            self.history.append({"role": "assistant", "content": ai_message})

            return ai_message

        except Exception as e:
            return f"❌ Error communicating with Ollama: {e}\n\nMake sure Ollama is running: ollama serve"

    def create_session_file(self) -> Path:
        """Create a new session file for today."""
        today = date.today().isoformat()
        session_file = self.sessions_dir / f"{today}.md"

        # If file exists, append a number
        counter = 1
        while session_file.exists():
            session_file = self.sessions_dir / f"{today}-{counter}.md"
            counter += 1

        # Create session template
        template = f"""# Learning Session - {today}

**Phase:** {self.progress['current_phase']}
**Topic:** {self.progress['current_topic']}
**Started:** {datetime.now().strftime('%H:%M')}

---

## Goals
- 

---

## Conversation

"""
        session_file.write_text(template)
        return session_file

    def save_session(self, summary: str = None):
        """Save the current session."""
        if not self.history:
            print("⚠️  No conversation to save")
            return

        session_file = self.create_session_file()

        # Build conversation log
        conversation = []
        for msg in self.history:
            role = "**You:**" if msg["role"] == "user" else "**Mentor:**"
            conversation.append(f"{role}\n{msg['content']}\n")

        # Append to file
        content = session_file.read_text()
        content += "\n".join(conversation)

        # Add summary if provided
        if summary:
            content += f"\n\n---\n\n## Summary\n\n{summary}\n"

        session_file.write_text(content)

        # Update progress
        self.progress["last_session"] = str(date.today())
        self.progress["sessions_completed"] += 1
        self._save_progress()

        print(f"✅ Session saved to: {session_file}")

        # Clear history for next session
        self.history = []

    def create_exercise(self, exercise_data: Dict) -> Path:
        """Create an exercise file."""
        ex_id = exercise_data.get(
            "id", f"ex-{self.progress['exercises_completed'] + 1:03d}"
        )
        title = exercise_data.get("title", "Untitled")

        # Sanitize filename
        filename = f"{ex_id}-{title.lower().replace(' ', '-')}.md"
        filename = re.sub(r"[^a-z0-9\-.]", "", filename)

        exercise_file = self.exercises_dir / filename

        template = f"""# Exercise {ex_id}: {title}

**Phase:** {self.progress['current_phase']}
**Created:** {date.today()}
**Status:** pending

---

## Instructions

{exercise_data.get('instructions', '')}

---

## Learning Objectives

{exercise_data.get('objectives', '')}

---

## Your Solution

```python
# Write your solution here

```

---

## Notes

"""
        exercise_file.write_text(template)
        print(f"✅ Exercise created: {exercise_file}")
        return exercise_file

    def update_progress(self, **kwargs):
        """Update progress tracking."""
        for key, value in kwargs.items():
            if key in self.progress:
                self.progress[key] = value
        self._save_progress()
        print(f"✅ Progress updated: {', '.join(kwargs.keys())}")

    def show_status(self):
        """Display current learning status."""
        print("\n" + "=" * 60)
        print("📊 LEARNING STATUS")
        print("=" * 60)
        print(f"\n📍 Current Position:")
        print(f"   Phase: {self.progress['current_phase']}")
        print(f"   Topic: {self.progress['current_topic']}")
        print(f"\n📈 Progress:")
        print(f"   Sessions: {self.progress['sessions_completed']}")
        print(f"   Exercises: {self.progress['exercises_completed']}")
        print(f"   Last session: {self.progress['last_session'] or 'Never'}")
        print(
            f"\n✅ Completed Phases: {', '.join(self.progress['phases_completed']) or 'None yet'}"
        )
        print(f"\n📁 Workspace: {self.workspace}")
        print(f"   Sessions: {len(list(self.sessions_dir.glob('*.md')))}")
        print(f"   Exercises: {len(list(self.exercises_dir.glob('*.md')))}")
        print("=" * 60 + "\n")

    def interactive_session(self):
        """Start an interactive chat session."""
        print("\n" + "=" * 60)
        print("🧠 AI MENTOR - Interactive Session")
        print("=" * 60)
        print(f"\nModel: {self.model}")
        print(
            f"Phase: {self.progress['current_phase']} - {self.progress['current_topic']}"
        )
        print("\nCommands:")
        print("  'exit' or 'quit' - End session")
        print("  'save' - Save session and continue")
        print("  'status' - Show progress")
        print("  'roadmap' - Show roadmap summary")
        print("\n" + "=" * 60 + "\n")

        while True:
            try:
                user_input = input("\n💬 You: ").strip()

                if not user_input:
                    continue

                # Handle commands
                if user_input.lower() in ["exit", "quit", "q"]:
                    if self.history:
                        save = input("\n💾 Save this session? (y/n): ").lower()
                        if save == "y":
                            summary = input("Session summary (optional): ").strip()
                            self.save_session(summary or None)
                    print("\n👋 Goodbye! Keep learning.\n")
                    break

                elif user_input.lower() == "save":
                    summary = input("Session summary: ").strip()
                    self.save_session(summary or None)
                    continue

                elif user_input.lower() == "status":
                    self.show_status()
                    continue

                elif user_input.lower() == "roadmap":
                    print("\n" + "=" * 60)
                    print(self.roadmap[:1000] if self.roadmap else "No roadmap loaded")
                    print("=" * 60 + "\n")
                    continue

                # Chat with mentor
                print("\n🤖 Mentor: ", end="", flush=True)
                response = self.chat(user_input)
                print(response)

            except KeyboardInterrupt:
                print("\n\n👋 Session interrupted. Use 'exit' to save and quit.\n")
                continue
            except Exception as e:
                print(f"\n❌ Error: {e}\n")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="AI Learning Mentor")
    parser.add_argument(
        "--workspace",
        "-w",
        help="Workspace directory",
        default=os.path.expanduser("~/learning-workspace"),
    )
    parser.add_argument("--import-roadmap", "-i", help="Import roadmap file")
    parser.add_argument(
        "--model", "-m", help="Ollama model to use", default="llama3.1:latest"
    )
    parser.add_argument(
        "--status", "-s", action="store_true", help="Show status and exit"
    )

    args = parser.parse_args()

    # Initialize mentor
    mentor = LearningMentor(workspace_dir=args.workspace)
    mentor.model = args.model

    # Import roadmap if provided
    if args.import_roadmap:
        mentor.import_roadmap(args.import_roadmap)

    # Show status if requested
    if args.status:
        mentor.show_status()
        return

    # Check if roadmap exists
    if not mentor.roadmap:
        print("\n⚠️  No roadmap found!")
        print(
            f"   Import one with: python mentor.py --import-roadmap /path/to/ROADMAP.md\n"
        )
        import_now = input("Do you have a roadmap to import? (y/n): ").lower()
        if import_now == "y":
            path = input("Path to roadmap: ").strip()
            if not mentor.import_roadmap(path):
                return
        else:
            print(
                "\n   You can still use the mentor, but it won't have roadmap context.\n"
            )

    # Start interactive session
    mentor.interactive_session()


if __name__ == "__main__":
    main()
