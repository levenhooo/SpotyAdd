# SpotyAdd
An app that lets you add the currently playing song to your "Favourite Songs" playlist via a keyboard shortcut.

# Installation
1. Go to https://developer.spotify.com and log into your spotify account
2. Go to your dashboard and create a new app
3. Choose an app name, a description and a redirect uri like https://127.0.0.1:9090 (It doesn't need to be accessible)
4. Open the main.py and .env in your preferred code editor or IDE
5. Open the .env file and enter your client_id and client_secret you received from your newly created app
6. Make sure the redirect_uri in your .env file matches the one you used when creating your app
7. Run main.py and wait to be redirected to the Spotify website in your browser
8. Accept the request, then wait for the redirection to your selected URI (e.g., https://127.0.0.1:9090)
9. Copy the entire URI, paste it into your terminal, and press Enter
11. While listening to a song on Spotify, simply press the "+" key on your keyboard to add it to your "Liked Songs" playlist
- Feel free to change the hotkey in the config.json

# Starting
- SpotyAdd requires you to install python3 on your computer =>https://www.python.org/downloads/
- Simply execute the main.py with python3 (in the folder where all the files are)
