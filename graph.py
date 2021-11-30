from collections import defaultdict
from spotifyAPI import *
from queue import Queue
import time
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
    adj = defaultdict(list)
    artistSet = set()
    q = Queue()
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
        self.q.put(song1)
        self.insert_related_songs()
        before = time.localtime().tm_min
        while not self.q.empty():
            self.insert_related_songs()
            after = time.localtime().tm_min
            if after - before > 5:
                print("Broke because graph creation took more than 5 minutes")
                break
        song2 = get_song(song2_name, artist2_name) #get_song(song2_name, artist2_name)
        print("Adding " + song2.name + " and all related songs to graph")
        self.q.put(song2)
        before = time.localtime().tm_min
        while not self.q.empty():
            self.insert_related_songs()
            after = time.localtime().tm_min
            if after - before > 5:
                print("Broke because graph creation took more than 5 minutes")
                break
    def insert_related_songs(self):
        song_ = self.q.get()
        Artists = get_artists_from_song(song_.name, song_.ID)
        for artist in Artists:
            if artist.name in self.artistSet:
                continue
            if artist.name == "Baby Sleep":
                continue
            self.artistSet.add(artist.name)
            print("   -adding " + artist.name + "'s songs to the graph")
            skipIt = False
            try:
                Songs = get_filtered_albums_and_songs(artist.name)
            except:
                print("An error occured. Skipping " + artist.name)
                continue
            if len(Songs) == 1:
                print("discarding " + artist.name)
                self.artistSet.discard(artist.name)
            for song in Songs:
                if(song.name == song_):
                    continue
                if len(self.adj[song.ID]) == 0:
                    self.q.put(song)
                #print("      -inserting " + song.name + " to the graph")
                self.adj[song.ID].append((song_, artist))
                self.adj[song_.ID].append((song, artist))
   


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
before = time.localtime().tm_min
G.createGraph('Linen', 'The Boas', 'Be Like Me', "Lil Pump")
# song = Song("songOneName", "1345")
# song_ = Song("songTwoName", "44533")
# artist = Artist("guy", "943124")
# G.adj[song.ID].append((song_, artist))
# G.adj[song_.ID].append((song, artist))
# song = Song("songTrheeName", "134534")
# song_ = Song("songFourName", "423454533")
# artist = Artist("guy2", "305943124")
# G.adj[song.ID].append((song_, artist))
# G.adj[song_.ID].append((song, artist))


after = time.localtime().tm_min
print("Took " + str(after - before) + " minutes to create")
G.printAllSongs()