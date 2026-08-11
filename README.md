# AgentJem

An AI coding agent powered by Google Gemini that can read files, write files, and execute Python code in a working directory — built as part of the Boot.dev "Build an AI Agent" course.

## What it does

AgentJem takes a natural language instruction and uses the Gemini API to decide which actions to take. It can:

- **List files and directories** to explore a project's structure
- **Read file contents** to understand existing code
- **Write or overwrite files** to create or update code
- **Run Python files** and capture their output

The agent loops through function calls until it completes the task, reporting back what it did at each step.

## How it works

1. You give the agent a prompt describing what you want done
2. Gemini decides which function to call (get files info, get file content, write file, or run python file)
3. `call_function.py` executes that function and returns the result to Gemini
4. This repeats until Gemini decides the task is complete and returns a final response

## Project structure

```
functions/       # Function schemas and implementations (list, read, write, run)
calculator/       # Sample working directory the agent operates on
call_function.py  # Routes Gemini's function calls to the right implementation
config.py         # Configuration (working directory limits, etc.)
main.py           # Entry point — takes a prompt, runs the agent loop
prompts.py        # System prompt defining the agent's behavior and available tools
```

## Setup

1. Clone the repo and install dependencies with `uv sync`
2. Add your Gemini API key to a `.env` file: `GEMINI_API_KEY=your_key_here`
3. Run the agent:
   ```
   uv run main.py "your instruction here"
   ```

## Requirements

Python 3.13+, a Google Gemini API key
