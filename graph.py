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

    def createGraph(self, song1_name, artist1_name, song2_name, artist2_name):
        song1 = Song("placeHolder", "placeHOlder") #get_song(song1_name, artist1_name)
        q.put(song1.ID)
        insert_related_songs(self)
        while not q.empty():
            insert_related_songs(self)
        song2 = Song("placeholder", "placeholder2") #get_song(song2_name, artist2_name)
        q.put(song2.ID)
        while not q.empty():
            insert_related_songs(self)
    def insert_related_songs(self):
        song_ = q.get()
        Artists = [] #get_artists_related(song_)
        for artist in Artists:
            if artist.name in artistsSet:
                continue
            artistSet.add(artist)
            Songs = [] #get_filtered_songs(artist.name)
            if len(Songs) == 1:
                artistSet.discard(artist.name)
            for song in Songs:
                if(song.name == song_):
                    continue
                if len(self.adj[song.ID]) == 0:
                    q.put(song.ID)
                self.adj[song.ID].append(song_, artist)
                self.adj[song_.ID].append(song, artist)
   
G = Graph()
S1 = Song("M2", "wierhisugfu8wi3r-0")
S2 = Song("M5", "w435etghdhwi3r-0")
S3 = Song("M3", "siouf08dgffdsi9gi9dg")
A1 = Artist("JCole", "w87d98f7s98dfd")
G.insert(S1, S2, A1)
G.insert(S1, S3, A1)
G.findCurrentSong("wierhisugfu8wi3r-0")

tracks = get_filtered_albums_and_songs("J Cole")
print(str(len(tracks)) + " number of songs by artist")

