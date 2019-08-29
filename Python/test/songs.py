
#/home/jeen/Bash/Python/myvenv/bin
# from mp3_tagger import MP3File,VERSION_1,VERSION_2,VERSION_BOTH
import eyed3
import os

file = "Taylor Swift And Ed Sheeran - End Game (feat. Future).mp3"

load = eyed3.load(file)

# tags = MP3File(file).get_tags()
print(load.tag.artist)
print(load.tag.title)
# load.tag.album = ''
# load.tag.save()
# print(load.tag.album)

def fileTagInfo(song):
    audio = eyed3.load(song)
    return audio.tag.artist + " - " + audio.tag.title

path = "/media/jeen/Transcend/AAA[JUST BEST]/РОК/РОК 1 ( + - - )/"

songsList = os.listdir(path)
songs = []
# print(songs)

for i in songsList:
    songs.append(path+i)
    # print(i)

# print(songs)

for i in songs:
    # print(i)
    try:
        if isinstance(fileTagInfo(i), str) :
            print(fileTagInfo(i))
    except Exception as e:
        print(e)





