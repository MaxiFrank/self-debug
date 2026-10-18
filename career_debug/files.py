"""
This module provides functions for reading and appending entries to a career log file.
"""

from datetime import datetime
from pathlib import Path
from config import MAIN_DIR

LOG_PATH = MAIN_DIR / "data" / "data.md"


def read_file(path=LOG_PATH):
    """Read the content of the career log file."""
    with open(path, encoding="utf-8") as f:
        content = f.read()
        return content


def append_entry(text: str, path: Path = LOG_PATH) -> Path:
    """Append one timestamped entry to the career markdown log."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("# Career log\n", encoding="utf-8")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n## {timestamp}\n\n{text}\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(entry)
    return path
