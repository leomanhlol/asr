import os
import moviepy.editor as moviepy
import subprocess


path_file = '/home/manhd/django-ajax-record/media/records/'


# ### xoa file khac
# #Change working directory
# os.chdir(path_file)

# audio_files = os.listdir()
# i=0
# # You dont need the number of files in the folder, just iterate over them directly using:
# for file in audio_files:
#     #spliting the file into the name and the extension
#     name, ext = os.path.splitext(file)
#     if ext in ['.mp3','.mp3 1','.mp3 2','.mp3 3']:
#        os.remove(file)
#        i+=1
#        print('removed '+str(i) +' file')



### create wav files
#Change working directory
# k=open(path_file+"records/audiorecord.webm".split("/")[1],mode="r")
def conv(k):
    # path_file = '/home/manhd/django-ajax-record/media/records'
    os.chdir(path_file)

    audio_files = os.listdir()
    # i=0
    # # You dont need the number of files in the folder, just iterate over them directly using:
    # for file in audio_files:
        #spliting the file into the name and the extension
    name, ext = os.path.splitext(k.name)
    name= name.split("/")[-1]
    if ext == ".webm":
        os.system(" ffmpeg -i \"{}.webm\" -vn -acodec copy \"{}.opus\"".format(name, name)) 
        os.system(" ffmpeg -i \"{}.opus\" \"{}.wav\"".format(name, name))
        # os.remove("{}.opus".format(name))
        return "{}.wav".format(name)
    






