import os

def print_python_files(directory, base_directory):
    """
    Recursively prints all Python files in the given directory relative to base_directory.

    :param directory: The root directory to start searching from.
    :param base_directory: The base directory to calculate relative paths.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                # Calculate the relative path
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, base_directory)
                print(f"('{relative_path}' ,'.'),")

# Specify the root directory of your project
project_directory = 'F:/python_desktop_application/backup_2/VA_App_Desktop'
base_directory = project_directory

# Call the function to print all Python files relative to VA_App_Desktop
print_python_files(project_directory, base_directory)
