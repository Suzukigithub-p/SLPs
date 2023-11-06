# SLPs(SpotifyLargePlaylists)

"SLPs(SpotifyLargePlaylists)" is a program to create large-scale playlists with Python.

# Requirement

* Python 3.6.5
* spotipy

# Installation

Install spotipy with pip command.

```bash
pip install spotipy
```

# Usage

Please run python code named "main.py" and enter query.

```bash
python main.py {user_name} {client_ID} {client_secret}　{search_limit}
```

If you want to finish it,please enter 'exit'.


# Example
```bash
$ python main.py {user_name} {client_ID} {client_secret}　20
Enter a title to create a playlist associated with it: 
$ Neurofunk
start to get tracks...
Get tracks from 5 playlists 
...
Get tracks from 20 playlists 
start to create playlist...
playlist size:9550
Add 1000 tracks 
...
Add 9000 tracks 
finnish to create Neurofunk2023-11-06
Enter a title to create a playlist associated with it: 
$ exit
```

# Note

I don't test environments under Linux and Mac.

Create a spotify playlist and enjoy listening to it!
Thank you!