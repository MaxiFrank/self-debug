"""
Run the career debug CLI.
"""

from commands import CustomParser
from files import append_entry


def run_cli() -> None:
    """Run the career debug CLI."""
    args = CustomParser().parse()
    path = append_entry(text=args.text)
    # TODO: replace with logging system
    print(f"Saved {args.career_action} to {path}")


if __name__ == "__main__":
    run_cli()
