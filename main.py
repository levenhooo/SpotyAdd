import os
from datetime import datetime
import keyboard
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

#Load all environment variables
load_dotenv()

#Set needed permissions
scope = ["user-read-currently-playing", "user-library-modify", "user-library-read"]

#Get environment variables
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")

#Create client with environment variables
client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

while True:
    if keyboard.is_pressed(hotkey="+"):
        #Get the current song
        current_song = client.currently_playing(market=None, additional_types=None)

        #Extract trackId and put it into the trackURL list
        trackId = current_song["item"]["id"] 
        trackURL = [f"http://open.spotify.com/track/{trackId}"]

        #Check if current song is already in "Liked Songs" playlist
        if client.current_user_saved_tracks_contains(tracks=trackURL)[0] == False:
            #Add current song to the "Liked Songs" playlist
            client.current_user_saved_tracks_add(tracks=trackURL)
            get_time = datetime.now()
            new_time = get_time.strftime("%H:%M:%S")
            time = new_time.replace("'", "")
            print(f"[{time}] Song was added to favourite songs.")
            continue
        else:
            get_time = datetime.now()
            new_time = get_time.strftime("%H:%M:%S")
            time = new_time.replace("'", "")
            print(f"[{time}] Song is already in favourite songs.")
            continue
        
