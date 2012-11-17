from plistlib import readPlistFromString
import macos
readPlistFromString(macos.shell("defaults read com.apple.iCal"))