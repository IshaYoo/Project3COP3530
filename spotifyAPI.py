import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
class Artist:
    name = ""
    ID = ""

class Song:
    name = ""
    ID = ""


#First make a spotify devloper account and create an app
#Use that information to update SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
SPOTIPY_CLIENT_ID='78b872793308473895468b5886bfbaa3'
SPOTIPY_CLIENT_SECRET='e4448212cba449439cc4b73be9809e8b'
SPOTIPY_REDIRECT_URI='http://127.0.0.1:9090'
SCOPE = 'user-top-read'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

#returns an array of all songs from artist that are NOT solo songs
#...returns an array of song objects
def get_filtered_albums_and_songs(artist_name):
    artistID = sp.search("artist:" + artist_name, limit=1, offset=0, type='artist', market="ES")['artists']['items'][0]['id']
    search = sp.artist_albums(artistID, album_type='album', limit=1)
    albums = []
    tracks = []
    counter = 0
    while search['next']:
        search = sp.next(search)
        for album in search['items']:
            found = False
            for temp_album in albums:
                if (temp_album in album['name'] or album['name'] in temp_album):
                    found = True
                    break
            if (found):
                continue
            albums.append(album['name'])
            #print("Album: " + album['name'])
            temp_track_names = get_filtered_tracks_from_album(album['name'], artist_name)
            for song in temp_track_names:
                #print("   song: " + song)
                songObject = Song()
                songQuery = sp.search("track:" + song, limit=1, offset=0, type='track', market="ES")['tracks']['items']
                if (len(songQuery) > 0):
                    songID = songQuery[0]['id']
                    #songID = sp.search("track:" + song, limit=1, offset=0, type='track', market="ES")['tracks']['id']
                    songNAME = songQuery[0]['name']
                    #print(songNAME + " has ID: " + songID)
                    songObject.name = song
                    songObject.ID = songID
                    tracks.append(songObject)
            counter += 1
    return tracks

#returns an array of all songs in an album that are NOT solo songs
#used in get_filtered_albums_and_songs
def get_filtered_tracks_from_album(album_name, artist_name):
 search = sp.search("album:" + album_name + ", artist:" + artist_name, limit=50, offset=0, type='track', market="ES")
 found = False
 track_ids = []
 counter = 0
 for song in search['tracks']['items']:
    duplicate = False
    for found_tracks in track_ids:
        if(found_tracks == song['name']):
            duplicate = True
            break
        if duplicate:
            break
    if duplicate:
        continue
    if (len(song['artists']) == 1):
        continue
    track_ids.append(song['name'])
    counter+=1
 return track_ids


#Get all artists related to song...returns an array of artist objects
def get_artists_from_song(song_name, song_id):
    artistArr = []
    #track = sp.search("track:" + song_name, limit=50, offset=0, type='track', market="ES")['tracks']['items'][0]['artists']
    tracks = sp.search("track:" + song_name, limit=50, offset=0, type='track', market="ES")['tracks']['items']
    indexer = 0
    track = tracks[indexer]
    #print("checking " + track['id'] + " vs " + song_id)
    while track['id'] != song_id:
        indexer += 1
        track = tracks[indexer]
    track = track['artists']
    for artist in track:
        artistName = artist['name']
        artistID = artist['id']
        #print(artistName + " with ID " + artistID)
        artistObject = Artist()
        artistObject.name = artistName
        artistObject.ID = artistID
        artistArr.append(artistObject)

    return artistArr


#given a song name and artist name. Return the song object
def get_song(song1_name, artist1_name):
    song0 = Song()
    song0.name = song1_name
    songID = sp.search("artist:" + artist1_name + ", track:" + song1_name, limit=1, offset=0, type='track', market="ES")['tracks']['items'][0]['id']
    song0.ID = songID
    return song0


def runTest():
    for songx in get_filtered_albums_and_songs("J. Cole"):
        print(songx.name + " has ID " + songx.ID)
    print("                 ")
    for artists in get_artists_from_song("Forbidden Fruit", "J. Cole"):
        print(artists.name + " has ID " + artists.ID)


#TEST
#runTest()


#############
#ALL code below was for testing
#############


#NOT USED
def get_track_artists(song_name, artist_name):
 search = sp.search("track:" + song_name, limit=50, offset=0, type='track', market="ES")
 found = False
 track_ids = []
 for song in search['tracks']['items']:
    for item in song['artists']:
        if (item['name'] == artist_name):
            #print(item['name'])
            track_ids.append(item['name'])
            found = True
            break
        if found:
            break
    if found:
        break
 return track_ids

#NOT USED
def get_tracks(artist_name):
 search = sp.search("artist:" + artist_name, limit=50, offset=0, type='track', market="ES")
 found = False
 track_ids = []
 counter = 0
 for song in search['tracks']['items']:
    duplicate = False
    for found_tracks in track_ids:
        if(found_tracks == song['name']):
            duplicate = True
            break
        if duplicate:
            break
    if duplicate:
        continue
    track_ids.append(song['name'])
    counter+=1
 return track_ids

#NOT USED
def get_tracks_from_album(album_name):
 search = sp.search("album:" + album_name, limit=50, offset=0, type='track', market="ES")
 found = False
 track_ids = []
 counter = 0
 for song in search['tracks']['items']:
    duplicate = False
    for found_tracks in track_ids:
        if(found_tracks == song['name']):
            duplicate = True
            break
        if duplicate:
            break
    if duplicate:
        continue
    track_ids.append(song['name'])
    counter+=1
 return track_ids

#NOT USED
def get_albums(artist_name):
    artistID = sp.search("artist:" + artist_name, limit=1, offset=0, type='artist', market="ES")['artists']['items'][0]['id']
    #results = sp.artist_albums(birdy_uri, album_type='album')
    search = sp.artist_albums(artistID, album_type='album', limit=1)
    #search = sp.artist_albums(artistID, album_type='album', country=None, limit=20, offset=0)
    #albums = search['items']
    albums = []
    counter = 0
    while search['next']:
        search = sp.next(search)
        for album in search['items']:
            found = False
            for temp_album in albums:
                if (temp_album in album['name'] or album['name'] in temp_album):
                    found = True
                    break
            if (found):
                continue
            albums.append(album['name'])
            counter += 1
    #print(str(counter) + " many albums")
    return albums

#NOT USED
def get_albums_and_songs(artist_name):
    artistID = sp.search("artist:" + artist_name, limit=1, offset=0, type='artist', market="ES")['artists']['items'][0]['id']
    #results = sp.artist_albums(birdy_uri, album_type='album')
    search = sp.artist_albums(artistID, album_type='album', limit=1)
    #search = sp.artist_albums(artistID, album_type='album', country=None, limit=20, offset=0)
    #albums = search['items']
    albums = []
    tracks = []
    counter = 0
    while search['next']:
        search = sp.next(search)
        for album in search['items']:
            found = False
            for temp_album in albums:
                if (temp_album in album['name'] or album['name'] in temp_album):
                    found = True
                    break
            if (found):
                continue
            albums.append(album['name'])
            #print("Album: " + album['name'])
            temp_tracks = get_tracks_from_album(album['name'])
            for song in temp_tracks:
                #print("   song: " + song)
                tracks.append(song)
            counter += 1
    return tracks