import os, shutil, urllib.parse

def is_empty_or_whitespace(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return content.strip() == ''

def is_single_url(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        # Split content by newlines and remove empty strings
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        
        # Check if there is exactly one line and it looks like a URL
        if len(lines) == 1:
            parsed = urllib.parse.urlparse(lines[0])
            return parsed.scheme != '' and parsed.netloc != ''
        
        return False

def move_directory(directory_path, destination_dir):
    directory_name = os.path.basename(directory_path)
    destination_path = os.path.join(destination_dir, directory_name)

    shutil.move(directory_path, destination_path)
    print(f"Moved directory {directory_path} to {destination_path}")

def process_files(directory, destination_dir):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # Check if file meets the conditions
            if is_empty_or_whitespace(file_path) or is_single_url(file_path):
                # Move the directory containing this file
                move_directory(root, destination_dir)
                # No need to check other files in this directory
                break

if __name__ == "__main__":
    # Specify your source directory and destination directory here
    source_directory = '/path/to/source/directory'
    destination_directory = '/path/to/destination/directory'

    # Create the destination directory if it doesn't exist
    os.makedirs(destination_directory, exist_ok=True)

    process_files(source_directory, destination_directory)
