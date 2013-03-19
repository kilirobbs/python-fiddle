from appscript import app

iTunes = app(u'/Applications/iTunes.app')
iTunes = app('itunes')
for plist in iTunes.user_playlists():
    print plist
    print plist.id()
    #print plist.name() 
    for track in plist.tracks():
        print track.properties()
    break