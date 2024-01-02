from moviepy.editor import VideoFileClip 

clip1 = VideoFileClip("one.mp4").subclip(0,5)
clip2 = VideoFileClip("one.mp4").subclip(5,10)
clip3 = VideoFileClip("one.mp4").subclip(10,15)
clip4 = VideoFileClip("one.mp4").subclip(15,20)
clip5 = VideoFileClip("one.mp4").subclip(20,25)
clip6 = VideoFileClip("one.mp4").subclip(25,30)
clip7 = VideoFileClip("one.mp4").subclip(35,40)
clip8 = VideoFileClip("one.mp4").subclip(45,50)
clip9 = VideoFileClip("one.mp4").subclip(55,60)
clip10 = VideoFileClip("one.mp4").subclip(65,70)
clip11 = VideoFileClip("one.mp4").subclip(75,80)

combined = concatenate_videoclips([clip1,clip2,clip3])
combined.write_videofile("combined.mp4")