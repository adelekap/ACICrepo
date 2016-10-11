import os
import sys

commandlineArgs = sys.argv[1:]

os.system("/home/u14/akoutia/homework/hw10/ffmpeg/3.1.3/bin/ffmpeg -r " + commandlineArgs[0] + " -i %03d.png -r ntsc " + commandlineArgs[1] +"-y")