"""
Run the career debug CLI.
"""

from commands import CustomParser, append_entry


def run_cli() -> None:
    """Run the career debug CLI."""
    args = CustomParser().parse()
    path = append_entry(args.career_action, args.text)
    # TODO: replace with logging system
    print(f"Saved {args.career_action} to {path}")


if __name__ == "__main__":
    run_cli()
