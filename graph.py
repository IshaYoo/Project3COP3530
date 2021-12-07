from collections import defaultdict
from spotifyAPI import *
from queue import Queue
import time
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 


class Stack:
 
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0
 
    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]
 
    # Get the current size of the stack
    def getSize(self):
        return self.size
 
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
 
    # Get the top item of the stack
    def peek(self):
 
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
 
    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value



class Artist:
    name = ""
    ID = ""
    def __init__(self, _name, _ID):
        self.name = _name
        self.ID = _ID

class Song:
    name = ""
    ID = ""
    def __init__(self, _name, _ID):
        self.name = _name
        self.ID = _ID

class Graph:
    skipTimeLimit = 0.0000000001
    songLimiter = 50
    adj = defaultdict(list)
    artistSet = set()
    q = Queue()
    songSet = set()
    def insert(self, song1, song2, artist):
        self.adj[song1.ID].append((song2, artist))
        self.adj[song2.ID].append((song1, artist))
    def findCurrentSong(self, ID):
        for vertex in self.adj[ID]:
            print("Name of Song: " + vertex[0].name)
    def printAllSongs(self):
        for list_ in self.adj:
            for vertex in self.adj[list_]:
                currSongName = self.getCurrSong(list_)
                print(currSongName + " and " + vertex[0].name + " are both made by " + vertex[1].name)
    def getCurrSong(self, ID_):
        for list_ in self.adj:
            for vertex in self.adj[list_]:
                if (vertex[0].ID == ID_):
                    return vertex[0].name

    def createGraph(self, song1_name, artist1_name, song2_name, artist2_name):
        song1 = get_song(song1_name, artist1_name)
        print("Adding " + song1.name + " and all related songs to graph")
        self.q = Queue()
        self.q.put(song1)
        self.insert_related_songs()
        index = 0
        while not self.q.empty():
            self.insert_related_songs()
            index += 1
            if (index == self.songLimiter):
                break
        song2 = get_song(song2_name, artist2_name) #get_song(song2_name, artist2_name)
        print("Adding " + song2.name + " and all related songs to graph")
        self.q = Queue()
        # self.artistSet = set() #this possibly messes up the entire algorith,
        self.q.put(song2)
        self.insert_related_songs()
        index = 0
        while not self.q.empty():
            self.insert_related_songs()
            index += 1
            if (index == self.songLimiter):
                break
        
        print("Size of the graph is now +" + str(len(self.adj)) + " songs")
        if (self.dijkstras(song1, song2) == False):
            if (~G.isConnection(song1Name, artist1Name, song2Name, artist2Name)):
                print("No connection made. Try again and maybe we can find a connection.")
            else:
                print("There is a discrepancy in the code for some reason")
    
    def isConnection(self, song1objectName, song1artistName, song2objectName, song2artistname):
        song1object = get_song(song1objectName, song1artistName)
        song2object = get_song(song2objectName, song2artistname)
        stack = Stack()
        visited = set()
        stack.push(song1object.ID)
        visited.add(song1object.ID)
        while (~stack.isEmpty()):
            if (stack.isEmpty()):
                break
            u = stack.pop()
            for adjacentV in self.adj[u]:
                if adjacentV[0].ID in visited:
                    continue
                visited.add(adjacentV[0].ID)
                stack.push(adjacentV[0].ID)
        if (song2object.ID in visited):
            return True
        return False
    
    def insert_related_songs(self):
        soloSong = True
        song_ = self.q.get()
        if song_ in self.songSet:
            return
        print("   adding " + song_.name + "'s related songs to queue")
        self.songSet.add(song_.ID)
        Artists = get_artists_from_song(song_.name, song_.ID)
        for artist in Artists:
            if artist.name in self.artistSet:
                continue
            self.artistSet.add(artist.name)
            # print("   -adding " + artist.name + "'s songs to the graph")
            skipIt = False
            try:
                Songs = get_filtered_albums_and_songs(artist.name)
            except:
                print("An error occured. Skipping " + artist.name)
                continue
            if len(Songs) == 1:
                # print("discarding " + artist.name)
                self.artistSet.discard(artist.name)
            # print("Number of collabs by " + artist.name + " is " + str(len(Songs)))
            for song in Songs:
                if(song.name == song_):
                    continue
                if len(self.adj[song.ID]) == 0:
                    self.q.put(song)
                # print("      -inserting " + song.name + " to the graph")
                self.adj[song.ID].append((song_, artist))
                self.adj[song_.ID].append((song, artist))

    def dijkstras(self, song1object, song2object):
        # print(song2object.name + " is connected to:")
        # for vertex in self.adj[song2object.ID]:
        #     print("   " + vertex[0].name)

        # print(song1object.name + " is connected to:")
        # for vertex in self.adj[song1object.ID]:
        #     print("   " + vertex[0].name)

        # for vertex in self.adj[song1object.ID]:
        #     if (vertex[0].ID == song2object.ID):
        #         currSongName = self.getCurrSong(song1object.ID)
        #         print(currSongName + " and " + vertex[0].name + " are both made by " + vertex[1].name)



        print("finding connection between " + song1object.name + " and " + song2object.name)
        # print("song2 ID = " + song2object.ID)
        # print("song1 ID = " + song1object.ID)
        song1 = song1object.ID
        song2 = song2object.ID
        p = dict()
        d = dict()
        s = set()
        s.add(song1)
        vs = set()
        for ID in self.adj:
            if ID == song1:
                continue
            vs.add(ID)
            # for element in self.adj[ID]:
            #     vs.add(element[0].ID)
        # for v in vs:
        #     print(v + " has not been analyzed")
        # for v_ in s:
        #     print(v_ + " has been analyzed")

        for v_ in vs:
            p[v_] = song1
            #if edge from song1 to v
            #set d[v] to w(s, v)
            for edge in self.adj[song1]:
                if edge[0].ID == v_:
                    d[v_] = 1
                else:
                    d[v_] = sys.maxsize - 1
        while len(vs) > 0:
            min = sys.maxsize + 1
            currU = -1
            for u in vs:
                if d[u] < min:
                    currU = u
                    min = d[u]
            vs.remove(currU)
            s.add(currU)
            #for all v adjacent to u in vs
                #for all v adjacent to u
                    #if u is in vs
            for connection in self.adj[currU]:
                vx = 0
                for temp in vs:
                    cont = False
                    if (temp == connection[0].ID):
                        vx = temp
                        cont = True
                        break
                if (cont):
                    if (d[currU] + 1 < d[temp]):
                        d[temp] = d[currU] + 1
                        p[temp] = currU
            # for v in vs:
            #     for connection in self.adj[v]:
            #         if connection[0].ID == currU:
            #             if (d[currU] + 1) < d[v]:
            #                 d[v] = d[currU] + 1
            #                 p[v] = currU
        prev = song2 
        if (prev == song1):
            return False
        if (p[prev] == song1):
            return False
        # print("Song " + str(self.getCurrSong(song2)))
        while prev != song1:
            oldSong = prev
            artistConnection = ""
            # print("prev = " + str(prev))
            prev = p[prev]
            # for vertex in self.adj[prev]:
            #     currSongName = self.getCurrSong(vertex)
                # print(currSongName)
                # print(" and ")
                # print(vertex[0].name)
                # print(" are both made by ")
                # print(vertex[1].name)
            # print("testing: prev = " + str(prev) + " p[prev] = " + str(p[prev]))
            print(str(self.getCurrSong(oldSong)) + " is connected to " + str(self.getCurrSong(prev)))
        return True
            


#tracks = get_filtered_albums_and_songs("J Cole")
#for song in tracks:
    #print(song.name + " has ID " + song.ID)
#print(str(len(tracks)) + " number of songs by artist")

#swf = 5fBoh0hqi7shM8a8nfPnDB
#artists = get_artists_from_song('Sparks Will Fly', "5fBoh0hqi7shM8a8nfPnDB")
#for a in artists:
    #print(a.name + " has ID " + a.ID)
#song1 = get_song('Sparks Will Fly', "J Cole")
#print(song1.name + " has ID " + song1.ID)
G = Graph()
x = "yes"
while (x != "no"):
    song1Name = input("Enter song 1 name:\n")
    artist1Name = input("Enter song 1's artist:\n")
    song2Name = input("Enter song 2 name:\n")
    artist2Name = input("Enter song 2's artist:\n")
    G.createGraph(song1Name, artist1Name, song2Name, artist2Name)
    x = input("Continue? Enter yes or no\n")
    


# before = time.localtime().tm_min
# G.createGraph('A Milli', 'Lil Wayne', 'Wet Dreamz', "J Cole")
# if (~G.isConnection('A Milli', 'Lil Wayne', 'Wet Dreamz', "J Cole")):
#     print("No connection made")
# G.createGraph('A Milli', 'Lil Wayne', 'Shape of My Heart', "Sting")
# song1 = Song("S1", "1")
# song2 = Song("S2", "2")
# artist1 = Artist("A1", "1")
# song3 = Song("S3", "3")
# song4 = Song("S4", "4")
# song6 = Song("S6", "6")
# artist2 = Artist("A2", "2")
# artist3 = Artist("A3", "3")
# artist4 = Artist("A4", "4")
# G.adj[song1.ID].append((song2, artist1))
# G.adj[song1.ID].append((song4, artist3))
# G.adj[song2.ID].append((song1, artist1))
# G.adj[song4.ID].append((song1, artist3))
# G.adj[song2.ID].append((song3, artist2))
# G.adj[song3.ID].append((song2, artist2))
# G.adj[song3.ID].append((song6, artist4))
# G.adj[song6.ID].append((song3, artist4))

# songX = Song("SX", "X")
# songY = Song("SY", "Y")
# artistX = Artist("AX", "X")
# G.adj[songX.ID].append((songY, artistX))
# G.adj[songY.ID].append((songX, artistX))


# G.dijkstras(song4, songX)


# after = time.localtime().tm_min
# print("Took " + str(after - before) + " minutes to create")
# G.printAllSongs()