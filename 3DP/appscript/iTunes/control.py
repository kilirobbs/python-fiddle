from appscript import app

iTunes = app(u'/Applications/iTunes.app')
iTunes = app('itunes')

iTunes.pause()
iTunes.stop()
iTunes.play()

iTunes.next_track()
iTunes.previous_track()