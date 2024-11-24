import os

# Path to the chromatic directory
chromatic_path = './Diatonic'

# Function to convert a string to Title Case
def to_title_case(name):
    return '_'.join([word.capitalize() for word in name.split('_')])

# Traverse the directory structure
for root, dirs, files in os.walk(chromatic_path, topdown=False):  # Process files and subdirectories first
    # Rename files
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_name = to_title_case(file)
        new_file_path = os.path.join(root, new_file_name)
        if old_file_path != new_file_path:  # Prevent unnecessary renames
            os.rename(old_file_path, new_file_path)
            print(f"Renamed file: {old_file_path} -> {new_file_path}")

    # Rename directories
    for dir in dirs:
        old_dir_path = os.path.join(root, dir)
        new_dir_name = to_title_case(dir)
        new_dir_path = os.path.join(root, new_dir_name)
        if old_dir_path != new_dir_path:  # Prevent unnecessary renames
            try:
                os.rename(old_dir_path, new_dir_path)
                print(f"Renamed directory: {old_dir_path} -> {new_dir_path}")
            except OSError as e:
                print(f"Error renaming directory: {old_dir_path} -> {new_dir_path} | {e}")
