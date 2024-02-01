from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

video_file = askopenfilename()
clip = (VideoFileClip(video_file)).subclip((0,42.00),(0,46.59))
clip.write_gif("ouput.gif", fps=10)