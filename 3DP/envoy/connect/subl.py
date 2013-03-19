#!/usr/bin/env python
from os import popen
from envoy import connect, run

bin="/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"
d="/Users/nordmenss/git/GISTS/4039460"
#connect(bin.replace(" ","\\ "))
#connect(bin.replace(" ","\\ ")+" -n "+d)
#run(bin.replace(" ","\\ ")," -n "+d)
#popen("/Applications/Sublime\\ Text\\ 2.app/Contents/SharedSupport/bin/subl -n /Users/nordmenss/git/GISTS/4039460")


print connect("say hi")