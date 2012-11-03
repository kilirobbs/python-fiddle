from appscript import *

iTunes = app(u'/Applications/iTunes.app')
iTunes = app('itunes')
track = iTunes.current_track
print "name=", track.name().encode('utf-8')
print "artist=", track.artist().encode('utf-8')
print "album=", track.album.get().encode('utf-8')
print "rating=", track.rating.get() / 20
