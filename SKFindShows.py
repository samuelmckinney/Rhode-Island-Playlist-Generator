import requests
import json
from pprint import pprint
#from urllib import urlopen

city = requests.get('http://api.songkick.com/api/3.0/metro_areas/5274/calendar.json?apikey=4ijYWoKGnZfk7eoY')
response  = json.loads(city.text)
events = response['resultsPage']['results']['event'][:50]
tup = {}
for event in events:
    tup[event['performance'][0]['displayName']] = event['popularity']
    #print(str(event['popularity']) + ' ' + event['performance'][0]['displayName'])
print(tup)
