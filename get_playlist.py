import ch_character_converter

# get a playlist from spotify using Spotify Web API
def spotify_playlist():
    pass

# compare spotify playlist to a given list of songs based on artist and title
def compare_playlist():
    # when comparing songs with chinese characters, make sure to translate everything to simplified characters for both playlist
    pass

    # if song not in given playlist, record it
    def record_song():
        pass

# export recorded list of missing songs
def export_list(missing_list):
    with open("missing_playlist.txt", 'a', encoding='utf-16') as curFi:
        for i in missing_list:
            curFi.write(i)
