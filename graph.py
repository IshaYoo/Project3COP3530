from collections import defaultdict
from spotifyAPI import *
from queue import Queue
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
        for row in self.adj:
            for col in row:
                print("s")
                print(col[0].name)


    def createGraph(self, song1_name, artist1_name, song2_name, artist2_name):
        song1 = get_song(song1_name, artist1_name)
        print("Adding " + song1.name + " and all related songs to graph")
        self.q.put(song1)
        self.insert_related_songs()
        while not self.q.empty():
            self.insert_related_songs()
        song2 = get_song(song2_name, artist2_name) #get_song(song2_name, artist2_name)
        print("Adding " + song2.name + " and all related songs to graph")
        self.q.put(song2)
        while not self.q.empty():
            self.insert_related_songs()
    def insert_related_songs(self):
        song_ = self.q.get()
        Artists = get_artists_from_song(song_.name, song_.ID)
        for artist in Artists:
            if artist.name in self.artistSet:
                continue
            self.artistSet.add(artist.name)
            print("   -adding " + artist.name + "'s songs to the graph")
            Songs = get_filtered_albums_and_songs(artist.name)
            if len(Songs) == 1:
                artistSet.discard(artist.name)
            for song in Songs:
                if(song.name == song_):
                    continue
                if len(self.adj[song.ID]) == 0:
                    self.q.put(song)
                self.adj[song.ID].append({song_, artist})
                self.adj[song_.ID].append({song, artist})
   


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
G.createGraph('Sparks Will Fly', "J Cole", 'Be Like Me', 'Lil Pump')
print("created")
G.printAllSongs()