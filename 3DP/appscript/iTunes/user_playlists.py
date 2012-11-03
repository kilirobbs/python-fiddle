from appscript import app

iTunes = app(u'/Applications/iTunes.app')
iTunes = app('itunes')
play_lists = iTunes.user_playlists()
for i, plist in enumerate(play_lists):
    print "%3d:%s" % (i, plist.name().encode('utf-8'))


print iTunes.user_playlists["Chopin"]().play()
