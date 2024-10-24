import urllib.request
import json

url = 'https://animechan.io/api/v1/quotes/random'

print('Retrieving', url)

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    uh = urllib.request.urlopen(req)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    data_dict = json.loads(data)
    character_name = data_dict['data']['character']['name']
    print(f"This is a character name in a anime: {character_name}")
    
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
