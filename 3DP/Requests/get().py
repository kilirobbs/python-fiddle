import requests

r = requests.get('https://github.com/cancerhermit')
print r.text
print r.json