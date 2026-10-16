"""
Write career notes, questions, job URLs, and what you've done.

Usage:
    python career_debug/main.py career notes "I'm feeling overwhelmed"
    python career_debug/main.py career questions "What are the best ways to learn Python?"
    python career_debug/main.py career job "https://www.linkedin.com/jobs/view/3821301999/"
    python career_debug/main.py career done "I finished the Python tutorial"
"""

import argparse
from datetime import datetime
from pathlib import Path
from config import MAIN_DIR

LOG_PATH = MAIN_DIR / "data" / "career.md"


class CustomParser:
    """
    Builds the career CLI.
    """

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            description="Save career notes, questions, job URLs, and what you've done.",
        )
        self._add_commands()

    def _add_commands(self) -> None:
        subparsers = self.parser.add_subparsers(dest="command", required=True)
        career_parser = subparsers.add_parser("career", help="Career log commands")
        career_subparsers = career_parser.add_subparsers(
            dest="career_action",
            required=True,
        )

        notes = career_subparsers.add_parser("notes", help="Save a career thought")
        notes.add_argument("text", help="The note to save")

        questions = career_subparsers.add_parser(
            "questions", help="Save an open question"
        )
        questions.add_argument("text", help="The question to save")

        job = career_subparsers.add_parser("job", help="Save a job posting URL")
        job.add_argument("text", help="Job posting URL")

        done = career_subparsers.add_parser("done", help="Save what you've done")
        done.add_argument("text", help="What you did")

    def parse(self) -> argparse.Namespace:
        """Parse the command line arguments."""
        return self.parser.parse_args()


def append_entry(kind: str, text: str, path: Path = LOG_PATH) -> Path:
    """Append one timestamped entry to the career markdown log."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("# Career log\n", encoding="utf-8")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n## {timestamp}\n\n**{kind}**\n\n{text.strip()}\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(entry)
    return path
