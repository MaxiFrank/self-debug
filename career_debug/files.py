"""
This module provides functions for reading and appending entries to a career log file.
"""

from datetime import datetime
from pathlib import Path
from config import MAIN_DIR

DATA_DIR = MAIN_DIR / "data"
LOG_PATH = DATA_DIR / "data.md"


def read_file(file: str, directory: Path = DATA_DIR) -> str:
    """Read a file from the data directory."""
    path = directory / file
    with path.open(encoding="utf-8") as handle:
        return handle.read()


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
