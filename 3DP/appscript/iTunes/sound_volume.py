from appscript import *

iTunes = app(u'/Applications/iTunes.app')
iTunes = app('itunes')
print iTunes.sound_volume()
iTunes.sound_volume.set(100)
print iTunes.sound_volume()