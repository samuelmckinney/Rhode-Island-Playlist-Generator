import requests
import json
from urllib2 import urlopen

city = urlopen(http://api.songkick.com/api/3.0/search/locations.json?query=Providence&apikey={4ijYWoKGnZfk7eoY})
response = city.read()
print response