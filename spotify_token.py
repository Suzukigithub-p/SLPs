import spotipy.util as util

class Spotify_token:
    def __init__(self, username, my_id, my_secret, redirect_uri):
        self.username = username
        self.my_id=my_id
        self.my_secret=my_secret
        self.redirect_uri=redirect_uri
        self.scope = 'user-library-read user-read-playback-state playlist-read-private user-read-recently-played playlist-read-collaborative playlist-modify-public playlist-modify-private'

    def set(self):
        token = util.prompt_for_user_token(username=self.username, scope=self.scope, client_id=self.my_id, client_secret=self.my_secret,redirect_uri=self.redirect_uri)
        return token