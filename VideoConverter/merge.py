from moviepy.editor import *
  
# loading video gfg
clip = VideoFileClip("")
  

  
# loading audio file
audioclip = AudioFileClip("")
  
# adding audio to the video clip
videoclip = clip.set_audio(audioclip)
  
# showing video clip
videoclip.ipython_display()