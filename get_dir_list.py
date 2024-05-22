import os, sys

# gets all directories in a folder and write them to a text file
def write_dirs_to_file(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(folder_path):
            for directory in dirs:
                dir_path = os.path.join(root, directory)
                f.write(f"{directory}: {dir_path}\n")
    
    print("Directories written to", output_file)

def sup_dirs_to_file(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in os.listdir(folder_path):
            f.write(f"{item} : {os.path.join(folder_path, item)}\n")

if __name__ == "__main__":
    folder_path, output_file, mode = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        if mode == '0': write_dirs_to_file(folder_path, output_file)
        elif mode == '1': sup_dirs_to_file(folder_path, output_file)
    except IndexError:
        print("Error: missing necessary arguments to run program")
        print("Input: folder_path, output_file, mode")
        sys.exit(1)