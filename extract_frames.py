import cv2, os
import numpy as np

def convert_timeStrings_to_seconds(time):
    if time.count(':') == 2:
        start_list = time.splilt(':')
        hours, minutes, seconds = int(start_list[0]), int(start_list[1]), int(start_list[2])

        minutes = minutes +  (hours * 60)
        seconds = seconds + (minutes * 60)
    elif time.count(':') == 1:
        start_list = time.split(':')
        minutes, seconds = int(start_list[0]), int(start_list[1])

        seconds = seconds + (minutes * 60)
    elif time.count(':') == 0:
        seconds = int(time)
    
    return seconds

def extract_frame(path, output_folder, start_time=None, end_time=None):
    try:
        video = cv2.VideoCapture(path)
        duration = int(video.get(cv2.CAP_PROP_FRAME_COUNT))/ video.get(cv2.CAP_PROP_FPS)

        if not video.isOpened():
            print("Error: Could not Open Video")
            return

        #checking timestamp
        if start_time != None and end_time != None:

            #converting timestamp to seconds, "hours:minutes:seconds"
            start_time = convert_timeStrings_to_seconds(start_time)
            end_time = convert_timeStrings_to_seconds(end_time)

            if start_time < 0 or start_time > duration:
                print('Error: Start time is out of bounds')
                return
            if end_time < 0 or end_time > duration:
                print('Error: End time is out of bounds')
                return
            if start_time >= end_time:
                print('Error: End time must be greater than Start time')
                return
        else:
            start_time = 0
            end_time = duration
    except FileNotFoundError:
        print("Error: File not Found")
    
    #get name of file, create folder for file if folder does not exists
    name = os.path.basename(path)
    output_folder =os.path.join(output_folder, 'output')
    output_dir = os.path.join(output_folder, name)
    
    if not os.path.exists(output_folder): os.mkdir(output_folder)
    if not os.path.exists(output_dir): os.mkdir(output_dir)

    #set current position to start_frame and calculate last frame
    video.set(cv2.CAP_PROP_POS_MSEC, start_time * 1000)
    end_frame = end_time * video.get(cv2.CAP_PROP_FPS)

    #loop through video to convert to frames
    status = True
    count = 0
    while status:
        status, image = video.read()
        if not status: continue

        output_path = os.path.join(output_folder, name, f"frame{count}.png")

        is_success, im_buff_arr = cv2.imencode(".png", image)
        im_buff_arr.tofile(output_path)

        count += 1
        if count >= end_frame: break
    # print(f"{count} frames extracted.")
    
def extract_multiple_video(path, output_folder):
    for files in os.listdir(path):
        file_path = os.path.join(path, files)
        if os.path.isfile(file_path):
            extract_frame(file_path, output_folder)

if __name__ == "__main__":
    video_path = input('Enter Video Path\n') 
    output_folder = input('Enter Output Location\n')
    type = input('Enter 0 if single file, 1 otherwise\n')

    if type == '0' or type == 'single':

        start_frame = input('Enter timestamp of first frame\n')
        end_frame = input('Enter timestamp  of last frame\n')
        extract_frame(video_path, output_folder, start_frame, end_frame)

    elif type == '1' or type == 'multiple': extract_multiple_video(video_path, output_folder)
    else: print("invalid type")