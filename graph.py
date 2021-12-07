# from collections import defaultdict
# from spotifyAPI import *
# from queue import Queue
# import time
# import sys
# class Artist:
#     name = ""
#     ID = ""
#     def __init__(self, _name, _ID):
#         self.name = _name
#         self.ID = _ID

# class Song:
#     name = ""
#     ID = ""
#     def __init__(self, _name, _ID):
#         self.name = _name
#         self.ID = _ID

# class Graph:
#     skipTimeLimit = 0.0000000001
#     adj = defaultdict(list)
#     artistSet = set()
#     q = Queue()
#     def insert(self, song1, song2, artist):
#         self.adj[song1.ID].append((song2, artist))
#         self.adj[song2.ID].append((song1, artist))
#     def findCurrentSong(self, ID):
#         for vertex in self.adj[ID]:
#             print("Name of Song: " + vertex[0].name)
#     def printAllSongs(self):
#         for list_ in self.adj:
#             for vertex in self.adj[list_]:
#                 currSongName = self.getCurrSong(list_)
#                 print(currSongName + " and " + vertex[0].name + " are both made by " + vertex[1].name)
#     def getCurrSong(self, ID_):
#         for list_ in self.adj:
#             for vertex in self.adj[list_]:
#                 if (vertex[0].ID == ID_):
#                     return vertex[0].name

#     def createGraph(self, song1_name, artist1_name, song2_name, artist2_name):
#         song1 = get_song(song1_name, artist1_name)
#         print("Adding " + song1.name + " and all related songs to graph")
#         self.q.put(song1)
#         self.insert_related_songs()
#         before = time.localtime().tm_min
#         while not self.q.empty():
#             self.insert_related_songs()
#             after = time.localtime().tm_min
#             if after - before > self.skipTimeLimit:
#                 print("Broke because graph creation took more than " + str(self.skipTimeLimit) + " minutes")
#                 break
#         song2 = get_song(song2_name, artist2_name) #get_song(song2_name, artist2_name)
#         print("Adding " + song2.name + " and all related songs to graph")
#         self.q = Queue()
#         self.artistSet = set() #this possibly messes up the entire algorith,
#         self.q.put(song2)
#         before = time.localtime().tm_min
#         self.insert_related_songs()
#         after = time.localtime().tm_min
#         while not self.q.empty():
#             if after - before > self.skipTimeLimit:
#                 print("Broke because graph creation took more than " + str(self.skipTimeLimit) + " minutes")
#                 break
#             self.insert_related_songs()
#             after = time.localtime().tm_min
#         self.dijkstras(song1, song2)
    
#     def insert_related_songs(self):
#         soloSong = True
#         song_ = self.q.get()
#         Artists = get_artists_from_song(song_.name, song_.ID)
#         for artist in Artists:
#             if artist.name in self.artistSet:
#                 continue
#             self.artistSet.add(artist.name)
#             # print("   -adding " + artist.name + "'s songs to the graph")
#             skipIt = False
#             try:
#                 Songs = get_filtered_albums_and_songs(artist.name)
#             except:
#                 print("An error occured. Skipping " + artist.name)
#                 continue
#             if len(Songs) == 1:
#                 print("discarding " + artist.name)
#                 self.artistSet.discard(artist.name)
#             print("Number of collabs by " + artist.name + " is " + str(len(Songs)))
#             for song in Songs:
#                 if(song.name == song_):
#                     continue
#                 if len(self.adj[song.ID]) == 0:
#                     self.q.put(song)
#                 # print("      -inserting " + song.name + " to the graph")
#                 self.adj[song.ID].append((song_, artist))
#                 self.adj[song_.ID].append((song, artist))

#     def dijkstras(self, song1object, song2object):
#         print("finding connection between " + song1object.name + " and " + song2object.name)
#         print("song2 ID = " + song2object.ID)
#         song1 = song1object.ID
#         song2 = song2object.ID
#         p = dict()
#         d = dict()
#         s = set()
#         s.add(song1)
#         vs = set()
#         for ID in self.adj:
#             if ID == song1:
#                 continue
#             for element in self.adj[ID]:
#                 vs.add(element[0].ID)

#         for v in vs:
#             p[v] = song1
#             #if edge from song1 to v
#             #set d[v] to w(s, v)
#             for edge in self.adj[song1]:
#                 if edge[0].ID == v:
#                     d[v] = 1
#                 else:
#                     d[v] = sys.maxsize
#         while len(vs) > 0:
#             min = sys.maxsize + 1
#             currU = -1
#             for u in vs:
#                 if d[u] <= min:
#                     currU = u
#                     min = d[u]
#             vs.remove(currU)
#             s.add(currU)
#             #for all v adjacent to u in vs
#                 #for all v in vs
#                     #if v is adjacent to u
#             for v in vs:
#                 for connection in self.adj[v]:
#                     if connection[0].ID == currU:
#                         if (d[currU] + 1) < d[v]:
#                             d[v] = d[currU] + 1
#                             p[v] = currU

#         prev = song2 
#         # print("prev = " + str(prev))
#         print("Song " + str(self.getCurrSong(song2)))
#         while prev != song1:
#             oldSong = prev
#             artistConnection = ""
#             prev = p[prev]
#             # for vertex in self.adj[prev]:
#             #     currSongName = self.getCurrSong(vertex)
#                 # print(currSongName)
#                 # print(" and ")
#                 # print(vertex[0].name)
#                 # print(" are both made by ")
#                 # print(vertex[1].name)
#             # print("testing: prev = " + str(prev) + " p[prev] = " + str(p[prev]))
#             print(str(self.getCurrSong(oldSong)) + " is connected to " + str(self.getCurrSong(prev)))
#         print("to " + str(self.getCurrSong(prev)))
            


# #tracks = get_filtered_albums_and_songs("J Cole")
# #for song in tracks:
#     #print(song.name + " has ID " + song.ID)
# #print(str(len(tracks)) + " number of songs by artist")

# #swf = 5fBoh0hqi7shM8a8nfPnDB
# #artists = get_artists_from_song('Sparks Will Fly', "5fBoh0hqi7shM8a8nfPnDB")
# #for a in artists:
#     #print(a.name + " has ID " + a.ID)
# #song1 = get_song('Sparks Will Fly', "J Cole")
# #print(song1.name + " has ID " + song1.ID)
# G = Graph()
# before = time.localtime().tm_min
# G.createGraph('A Milli', 'Lil Wayne', 'Like a Bird', "WILLOW")
# # song1 = Song("S1", "1")
# # song2 = Song("S2", "2")
# # artist1 = Artist("A1", "1")
# # song3 = Song("S3", "3")
# # song4 = Song("S4", "4")
# # artist2 = Artist("A2", "2")
# # artist3 = Artist("A3", "3")
# # G.adj[song1.ID].append((song2, artist1))
# # G.adj[song1.ID].append((song4, artist3))
# # G.adj[song2.ID].append((song1, artist1))
# # G.adj[song4.ID].append((song1, artist3))
# # G.dijkstras(song2, song4)


# # after = time.localtime().tm_min
# # print("Took " + str(after - before) + " minutes to create")
# # G.printAllSongs()




#HEREEEEEEEEEEEEEEE


from collections import defaultdict
from spotifyAPI import *
from queue import Queue
import time
import sys
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
            if after - before > self.skipTimeLimit:
                print("Broke because graph creation took more than " + str(self.skipTimeLimit) + " minutes")
                break
        song2 = get_song(song2_name, artist2_name) #get_song(song2_name, artist2_name)
        print("Adding " + song2.name + " and all related songs to graph")
        self.q = Queue()
        # self.artistSet = set() #this possibly messes up the entire algorith,
        self.q.put(song2)
        before = time.localtime().tm_min
        self.insert_related_songs()
        after = time.localtime().tm_min
        while not self.q.empty():
            if after - before > self.skipTimeLimit:
                print("Broke because graph creation took more than " + str(self.skipTimeLimit) + " minutes")
                break
            self.insert_related_songs()
            after = time.localtime().tm_min
        self.dijkstras(song1, song2)
    
    def insert_related_songs(self):
        soloSong = True
        song_ = self.q.get()
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
                print("discarding " + artist.name)
                self.artistSet.discard(artist.name)
            print("Number of collabs by " + artist.name + " is " + str(len(Songs)))
            for song in Songs:
                if(song.name == song_):
                    continue
                if len(self.adj[song.ID]) == 0:
                    self.q.put(song)
                # print("      -inserting " + song.name + " to the graph")
                self.adj[song.ID].append((song_, artist))
                self.adj[song_.ID].append((song, artist))

    def dijkstras(self, song1object, song2object):
        for vertex in self.adj[song1object.ID]:
            if (vertex[0].ID == song2object.ID):
                currSongName = self.getCurrSong(song1object.ID)
                print(currSongName + " and " + vertex[0].name + " are both made by " + vertex[1].name)




        print("finding connection between " + song1object.name + " and " + song2object.name)
        print("song2 ID = " + song2object.ID)
        print("song1 ID = " + song1object.ID)
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

        for v in vs:
            p[v] = song1
            #if edge from song1 to v
            #set d[v] to w(s, v)
            for edge in self.adj[song1]:
                if edge[0].ID == v:
                    d[v] = 1
                else:
                    d[v] = sys.maxsize
        while len(vs) > 0:
            min = sys.maxsize + 1
            currU = -1
            for u in vs:
                if d[u] <= min:
                    currU = u
                    min = d[u]
            vs.remove(currU)
            s.add(currU)
            #for all v adjacent to u in vs
                #for all v in vs
                    #if v is adjacent to u
            for v in vs:
                for connection in self.adj[v]:
                    if connection[0].ID == currU:
                        if (d[currU] + 1) < d[v]:
                            d[v] = d[currU] + 1
                            p[v] = currU
        prev = song2 
        print("Song " + str(self.getCurrSong(song2)))
        while prev != song1:
            oldSong = prev
            artistConnection = ""
            print("prev = " + str(prev))
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
        print("to " + str(self.getCurrSong(prev)))
            


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
# before = time.localtime().tm_min
G.createGraph('A Milli', 'Lil Wayne', 'Like A Bird', "Willow")
# G.createGraph('A Milli', 'Lil Wayne', 'Shape of My Heart', "Sting")
# song1 = Song("S1", "1")
# song2 = Song("S2", "2")
# artist1 = Artist("A1", "1")
# song3 = Song("S3", "3")
# song4 = Song("S4", "4")
# artist2 = Artist("A2", "2")
# artist3 = Artist("A3", "3")
# G.adj[song1.ID].append((song2, artist1))
# G.adj[song1.ID].append((song4, artist3))
# G.adj[song2.ID].append((song1, artist1))
# G.adj[song4.ID].append((song1, artist3))
# G.dijkstras(song2, song4)


# after = time.localtime().tm_min
# print("Took " + str(after - before) + " minutes to create")
# G.printAllSongs()