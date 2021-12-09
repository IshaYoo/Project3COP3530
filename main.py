import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text, messagebox
from graph import *
#1DB954 is the Spotify green color



G = Graph()

def runProgram():
    #Make graph
    #Check if new songs have been inserted, make new graph if needed

    song1 = chooseSong1.get(1.0, "end-1c")
    artist1 = chooseArtist1.get(1.0, "end-1c")
    song2 = chooseSong2.get(1.0, "end-1c")
    artist2 = chooseArtist2.get(1.0, "end-1c")

    G.createGraph(song1, artist1, song2, artist2)

    textBoxDij.config(text = "Took " + str(G.dij_time) + " seconds" + G.dijSTR)
    textBoxBFS.config(text = "Took " + str(G.bfs_time) + " seconds \n" + G.bfsSTR)


#Creating main root of the GUI
root = tk.Tk()
root.title("Spotify Song Linker")
root.geometry("650x700")
root.configure(bg = '#1DB954') #Setting background color
titleLabel = Label(root, text = "Spotify Song Linker", bg = '#1DB954', font=("Helvetica", 25)).place(x = 200, y = 30)

###########################################################################

#Creating button ONE
#songOneVar = string(root) #Song option variable
song1Label = Label(root, text = "Song choice 1", bg = '#1DB954').place(x = 20, y = 80)
chooseSong1 = tk.Text(root, height = 2, width = 20)
chooseSong1.config(font = ('Helvetica', 12))
chooseSong1.place(x = 20, y = 100)

#Artist ONE
artistOneVar = str(root) #Artist option variable
artist1Label = Label(root, text = "Artist choice 1", bg = '#1DB954').place(x = 20, y = 150)
chooseArtist1 = tk.Text(root, height = 2, width = 20)
chooseArtist1.config(font = ('Helvetica', 12))
chooseArtist1.place(x = 20, y = 170)

###########################################################################


#Creating button TWO
songTwoVar = str(root) #Song option variable
song2Label = Label(root, text = "Song choice 2", bg = '#1DB954').place(x = 460, y = 80)
chooseSong2 = tk.Text(root, height = 2, width = 20)
chooseSong2.config(font = ('Helvetica', 12))
chooseSong2.place(x = 460, y = 100)
#Artist TWO
artistTwoVar = str(root) #Artist option variable
artist2Label = Label(root, text = "Artist choice 2", bg = '#1DB954').place(x = 460, y = 150)
chooseArtist2 = tk.Text(root, height = 2, width = 20)
chooseArtist2.config(font = ('Helvetica', 12))
chooseArtist2.place(x = 460, y = 170)


###########################################################################



labelDij = Label(root, text = "Results from Dijkstra’s Algorithm", bg = '#1DB954').place(x = 45, y = 300)
textBoxDij = Label(root, height = 20, width = 25)
textBoxDij.place(relx = 0.06, rely = 0.5)



mkGraph = tk.Button(root, text = "Make and Traverse", command = runProgram).place(x = 240, y = 250)


labelBFS = Label(root, text = "Results from Breadth First Search", bg = '#1DB954').place(x = 370, y = 300)
textBoxBFS = Label(root, height = 20, width = 25)
textBoxBFS.place(relx = 0.56, rely = 0.5)



root.mainloop()



