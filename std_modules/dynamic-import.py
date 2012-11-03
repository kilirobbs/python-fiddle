# http://stackoverflow.com/questions/301134/dynamic-module-import-in-python

moduleNames = ['sys', 'os', 're', 'unittest']
modules = map(__import__, moduleNames)