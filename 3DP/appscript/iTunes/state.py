from appscript import app, k

iTunes = app(u'/Applications/iTunes.app')
iTunes = app('itunes')

print iTunes.player_state.get()

print "playing", iTunes.player_state.get() == k.playing
print "paused", iTunes.player_state.get() == k.paused
print "stoped",iTunes.player_state.get()==k.stoped