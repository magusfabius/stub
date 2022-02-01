import os 


def execute_command_line(command):
    os.system(command)  


# install ffmpeg
command = "ffmpeg -i largefile.mp4 -sameq -ss 00:00:00 -t 00:50:00 smallfile.mp4"