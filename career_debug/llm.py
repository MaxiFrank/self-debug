"""
This module provides a class for interacting with an LLM model.
"""

from typing import List
import ollama
from files import read_file, append_entry
from config import MAIN_DIR

LOG_PATH = MAIN_DIR / "data" / "data.md"

files = {
    "resume": "resume.md",
    "work_summary": "current_work_summary.md",
    "resource": "resource.md",
}


class LLM:
    """A class for interacting with an LLM model."""

    def __init__(self, model: str):
        """Initialize the LLM model."""
        self.model = model

    def model_generate(self, prompt: str, system: str = ""):
        """Generate a response from the LLM model."""
        response = ollama.generate(model=self.model, prompt=prompt, system=system)
        return response.response

    def get_context(self, files):
        # add typing
        resume = read_file(file=files["resume"])
        work_summary = read_file(file=files["work_summary"])
        resource = read_file(file=files["resource"])
        return resume, work_summary, resource


if __name__ == "__main__":
    llm = LLM(model="gemma4:26b")
    resume, work_summary, resource = llm.get_context(files)
    content = read_file("data.md")
    answer = llm.model_generate(system=resume + work_summary + resource, prompt=content)
    append_entry(text=answer, path=LOG_PATH)
