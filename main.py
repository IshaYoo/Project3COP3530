import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text, messagebox
import os
#E48214 is the color gator orange


#Creating main root of the GUI
root = tk.Tk()
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
    choice = algorVar.get()
    #Make graph
    #Check if new songs have been inserted, make new graph if needed
    if choice == 1:
        print("1")
        #Prims
    elif choice == 2:
        print("2")
        #Kruskals



algorVar = IntVar()
algorLabel = Label(root, text = "Choose which algorithm to search with: ", bg = '#E48214', command = chooseAlgorithm()).pack(side = BOTTOM, padx = 50, pady = 160)
Radiobutton(root, text = "Prim's", variable = algorVar, value = 1, bg = '#E48214', command = chooseAlgorithm()).place(relx = .55, rely = .6)
Radiobutton(root, text = "Kruskal's", variable = algorVar, value = 2, bg = '#E48214', command = chooseAlgorithm()).place(relx = .315, rely = .6)


textBox = Text(root, height = 7, width = 60)
textBox.place(relx = 0.16, rely = 0.72)

result = "Results from program go here"
textBox.insert(tk.END, result)




root.mainloop()
