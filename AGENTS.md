# Repository Guidelines

## Project Structure & Module Organization
- `get_requests.py`: Simple GET request example against the ReqRes API.
- `post_requests.py`: Simple POST request example with basic assertions.
- `README.md`: Minimal project description.

There is no dedicated `src/` or `tests/` directory; the Python scripts live at the repo root.

## Build, Test, and Development Commands
- `python get_requests.py`: Runs the GET example and prints status, headers, and JSON.
- `python post_requests.py`: Runs the POST example and validates the response with assertions.
- `python -m venv .venv && source .venv/bin/activate`: Optional local virtual environment.
- `pip install requests`: Install the only external dependency used by the scripts.

## Coding Style & Naming Conventions
- Indentation: 4 spaces (Python default).
- Naming: use descriptive snake_case for variables (e.g., `json_response`, `payload`).
- Keep scripts short and focused; prefer explicit variable names over abbreviations.

## Testing Guidelines
- There is no test framework configured. The POST script uses inline `assert` statements as lightweight checks.
- If adding tests, place them under a new `tests/` directory and name files `test_*.py`.
- Keep API-dependent checks deterministic; validate status codes and key fields.

## Commit & Pull Request Guidelines
- Commit history currently contains a single “Initial commit” message; no established convention.
- Prefer concise, imperative commit messages (e.g., “Add POST response assertions”).
- PRs should include: a brief summary, how to run the scripts, and any API changes.
- Add screenshots only if introducing UI or web artifacts (not typical for this repo).

## Security & Configuration Tips
- These scripts call the public `https://reqres.in` API; avoid committing secrets or tokens.
- If you add configuration (e.g., base URLs), prefer environment variables and document them here.
