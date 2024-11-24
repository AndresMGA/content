import os
import shutil

# Paths to the directories
json_path = './json'
chromatic_path = './chromatic'
diatonic_path = './diatonic'

# Function to find the matching folder recursively
def find_matching_folder(base_name, root_paths):
    for root_path in root_paths:
        for dirpath, dirnames, filenames in os.walk(root_path):
            if os.path.basename(dirpath) == base_name:
                return dirpath
    return None

# List of root directories to search for matching folders
search_paths = [chromatic_path, diatonic_path]

# Iterate through all .json files in ./json
for root, dirs, files in os.walk(json_path):
    for file in files:
        if file.endswith('.json'):
            # Full path of the JSON file
            json_file_path = os.path.join(root, file)
            
            # Base name of the JSON file (without extension)
            base_name = os.path.splitext(file)[0]
            
            # Find the matching folder recursively
            matching_folder = find_matching_folder(base_name, search_paths)
            
            if matching_folder:
                # Copy the JSON file into the matching folder
                destination_path = os.path.join(matching_folder, file)
                shutil.copy(json_file_path, destination_path)
                print(f"Copied {json_file_path} to {destination_path}")
            else:
                # If no matching folder is found
                print(f"No matching folder found for {json_file_path}")
