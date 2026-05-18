import os
from config import MAX_FILE_CHARS

def get_file_content(working_directory, file_path):
    try:
        # Get absolute path of working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Build and normalise the full target path
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Security check — target must be inside working directory
        valid_target = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Must be a file
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read file contents up to MAX_FILE_CHARS
        with open(target_file, "r") as f:
            content = f.read(MAX_FILE_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_FILE_CHARS} characters]'
        return content

    except Exception as e:
        return f"Error: {e}"

    
