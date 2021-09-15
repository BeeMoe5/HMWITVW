import os
from os.path import expanduser, isdir, splitext, isfile

import cv2


def file_check(s):
    return isdir(s) or splitext(s)[1] == '.mp4'


def find_file():
    os.chdir(expanduser('~'))
    while True:
        text = "[0] Go back a directory\n"
        options = {}
        listdir = list(filter(file_check, os.listdir()))
        for n, filename in enumerate(listdir, start=1):
            text += f"[{n}] {filename}\n"
            options[n] = filename
            
        print(text)
        option = input('Enter a number corresponding to the options above or "stop" to stop: ')
        if option.lower() == 'stop':
            exit()
        
        if option.isdigit():
            option = int(option)
            
            if option == 0:
                os.chdir('../')
                continue
            
            try:
                option = options[option]
            except KeyError:
                print('Invalid number range')
                continue
                
            if isdir(option):
                os.chdir(option)
                continue
                
            if isfile(option):
                return option
        
        else:
            print('Invalid option')


def main():
    f_path = find_file()
    cap = cv2.VideoCapture(f_path)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    video_length = frame_count / fps
    print(f"{frame_count=}, {fps=}, {video_length=}")


if __name__ == '__main__':
    main()
