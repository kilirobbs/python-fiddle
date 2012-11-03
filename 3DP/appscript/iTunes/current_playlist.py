from appscript import *

iTunes = app(u'/Applications/iTunes.app')
iTunes = app('itunes')
play_list = iTunes.current_playlist

tracks = play_list.tracks()
for track in tracks:
    print track.name().encode('utf-8')


iTunes.current_playlist.set(iTunes.user_playlists["Chopin"])
