import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:

        # Get absolute path of working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Build and normalise the full target path
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
            
        # Security check — target must be inside working directory
        valid_target = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            
        # Must be a file
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # Must be Python file
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        # Build the command
        command = ["python", target_file]
        if args:
            command.extend(args)
        
        # Run the subprocess
        result = subprocess.run(
            command,
            cwd=working_dir_abs, 
            capture_output=True, 
            text=True, timeout=30
        )
        
        # Build output string
        output = []
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        if not result.stdout and not result.stderr:
            output.append(f"No output produced")
        
        else:
            if result.stdout:
                output.append(f"STDOUT:\n{result.stdout}")

            if result.stderr:
                output.append(f"STDERR:\n{result.stderr}")

        
        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
