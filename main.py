import os
import json
import keyboard
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from datetime import datetime

#Load all environment variables
load_dotenv()

#Load config.json
with open("config.json") as config:
    config = json.load(config)

#Get hotkeys from config
hotkey_addtoPlaylist = str(config["hotkey_addtoPlaylist"])
hotkey_pause = str(config["hotkey_pause"])

#Set needed permissions
scope = ["user-read-currently-playing", "user-library-modify", "user-library-read"]

#Get environment variables
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")

#Create client with environment variables
client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

while True:
    #Adding the current song to the "Liked Songs" playlist
    if keyboard.is_pressed(hotkey=hotkey_addtoPlaylist):
        #Check if spotify is running or there is a song being played
        try:
            #Get the current song
            current_song = client.currently_playing(market=None, additional_types=None)
            #Extract trackId and put it into the trackURL list
            trackId = current_song["item"]["id"] 
            trackURL = [f"http://open.spotify.com/track/{trackId}"]
            trackName = current_song["item"]["name"]
            #Check if current song is already in "Liked Songs" playlist
            if client.current_user_saved_tracks_contains(tracks=trackURL)[0] == False:
                #Add current song to the "Liked Songs" playlist
                client.current_user_saved_tracks_add(tracks=trackURL)
                get_time = datetime.now()
                new_time = get_time.strftime("%H:%M:%S")
                current_time = new_time.replace("'", "")
                print(f"[{current_time}] {trackName} was added to Liked Songs.")
                continue
            else:
                get_time = datetime.now()
                new_time = get_time.strftime("%H:%M:%S")
                current_time = new_time.replace("'", "")
                print(f"[{current_time}] {trackName} is already in Liked Songs.")
                continue
        except:
            print("Spotify is not running or there is no song playing.")
    #Pause the program
    if keyboard.is_pressed(hotkey=hotkey_pause):
        print("Program is paused!")
        keyboard.wait(hotkey=hotkey_pause)
        print("Unpaused!")
        time.sleep(0.2)
        
