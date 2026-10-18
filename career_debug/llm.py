"""
This module provides a class for interacting with an LLM model.
"""

import ollama
from files import read_file, append_entry
from config import MAIN_DIR

LOG_PATH = MAIN_DIR / "data" / "data.md"


class LLM:
    """A class for interacting with an LLM model."""

    def __init__(self, model):
        """Initialize the LLM model."""
        self.model = model

    def model_generate(self, prompt):
        """Generate a response from the LLM model."""
        response = ollama.generate(model=self.model, prompt=prompt)
        return response.response


if __name__ == "__main__":
    llm = LLM(model="gemma4:26b")
    content = read_file("../data/data.md")
    answer = llm.model_generate(prompt=content)
    append_entry(text=answer, path=LOG_PATH)
