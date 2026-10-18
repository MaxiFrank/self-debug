# self-debug

commands to run:
poetry run python ./career_debug/main.py career notes "notes to add"
poetry run python ./career_debug/main.py career questions "career questions to add"
poetry run python ./career_debug/main.py career job "https://example.com/job/123"
poetry run python ./career_debug/main.py career done "what I did"

Chat, run separately from the commands above:
poetry run python ./career_debug/llm.py

notes, questions, job, and done append to data/data.md.
The chat reads that file, asks the local model, and appends the answer there too.
Ollama stays running. Each command starts, does one thing, and exits.
data folder is gitignored.
