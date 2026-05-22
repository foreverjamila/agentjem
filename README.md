# agentjem 🤖

A command-line AI agent powered by the Google Gemini API, capable of reading, writing, and executing Python code autonomously. Built as part of the [Boot.dev](https://boot.dev) guided project — *Build an AI Agent in Python*.

---

## What It Does

agentjem is a coding agent that accepts a natural language task, reasons about it using Gemini, and uses a set of tools to complete the task — all on its own. It can:

- Explore a project's file structure
- Read source code files
- Write and overwrite files
- Execute Python scripts and capture their output
- Loop through multiple steps until the task is complete

Think of it as a lightweight version of tools like Claude Code or Cursor's Agent Mode, built from scratch.

---

## How It Works

The agent follows a feedback loop:

```
User prompt
    ↓
Gemini reasons about the task
    ↓
Gemini requests a tool call (e.g. read this file)
    ↓
agentjem executes the function
    ↓
Result is fed back to Gemini
    ↓
Gemini reasons again → more tool calls or final answer
    ↓
Final response printed to console
```

This loop runs for a maximum of 20 iterations to prevent runaway token usage.

---

## Project Structure

```
agentjem/
├── main.py                   # Agent entry point and main loop
├── call_function.py          # Function dispatcher and tool declarations
├── prompts.py                # System prompt for the agent
├── config.py                 # Configuration constants (e.g. MAX_FILE_CHARS)
├── functions/
│   ├── get_files_info.py     # Lists directory contents
│   ├── get_file_content.py   # Reads file contents (with truncation)
│   ├── write_file.py         # Writes or overwrites files
│   └── run_python_file.py    # Executes Python files as subprocesses
├── calculator/               # Sample project the agent works on
│   ├── main.py
│   ├── tests.py
│   └── pkg/
│       ├── calculator.py
│       └── render.py
├── test_get_files_info.py    # Manual test script
├── test_get_file_content.py  # Manual test script
├── test_write_file.py        # Manual test script
└── test_run_python_file.py   # Manual test script
```

---

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) package manager
- A [Google AI Studio](https://aistudio.google.com/) account and Gemini API key

---

## Setup

**1. Clone the repository:**
```bash
git clone https://github.com/foreverjamila/agentjem.git
cd agentjem
```

**2. Create and activate a virtual environment:**
```bash
uv venv
source .venv/bin/activate
```

**3. Install dependencies:**
```bash
uv sync
```

**4. Create a `.env` file in the project root and add your Gemini API key:**
```
GEMINI_API_KEY='your_api_key_here'
```

> ⚠️ Never commit your `.env` file. It is already listed in `.gitignore`.

---

## Usage

**Basic prompt:**
```bash
uv run main.py "how does the calculator render results to the console?"
```

**With verbose output (shows token usage and function call details):**
```bash
uv run main.py "run the calculator tests and tell me if they pass" --verbose
```

**Ask it to fix a bug:**
```bash
uv run main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20"
```

---

## Agent Tools

All tools are scoped to the `./calculator` working directory. The agent cannot access files outside this directory — path traversal attempts are blocked at the function level using `os.path.commonpath()`.

| Tool | What it does |
|---|---|
| `get_files_info` | Lists files and directories with sizes |
| `get_file_content` | Reads file contents, truncated at 10,000 characters |
| `write_file` | Writes or overwrites a file, creates parent dirs if needed |
| `run_python_file` | Runs a Python file as a subprocess with a 30s timeout |

---

## Security

Each tool validates that the requested path is inside the permitted working directory before doing anything. The working directory is injected by the agent's Python code — the LLM never controls it directly.

```python
# Path validation used in every tool
valid = os.path.commonpath([working_dir_abs, target]) == working_dir_abs
```

---

## Dependencies

| Package | Version | Purpose |
|---|---|---|
| `google-genai` | 1.12.1 | Gemini API client |
| `python-dotenv` | 1.1.0 | Load API key from `.env` |

---

## What I Learned Building This

- How LLM APIs work — sending structured conversations, not just single prompts
- Function calling — giving an LLM a menu of tools and letting it decide which to use
- Agentic feedback loops — the agent acts, observes the result, and acts again
- Path security — preventing directory traversal with `commonpath()`
- Subprocess execution — running Python files programmatically and capturing output
- Token management — tracking and limiting token usage in LLM interactions
- System prompts — shaping agent behaviour before any user input arrives

---

## Built With

- [Google Gemini API](https://ai.google.dev/)
- [Boot.dev — Build an AI Agent in Python](https://boot.dev)
