
import spotipy
import sys
import pprint
import spotipy.oauth2 as oauth2

credentials = oauth2.SpotifyClientCredentials( #stores my (Sam's User info)
        client_id='822707b27ef54faca2906a67e683eab2',
        client_secret='a2d641799067491c9aa7898c608846df')

token = credentials.get_access_token() #gets access token, necessary for using Spotify Web API
sp = spotipy.Spotify(auth=token)

if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

#sp = spotipy.Spotify()
response = sp.artist_top_tracks(urn)

for track in response['tracks']:
    print(track['name'], track['id'])

