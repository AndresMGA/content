import os
import subprocess

# Path to the root directory where you want to start searching for .mscx files
root_directory = './Chromatic'

# Path to the MuseScore executable
mscore_path = '/home/andres/MuseScore/builds/Linux-Qt-usr-Make-Release/install/bin/mscore'

# Function to recursively find all .mscx files in a directory
def find_mscx_files(directory):
    mscx_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mscx'):
                mscx_files.append(os.path.join(root, file))
    return mscx_files

# Function to check if the .mscx file needs conversion based on modification time
def needs_conversion(mscx_filepath, svg_filepath):
    # Check if the SVG file exists
    if not os.path.exists(svg_filepath):
        return True  # Convert if the SVG doesn't exist
    # Compare modification times
    mscx_mtime = os.path.getmtime(mscx_filepath)
    svg_mtime = os.path.getmtime(svg_filepath)
    return mscx_mtime > svg_mtime  # Convert if .mscx is newer

# Function to convert .mscx file to .svg using MuseScore
def convert_mscx_to_svg(mscx_filepath):
    # Get the directory and basename of the file
    dir_path, basename = os.path.split(mscx_filepath)
    svg_filepath = os.path.join(dir_path, f"{os.path.splitext(basename)[0]}.svg")

    # Check if conversion is needed
    if needs_conversion(mscx_filepath, svg_filepath):
        print(f"Converting: {mscx_filepath} -> {svg_filepath}")
        # Execute the MuseScore command
        subprocess.run([mscore_path, mscx_filepath, '-o', svg_filepath], check=True)
    else:
        print(f"Skipping: {mscx_filepath} (No changes detected)")

# Main script
if __name__ == "__main__":
    # Find all .mscx files in the root directory
    mscx_files = find_mscx_files(root_directory)
    
    # Convert each .mscx file to .svg if needed
    for mscx_file in mscx_files:
        convert_mscx_to_svg(mscx_file)

    
    # Construct the command
    command = f"{mscore_path} {mscx_filepath} -o {output_filepath}"
    
    # Execute the command
    subprocess.run(command, shell=True, check=True)
    print(f"Converted: {mscx_filepath} -> {output_filepath}")

# Main execution
if __name__ == "__main__":
    # Find all .mscx files in the directory and subdirectories
    mscx_files = find_mscx_files(root_directory)

    # For each .mscx file, run the conversion
    for mscx_file in mscx_files:
        convert_mscx_to_svg(mscx_file)
