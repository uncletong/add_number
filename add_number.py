import tinytag
import sys
import os

path = sys.argv[1]
files = os.listdir(path)
tags = list()

try:
    for file in files:
        tags.append([file, tinytag.TinyTag.get(path + "\\" + file).track])
except tinytag.tinytag.TinyTagException:
    pass

for tag in tags:
    track_num = tag[1] + "."
    if len(track_num) == 2:
        track_num = "0" + track_num
    track_name = tag[0]
    track_name = track_name[track_name.index("-") + 1:]
    track_name = track_num + track_name
    os.rename(path + "\\" + tag[0], path + "\\" + track_name)
    print("rename " + track_name + " success!")


