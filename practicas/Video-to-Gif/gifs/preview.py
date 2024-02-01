from moviepy.editor import *



# video_file = askopenfilename()
clip = (VideoFileClip("Kursk1280x720.mp4", audio=False))

clip.show(35.00, interactive = True)
