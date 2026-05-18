import os

def get_files_info(working_directory, directory="."):
    try:
        # Get absolute path of working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Build and normalise the full target path
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # Security check — target must be inside working directory
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Must be a directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        return f'Success: "{directory}" is within the working directory'

    except Exception as e:
        return f"Error: {e}"