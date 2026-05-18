import os

def write_file(working_directory, file_path, content):
    try:

        # Get absolute path of working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Build and normalise the full target path
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
            
        # Security check — target must be inside working directory
        valid_target = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            
        # Must be a file #return error when it IS a directory
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Create any missing parent directories
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        # Write content to file
        with open(target_file, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
