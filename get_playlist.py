import ch_character_converter, spotipy, os
import mutagen as mutFile
from spotipy.oauth2 import SpotifyClientCredentials

# get a playlist from spotify using Spotify Web API
def get_spotify_playlist(username, password):
    # Set up client credentials manager
    client_credentials_manager = SpotifyClientCredentials(client_id=username, client_secret=password)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Get playlist ID (you can find this in the URL of the playlist)
    playlist_id = 'PLAYLIST_ID'

    # Retrieve playlist tracks
    results = sp.playlist_tracks(playlist_id)

    # Print track names
    for track in results['items']:
        print(track['track']['name'])

def is_music_file(filename):
    musicExt = {'.mp3', '.flac', '.wav', '.aac', '.ogg', '.m4a'}
    return any(filename.lower().endswith(ext) for ext in musicExt)
def get_metadata(file_path):
    try:
        audio = mutFile(file_path, easy=True)
        if audio:
            title = audio.get('title', ['Unknown Title'])[0]
            artist = audio.get('artist', ['Unknown Artist'])[0]
            return title, artist
        return "Unknown Title", "Unknown Artist"
    except Exception as e:
        print(f"Error reading metadata for {file_path}: {e}")
        return "Unknown Title", "Unknown Artist"

def get_local_playlist(folderPath):
    # get a list of files in all of the folder in the folderpath
    music_files = []
    missing_metadata = []

    # Walk through the directory
    for root, _, files in os.walk(folderPath):
        for f in files:
            if is_music_file(f): # filter out none music files
                full_path = os.path.join(root, f)
                music_files.append(full_path)

    # for loop over filtered list
        # get name and artist 

    for fPath in music_files:
        title, artist = get_metadata(fPath)
        print(f"File: {fPath}\nTitle: {title}\nArtist: {artist}\n")
        if title == "Unknown Title" or artist == "Unknown Artist":
            missing_metadata.append(fPath)


# compare spotify playlist to a given list of songs based on artist and title
def compare_playlist():
    # when comparing songs with chinese characters, make sure to translate everything to simplified characters for both playlist
    pass

    # if song not in given playlist, record it
    def record_song():
        pass

# export recorded list of missing songs
def export_list(missing_list, flag):
    if flag == "miss":
        with open("missing_playlist.txt", 'a', encoding='utf-16') as curFi:
            for i in missing_list:
                curFi.write(i)

    if flag == "metadata":
        with open("missing_metadata_playlist.txt", 'a', encoding='utf-16') as curFi:
            for i in missing_list:
                curFi.write(i)
    
    # using a single class might be easier/more benefical 