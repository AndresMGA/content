import os
import shutil

# Directories to check and copy .json files from
source_directory = './songs'
destination_directory = './Diatonic/Songs'

# Function to check folders and copy missing .json files
def ensure_json_in_folders(source_directory, destination_directory):
    # Walk through each folder in the destination directory
    for folder in os.listdir(destination_directory):
        folder_path = os.path.join(destination_directory, folder)
        
        # Ensure we only process directories
        if not os.path.isdir(folder_path):
            continue
        
        # Check if this folder already contains a .json file
        json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
        
        if json_files:
            print(f"Folder '{folder}' already contains a .json file. Skipping.")
        else:
            # If no .json file, check for the corresponding .json file in the source directory
            matching_json_file = f"{folder}.json"
            source_json_path = os.path.join(source_directory, matching_json_file)
            
            if os.path.exists(source_json_path):
                # Copy the .json file to the folder
                destination_json_path = os.path.join(folder_path, matching_json_file)
                shutil.copy(source_json_path, destination_json_path)
                print(f"Copied '{matching_json_file}' from '{source_directory}' to '{folder_path}'")
            else:
                print(f"No matching .json file found for folder '{folder}' in source directory.")

# Main execution
if __name__ == "__main__":
    ensure_json_in_folders(source_directory, destination_directory)
