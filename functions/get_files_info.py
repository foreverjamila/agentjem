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
        

        # List directory contents
        contents = []
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            contents.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
        
        return "\n".join(contents)

    except Exception as e:
        return f"Error: {e}"