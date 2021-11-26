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

titleLabel = Label(root, text = "Spotify Song Linker", bg = '#E48214', font=("Helvetica", 25)).place(relx = .3, rely = .2)






#Creating button ONE
songOneVar = StringVar(root) #Song option variable


def songChoice():
    #Change to get input and pass to graph
    print("THIS IS THE SONG CHOICE: " + songOneVar.get())

label1 = Label(root, text = "Song choice 1", bg = '#E48214', command = songChoice()).pack(side = LEFT, pady = 100)
choices = {'a', 'b', 'c'} #Song options
chooseSong1 = tk.OptionMenu(root, songOneVar, *choices)
chooseSong1.config(font = ('Helvetica', 12), fg = 'orange')
chooseSong1.place(x = 35, y = 150)





#Creating button TWO
songTwoVar = StringVar(root) #Song option variable
label2 = Label(root, text = "Song choice 2", bg = '#E48214', command = songChoice()).pack(side = RIGHT, pady = 100)
#choices = {'a', 'b', 'c'} #Song options #Same choices as above
chooseSong2 = OptionMenu(root, songTwoVar, *choices,)
chooseSong2.config(font = ('Helvetica', 12), fg = 'orange')
chooseSong2.place(x = 540, y = 150)


def chooseAlgorithm():
    choice = algorVar.get()
    if choice == 1:
        print("1")
        #Prims
    elif choice == 2:
        print("2")
        #Kruskals



algorVar = IntVar()
algorLabel = Label(root, text = "Choose which algorithm to search with: ", bg = '#E48214', command = songChoice()).pack(side = BOTTOM, padx = 50, pady = 160)
Radiobutton(root, text = "Prim's", variable = algorVar, value = 1, bg = '#E48214', command = chooseAlgorithm()).place(relx = .55, rely = .6)
Radiobutton(root, text = "Kruskal's", variable = algorVar, value = 2, bg = '#E48214', command = chooseAlgorithm()).place(relx = .315, rely = .6)


textBox = Text(root, height = 7, width = 60)
textBox.place(relx = 0.16, rely = 0.72)

result = "Results from program go here"
textBox.insert(tk.END, result)




root.mainloop()