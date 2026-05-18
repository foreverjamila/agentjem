from functions.run_python_file import run_python_file

print("--- main.py (no args) ---")
print(run_python_file("calculator", "main.py"))

print("\n--- main.py (with args) ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("\n--- tests.py ---")
print(run_python_file("calculator", "tests.py"))

print("\n--- ../main.py (outside working directory) ---")
print(run_python_file("calculator", "../main.py"))

print("\n--- nonexistent.py ---")
print(run_python_file("calculator", "nonexistent.py"))

print("\n--- lorem.txt (not a Python file) ---")
print(run_python_file("calculator", "lorem.txt"))