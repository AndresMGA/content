import os
import xml.etree.ElementTree as ET

# Paths to the root directories where you want to start searching for .mscx files
directories_to_check = ['./Chromatic', './Diatonic']

# Function to recursively find all .mscx files in a directory
def find_mscx_files(directories):
    mscx_files = []
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.mscx'):
                    mscx_files.append(os.path.join(root, file))
    return mscx_files

# Function to check if a .mscx file contains the specific VBox structure
def contains_vbox_with_title(mscx_filepath):
    try:
        # Parse the .mscx file as XML
        tree = ET.parse(mscx_filepath)
        root = tree.getroot()

        # Search for <VBox> elements
        for vbox_element in root.iter('VBox'):
            text_element = vbox_element.find('Text')
            if text_element is not None:
                style_element = text_element.find('style')
                if style_element is not None and style_element.text == 'Title':
                    text_content_element = text_element.find('text')
                    if text_content_element is not None:
                        return True
        return False
    except ET.ParseError as e:
        print(f"Error parsing {mscx_filepath}: {e}")
        return False

# Main execution
if __name__ == "__main__":
    # Find all .mscx files in both directories
    mscx_files = find_mscx_files(directories_to_check)

    # Check each .mscx file for the VBox structure
    for mscx_file in mscx_files:
        if contains_vbox_with_title(mscx_file):
            print(f"VBox with Title Text found in: {mscx_file}")
