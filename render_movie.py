import os
import sys


pov_file = "ChessGame.txt"

base_name = "frame"

frame_number = 0

opening_frames = ["<-5,20,-15>", "<-5,20,-15>", "<-5,20,-15>", "<-4,19,-14>", "<-3,18,-13>", "<-2,17,-12>",
                  "<-1,16,-11>", "<0,15,-10>", "<1,14,-9>", "<2,13,-8>",
                  "<3,12,-7>", "<4,11,-6>", "<5,10,-5>", "<6,9,-4>", "<7,8,-3>", "<8,7,-2>", "<9,6,-1>", "<10,5,0>",
                  "<10,5,0>", "<10,5,0>"]

chess_moves = [["WhitePawnAt(E2)", "WhitePawnAt(E3)"], ["WhitePawnAt(E3)", "WhitePawnAt(E4)"],
               ["BlackPawnAt(E7)", "BlackPawnAt(E6)"],
               ["BlackPawnAt(E6)", "BlackPawnAt(E5)"], ["WhitePawnAt(F2)", "WhitePawnAt(F3)"],
               ["WhitePawnAt(F3)", "WhitePawnAt(F4)"],
               ["BlackPawnAt(E5)", "BlackPawnAt(F4)", "WhitePawnAt(F4)"], ["WhiteBishopAt(F1)", "WhiteBishopAt(E2)"],
               ["WhiteBishopAt(E2)", "WhiteBishopAt(C4)"],
               ["BlackQueenAt(D8)", "BlackQueenAt(E7)"], ["BlackQueenAt(E7)", "BlackQueenAt(F6)"],
               ["BlackQueenAt(F6)", "BlackQueenAt(G5)"],
               ["BlackQueenAt(G5)", "BlackQueenAt(H4)"], ["WhiteKingAt(E1)", "WhiteKingAt(F1)"],
               ["BlackPawnAt(B7)", "BlackPawnAt(B6)"],
               ["BlackPawnAt(B6)", "BlackPawnAt(B5)"], ["WhiteBishopAt(C4)", "WhiteBishopAt(B5)", "BlackPawnAt(B5)"],
               ["BlackKnightAt(G8)", "BlackKnightAt(G7)"],
               ["BlackKnightAt(G7)", "BlackKnightAt(G6)"], ["BlackKnightAt(G6)", "BlackKnightAt(F6)"],
               ["WhiteKnightAt(G1)", "WhiteKnightAt(G2)"],
               ["WhiteKnightAt(G2)", "WhiteKnightAt(G3)"], ["WhiteKnightAt(G3)", "WhiteKnightAt(F3)"],
               ["BlackQueenAt(H4)", "BlackQueenAt(H5)"],
               ["BlackQueenAt(H5)", "BlackQueenAt(H6)"], ["WhitePawnAt(D2)", "WhitePawnAt(D3)"],
               ["BlackKnightAt(F6)", "BlackKnightAt(G6)"],
               ["BlackKnightAt(G6)", "BlackKnightAt(H6)"], ["BlackKnightAt(H6)", "BlackKnightAt(H5)"],
               ["WhiteKnightAt(F3)", "WhiteKnightAt(G3)"],
               ["WhiteKnightAt(G3)", "WhiteKnightAt(H3)"], ["WhiteKnightAt(H3)", "WhiteKnightAt(H4)"],
               ["BlackQueenAt(H6)", "BlackQueenAt(G5)"],
               ["WhiteKnightAt(H4)", "WhiteKnightAt(G4)"], ["WhiteKnightAt(G4)", "WhiteKnightAt(F4)"],
               ["WhiteKnightAt(F4)", "WhiteKnightAt(F5)"],
               ["BlackPawnAt(C7)", "BlackPawnAt(C6)"], ["WhitePawnAt(G2)", "WhitePawnAt(G3)"],
               ["WhitePawnAt(G3)", "WhitePawnAt(G4)"],
               ["BlackKnightAt(H5)", "BlackKnightAt(H6)"], ["BlackKnightAt(H6)", "BlackKnightAt(G6)"],
               ["BlackKnightAt(G6)", "BlackKnightAt(F6)"],
               ["WhiteRookAt(H1)", "WhiteRookAt(G1)"], ["BlackPawnAt(C6)", "BlackPawnAt(B5)", "WhiteBishopAt(B5)"],
               ["WhitePawnAt(H2)", "WhitePawnAt(H3)"],
               ["WhitePawnAt(H3)", "WhitePawnAt(H4)"], ["BlackQueenAt(G5)", "BlackQueenAt(G6)"],
               ["WhitePawnAt(H4)", "WhitePawnAt(H5)"], ["BlackQueenAt(G6)", "BlackQueenAt(G5)"],
               ["WhiteQueenAt(D1)", "WhiteQueenAt(E2)"], ["WhiteQueenAt(E2)", "WhiteQueenAt(F3)"],
               ["BlackKnightAt(F6)", "BlackKnightAt(F7)"],
               ["BlackKnightAt(F7)", "BlackKnightAt(F8)"], ["BlackKnightAt(F8)", "BlackKnightAt(G8)"],
               ["WhiteBishopAt(C1)", "WhiteBishopAt(D2)"],
               ["WhiteBishopAt(D2)", "WhiteBishopAt(E3)"],
               ["WhiteBishopAt(E3)", "WhiteBishopAt(F4)", "BlackPawnAt(F4)"], ["BlackQueenAt(G5)", "BlackQueenAt(F6)"],
               ["WhiteKnightAt(B1)", "WhiteKnightAt(B2)"], ["WhiteKnightAt(B2)", "WhiteKnightAt(B3)"],
               ["WhiteKnightAt(B3)", "WhiteKnightAt(C3)"],
               ["BlackBishopAt(F8)", "BlackBishopAt(E7)"], ["BlackBishopAt(E7)", "BlackBishopAt(D6)"],
               ["BlackBishopAt(D6)", "BlackBishopAt(C5)"],
               ["WhiteKnightAt(C3)", "WhiteKnightAt(C4)"], ["WhiteKnightAt(C4)", "WhiteKnightAt(C5)"],
               ["WhiteKnightAt(C5)", "WhiteKnightAt(D5)"],
               ["BlackQueenAt(F6)", "BlackQueenAt(E5)"], ["BlackQueenAt(E5)", "BlackQueenAt(D4)"],
               ["BlackQueenAt(D4)", "BlackQueenAt(C3)"],
               ["BlackQueenAt(C3)", "BlackQueenAt(B2)", "WhitePawnAt(B2)"], ["WhiteBishopAt(F4)", "WhiteBishopAt(E5)"],
               ["WhiteBishopAt(E5)", "WhiteBishopAt(D6)"],
               ["BlackBishopAt(C5)", "BlackBishopAt(D4)"], ["BlackBishopAt(D4)", "BlackBishopAt(E3)"],
               ["BlackBishopAt(E3)", "BlackBishopAt(F2)"],
               ["BlackBishopAt(F2)", "BlackBishopAt(G1)", "WhiteRookAt(G1)"], ["WhitePawnAt(E4)", "WhitePawnAt(E5)"],
               ["BlackQueenAt(B2)", "BlackQueenAt(A1)", "WhiteRookAt(A1)"], ["WhiteKingAt(F1)", "WhiteKingAt(E2)"],
               ["BlackKnightAt(B8)", "BlackKnightAt(A8)"],
               ["BlackKnightAt(A8)", "BlackKnightAt(A7)"], ["BlackKnightAt(A7)", "BlackKnightAt(A6)"],
               ["WhiteKnightAt(F5)", "WhiteKnightAt(G5)"],
               ["WhiteKnightAt(G5)", "WhiteKnightAt(G6)"], ["WhiteKnightAt(G6)", "WhiteKnightAt(G7)"],
               ["BlackKingAt(E8)", "BlackKingAt(D8)"],
               ["WhiteQueenAt(F3)", "WhiteQueenAt(F4)"], ["WhiteQueenAt(F4)", "WhiteQueenAt(F5)"],
               ["WhiteQueenAt(F5)", "WhiteQueenAt(F6)"],
               ["BlackKnightAt(G8)", "BlackKnightAt(F8)"], ["BlackKnightAt(F8)", "BlackKnightAt(F7)"],
               ["BlackKnightAt(F7)", "BlackKnightAt(F6)", "WhiteQueenAt(F6)"],
               ["WhiteBishopAt(D6)", "WhiteBishopAt(E7)"]]

closing_frames = ['<10,5,0>', '<9,6,-1>', '<8,7,-2>', '<7,8,-3>', '<6,9,-4>', '<5,10,-5>','<4,11,-6>', '<3,12,-7>','<2,13,-8>',
                   '<1,14,-9>', '<0,15,-10>', '<-1,16,-11>', '<-2,17,-12>', '<-3,18,-13>', '<-4,19,-14>', '<-5,20,-15>']


def pad_with_zeros(count):
    if count < 10:
        return "00" + str(count)
    if count < 100:
        return "0" + str(count)
    return "" + str(count)

#OPENING FRAMES
with open(pov_file, "r") as pov:
    read_in_pov = pov.read()

for i in range(len(opening_frames)):
    with open(base_name + pad_with_zeros(i) + ".txt", 'w') as curr_frame:
        if i == 0:
            read_in_pov = read_in_pov.replace("location" + opening_frames[0], "location" + opening_frames[0])
        else:
            read_in_pov = read_in_pov.replace("location" + opening_frames[i - 1], "location" + opening_frames[i])
        curr_frame.write(read_in_pov)
        frame_number += 1

#CHESS GAME FRAMES


for move in chess_moves:
    with open(base_name + pad_with_zeros(frame_number) + ".txt", 'w') as curr_frame:
        read_in_pov = read_in_pov.replace(move[0], move[1])
        if len(move) == 3:
           read_in_pov = read_in_pov.replace(move[2], "        ")
        curr_frame.write(read_in_pov)
        frame_number +=1

#CLOSING GAME FRAMES

for i in range(len(closing_frames)):
    with open(base_name + pad_with_zeros(i) + ".txt", 'w') as curr_frame:
        if i == 0:
            read_in_pov = read_in_pov.replace("location" + closing_frames[0], "location" + closing_frames[0])
        else:
            read_in_pov = read_in_pov.replace("location" + closing_frames[i - 1], "location" + closing_frames[i])
        curr_frame.write(read_in_pov)
        frame_number += 1

makeflow_file = "/home/u14/akoutia/homework/hw10/chess.makeflow"

frame_number = 0

#Arg[0] = number of seconds of movie  #Arg[1] = input file   #Arg[2] = output file
commandlineArgs = sys.argv[1:]

#Generate opening frames in makeflow file

for i in range (20):
    with open(makeflow_file, "a") as mf:
        mf.write(pad_with_zeros(frame_number) + ".png: Swoop.py ChessGame.txt")
        mf.write("\n\tpython Swoop.py " + str(pad_with_zeros(frame_number)) +".txt " + str(pad_with_zeros(frame_number)) + "\n")
        frame_number += 1

#Generate chess move frames in makeflow file
for i in range(100):
    with open(makeflow_file, "a") as mf:
        mf.write(pad_with_zeros(frame_number) + ".png: ChessMoves.py ChessGame.txt")
        mf.write("\n\tChessMoves.py " + str(pad_with_zeros(frame_number)) +".txt"+ str(pad_with_zeros(frame_number)) +"\n")
        frame_number += 1

#Generate closing frames in makeflow file

for i in range (20):
    with open(makeflow_file, "a") as mf:
        mf.write(pad_with_zeros(frame_number) + ".png: Swoop.py ChessGame.txt")
        mf.write("\n\tpython Swoop.py " + str(pad_with_zeros(frame_number)) + ".txt" + str(pad_with_zeros(frame_number)) +"\n")
        frame_number += 1

#Generate movie in makeflow file
fps = int(round((frame_number + 1) / int(commandlineArgs[0])))

with open(makeflow_file, "a") as mf:
    mf.write(commandlineArgs[2] +": Frames")
    mf.write("\n\tpython Movie.py " + str(fps) + " " + commandlineArgs[2] +"\n")


#Start Makeflow
os.system("export PATH=$HOME/cctools/bin:$PATH")
os.system("makeflow -T wq chess.makeflow -p 9123")

