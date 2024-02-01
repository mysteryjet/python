from moviepy.editor import *
# from tkinter.filedialog import *

def time_symetrize(clip):

    return concatenate([clip, clip.fx( vfx.time_mirror )])

# video_file = askopenfilename()
clip = (VideoFileClip("Kursk1280x720.mp4", audio=False).subclip((35.00),(37.00)).resize(0.5).crop(x1=150, x2=350).fx( time_symetrize))

clip.write_gif("test.gif", fps=15, fuzz=2)

