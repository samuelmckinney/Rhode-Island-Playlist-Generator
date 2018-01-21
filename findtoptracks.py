import spotipy
import spotipy.oauth2 as oauth2

credentials = oauth2.SpotifyClientCredentials( #stores my (Sam's User info)
        client_id='822707b27ef54faca2906a67e683eab2',
        client_secret='a2d641799067491c9aa7898c608846df')

token = credentials.get_access_token() #gets access token, necessary for using Spotify Web API
spotify = spotipy.Spotify(auth=token)

if token:

response = spotify.artist_top_tracks(artist)
print response['track'['name']]
else:

 