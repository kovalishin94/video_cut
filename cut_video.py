import configparser
from typing import List
from moviepy.editor import VideoFileClip, concatenate_videoclips


def read_config(config_file: str):
    config = configparser.ConfigParser()
    config.read(config_file)
    
    input_file = config.get('settings', 'input_file')
    output_file = config.get('settings', 'output_file')
    
    times = config.get('settings', 'start_end_times')
    times_list = [
        tuple(map(int, t.split(','))) 
        for t in times.split(';')
    ]
    
    return input_file, output_file, times_list

def cut_video(input_file: str, output_file: str, times: List[tuple]) -> None:
    video = VideoFileClip(input_file)
    clips = [video.subclip(start, end) for start, end in times]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_file, codec="libx264")

if __name__ == "__main__":
    input_file, output_file, times_list = read_config("config.ini")
    cut_video(input_file, output_file, times_list)

