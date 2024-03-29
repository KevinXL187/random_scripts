import cv2, sys, os

def extract_frame(path, output_folder):
    video = cv2.VideoCapture(path)
    name = os.path.basename(path)

    status = True
    count = 0
    while status:
        status, image = video.read()
        if status:
            output_dir = os.path.join(output_folder, name)
            if not os.path.exists(output_dir): os.mkdir(output_dir)

            output_path = os.path.join(output_folder, name, f"frame{count}.png")
            cv2.imwrite(output_path, image)
            count += 1

    # print(f"{count} frames extracted.")
    
def extract_multiple_video(path, output_folder):
    for files in os.listdir(path):
        file_path = os.path.join(path, files)
        if os.path.isfile(file_path):
            extract_frame(file_path, output_folder)

if __name__ == "__main__":
    try:
        video_path, output_folder, type = sys.argv[1], sys.argv[2], sys.argv[3]
    except IndexError:
        print("Error: missing necessary arguments to run program")
        print("Input: video folder path, output folder path, single or multiple")
        sys.exit(1)
    
    if type == '0' or type == 'single':
        extract_frame(video_path, output_folder)
    elif type == '1' or type == 'multiple':
        extract_multiple_video(video_path, output_folder)
    else:
        print("invalid type")
        sys.exit(1)
