import spotipy, os
from mutagen import File as mutFile
from spotipy.oauth2 import SpotifyClientCredentials
from ch_character_converter import trad_simp

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

def normalize_song_data(song_list):
    normalized_list = []
    for song in song_list:
        title = trad_simp(song[0])
        artist = trad_simp(song[1])
        normalized_list.append((title, artist))
    return normalized_list

# get a playlist from spotify using Spotify Web API
def get_spotify_playlist(username, password):
    # Set up client credentials manager
    client_credentials_manager = SpotifyClientCredentials(client_id=username, client_secret=password)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Get playlist ID (you can find this in the URL of the playlist)
    playlist_id = 'PLAYLIST_ID'

    # Retrieve playlist tracks
    results = sp.playlist_tracks(playlist_id)

    # Process results
    song_list = []
    for track in results['items']:
        track_data = track['track']
        song_list.append((
            trad_simp(track_data['name']),  # Title
            trad_simp(track_data['artists'][0]['name']),  # Artist
            track_data['external_urls']['spotify']  # URL
        ))
    return song_list

def get_local_playlist(folderPath):
    # get a list of files in all of the folder in the folderpath
    music_files = [] 
    missing_metadata = []
    complete_files = [] #[name][artist]

    # Walk through the directory
    for root, _, files in os.walk(folderPath):
        for f in files:
            if is_music_file(f): # filter out none music files
                full_path = os.path.join(root, f)
                music_files.append(full_path)

    # get name and artist 
    for fPath in music_files:
        title, artist = get_metadata(fPath)
        print(f"File: {fPath}\nTitle: {title}\nArtist: {artist}\n")
        if title == "Unknown Title" or artist == "Unknown Artist":
            missing_metadata.append(fPath)
        else: complete_files.append((title, artist, fPath))

    return complete_files, missing_metadata

# compare spotify playlist to a given list of songs based on artist and title
def compare_playlist(dicPath, username, password):
    # when comparing songs with chinese characters, make sure to translate everything to simplified characters for both playlist
    spotify_list = get_spotify_playlist(username, password)
    local_list, missing_metadata = get_local_playlist(dicPath)
    missing_list = []

    local_list_normalized = normalize_song_data([(song[0], song[1]) for song in local_list])
    
    missing_list = [
        {"title": song[0], "artist": song[1], "url": song[2]}
        for song in spotify_list
        if (song[0], song[1]) not in local_list_normalized
    ]

    export_list(missing_metadata, "metadata")
    export_list(missing_list, "miss")

# export recorded list of missing songs
def export_list(missing_list, flag):
    if flag == "miss":
        with open("missing_playlist.txt", 'a', encoding='utf-16') as curFi:
            for song in missing_list:
                curFi.write(f"{song['title']} - {song['artist']} ({song['url']})\n")

    if flag == "metadata":
        with open("missing_metadata_playlist.txt", 'a', encoding='utf-16') as curFi:
            for i in missing_list:
                curFi.write(f"{i}\n")
    
    # using a single class might be easier/more benefical 