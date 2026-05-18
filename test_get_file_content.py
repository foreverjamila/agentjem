from functions.get_file_content import get_file_content

# Test truncation
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

# Test normal file reads
print("\nmain.py contents:")
print(get_file_content("calculator", "main.py"))

print("\npkg/calculator.py contents:")
print(get_file_content("calculator", "pkg/calculator.py"))

# Test error cases
print("\n/bin/cat result:")
print(get_file_content("calculator", "/bin/cat"))

print("\npkg/does_not_exist.py result:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))