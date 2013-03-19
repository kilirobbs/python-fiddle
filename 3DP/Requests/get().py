import requests

r = requests.get('https://github.com/cancerhermit')
print r.status_code # 200
print r.text
print r.json