import os
import json
import keyboard
import tkinter as tk
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

#Get hotkey from config
hotkey_addtoPlaylist = str(config["hotkey_addtoPlaylist"])

#Set needed permissions
scope = ["user-read-currently-playing", "user-library-modify", "user-library-read"]

#Get environment variables
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")

#Create client with environment variables
client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

#UI
root = tk.Tk()
root.title("SpotyAdd")
root.geometry("350x200")
#CaptureInput
start_button = tk.Button(root, text="Start", background="white", command=lambda: SpotyAdd.AddHotkey())
start_button.pack()
#StopInput
pause_button = tk.Button(root, text="Pause",  background="white", command=lambda: SpotyAdd.RemoveHotkeyForPause())
pause_button.pack()
#Exit
exit_button = tk.Button(root, text="Exit",  background="white", command=lambda: root.quit())
exit_button.pack()

CaptureInput = False
StopInput = False

class SpotyAdd():
    def AddHotkey():
        global CaptureInput, StopInput
        CaptureInput = True
        StopInput = False
        #Add hotkey
        keyboard.add_hotkey(hotkey=hotkey_addtoPlaylist, callback=SpotyAdd.OnHotkey)
        #Set button states
        if CaptureInput == True:
            pause_button.config(state="normal")
            start_button.config(state="disabled")
    
    def OnHotkey():
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
                    time.sleep(1)
                else:
                    get_time = datetime.now()
                    new_time = get_time.strftime("%H:%M:%S")
                    current_time = new_time.replace("'", "")
                    print(f"[{current_time}] {trackName} is already in Liked Songs.")
                    time.sleep(1)
            except:
                print("Spotify is not running or there is no song playing.")
                time.sleep(1)

    def RemoveHotkeyForPause():
        global CaptureInput, StopInput
        CaptureInput = False
        StopInput = True
        #Remove hotkey
        keyboard.remove_hotkey(hotkey_or_callback=hotkey_addtoPlaylist)
        #Set button states
        if CaptureInput == False:
            start_button.config(state="normal")
            pause_button.config(state="disabled")

root.mainloop()
