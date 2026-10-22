"""
Write career notes, questions, resource URLs, and what you've done.

Usage:
    python career_debug/main.py career notes "I'm feeling overwhelmed"
    python career_debug/main.py career questions "What are the best ways to learn Python?"
    python career_debug/main.py career resource "https://www.thisisgoodresource.com"
    python career_debug/main.py career done "I finished the Python tutorial"
"""

import argparse


class CustomParser:
    """
    Builds the career CLI.
    """

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            description="Save career notes, questions, resource URLs, and what you've done.",
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

        resource = career_subparsers.add_parser("resource", help="Save a resource URL")
        resource.add_argument("text", help="Resource URL")

        done = career_subparsers.add_parser("done", help="Save what you've done")
        done.add_argument("text", help="What you did")

    def parse(self) -> argparse.Namespace:
        """Parse the command line arguments."""
        return self.parser.parse_args()
