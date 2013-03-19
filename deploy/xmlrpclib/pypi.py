from xmlrpclib import ServerProxy
server = ServerProxy('http://pypi.python.org/pypi')
print server.package_releases('defaults')
# ['0.0.2']
print server.user_packages('cancerhermit')
# [['Owner', 'earthtools'], ['Owner', 'pgpass'], ['Owner', 'macos'], ['Owner', 'githubatom'], ['Owner', 'gitconfig'], ['Owner', 'gitinfo'], ['Owner', 'github_events'], ['Owner', 'microclimate'], ['Owner', 'githubhook'], ['Owner', 'setuppy'], ['Owner', 'pygithooks'], ['Owner', 'yandexweather'], ['Owner', 'osascript'], ['Owner', 'growlnotify'], ['Owner', 'sublime_helper'], ['Owner', 'vlc'], ['Owner', 'defaults'], ['Owner', 'app']]

