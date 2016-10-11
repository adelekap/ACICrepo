import os
import sys

#args[0] = file args[1]=framenumber
commandlineArgs = sys.argv[1:]
POV_File = commandlineArgs[0]

bashCommand = "/home/u14/akoutia/homework/hw10/povray/3.7.0.0_1/bin/povray +I/home/u14/akoutia/homework/hw10/ChessPOV/ChessGame.txt +L/home/u14/akoutia/homework/hw10/ChessPOV +O/home/u14/akoutia/homework/hw10/Frames/" + commandlineArgs[1] + ".png +H1000 +W1000"

os.system(bashCommand)

