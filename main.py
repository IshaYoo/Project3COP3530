import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text, messagebox
from graph import *
#E48214 is the color gator orange


#Creating main root of the GUI
root = tk.Tk()
G = Graph()


root.title("Spotify Song Linker")
root.geometry("600x400")
root.configure(bg = '#E48214') #Setting background color
titleLabel = Label(root, text = "Spotify Song Linker", bg = '#E48214', font=("Helvetica", 25)).place(x = 200, y = 30)

###########################################################################

#Creating button ONE
songOneVar = StringVar(root) #Song option variable
song1Label = Label(root, text = "Song choice 1", bg = '#E48214').place(x = 20, y = 80)
chooseSong1 = tk.Text(root, height = 2, width = 15)
chooseSong1.config(font = ('Helvetica', 12), fg = 'orange')
chooseSong1.place(x = 20, y = 100)
#Artist ONE
artistOneVar = StringVar(root) #Artist option variable
artist1Label = Label(root, text = "Artist choice 1", bg = '#E48214').place(x = 20, y = 150)
chooseArtist1 = tk.Text(root, height = 2, width = 15)
chooseArtist1.config(font = ('Helvetica', 12), fg = 'orange')
chooseArtist1.place(x = 20, y = 170)




#Creating button TWO
songTwoVar = StringVar(root) #Song option variable
song2Label = Label(root, text = "Song choice 2", bg = '#E48214').place(x = 460, y = 80)
chooseSong2 = tk.Text(root, height = 2, width = 15)
chooseSong2.config(font = ('Helvetica', 12), fg = 'orange')
chooseSong2.place(x = 460, y = 100)
#Artist ONE
artistTwoVar = StringVar(root) #Artist option variable
artist2Label = Label(root, text = "Artist choice 2", bg = '#E48214').place(x = 460, y = 150)
chooseArtist2 = tk.Text(root, height = 2, width = 15)
chooseArtist2.config(font = ('Helvetica', 12), fg = 'orange')
chooseArtist2.place(x = 460, y = 170)


def chooseAlgorithm():
    #Make graph
    #Check if new songs have been inserted, make new graph if needed
    print("graph button")


mkGraph = tk.Button(root, text = "Make and Traverse", command = chooseAlgorithm()).place(relx = .4, rely = .53)

labelDij = Label(root, text = "Results from Dijkstra’s Algorithm", bg = '#E48214').place(x = 28, y = 255)
textBoxDij = Text(root, height = 7, width = 30)
textBoxDij.place(relx = 0.05, rely = 0.72)
result = "Results from program go here"
textBoxDij.insert(tk.END, result)

labelBFS = Label(root, text = "Results from Breadth First Search", bg = '#E48214').place(x = 345, y = 255)
textBoxBFS = Text(root, height = 7, width = 30)
textBoxBFS.place(relx = 0.57, rely = 0.72)
result = G.createGraph('A Milli', 'Lil Wayne', 'Be Like Me', "Lil Pump")
textBoxBFS.insert(tk.END, G.artistSet)



root.mainloop()
