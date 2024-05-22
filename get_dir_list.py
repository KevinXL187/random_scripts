import os, sys

# gets all directories in a folder and write them to a text file
def write_dirs_to_file(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(folder_path):
            for directory in dirs:
                dir_path = os.path.join(root, directory)
                f.write(f"{directory}: {dir_path}\n")
    
    print("Directories written to", output_file)

if __name__ == "__main__":
    folder_path, output_file = sys.argv[1], sys.argv[2]
    try:
        write_dirs_to_file(folder_path, output_file)
    except IndexError:
        print("Error: missing necessary arguments to run program")
        print("Input: folder_path, output_file")
        sys.exit(1)