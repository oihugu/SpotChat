import os
from twitchio.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

class Bot(commands.Bot):

    def __init__(self):

        with open('sec', 'r') as k:
            self.keys = k.readlines()
        
        super().__init__(
            irc_token=self.keys[0].replace('\n', ''),
            client_id=self.keys[1].replace('\n', ''),
            nick='oihugu',
            prefix='++',
            initial_channels=['oihugu']
        )

        

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.keys[3].replace('\n', ''),
                                               client_secret=self.keys[4].replace('\n', ''),
                                               redirect_uri="http://localhost:8080/",
                                               scope="user-read-playback-state,user-modify-playback-state"))
    
    async def event_ready(self):
        print('Loguei')
    
    @commands.command(name='spoti')
    async def spot(self, ctx):
        song = ctx.content.split(' ')[1]
        self.sp.start_playback(uris=[song])
    
    @commands.command(name='spotify')
    async def spotfy(self, ctx):
        
        song_name = ''

        for elem in ctx.content.split(' ')[1:]:
            song_name += elem + ' '

        song_name = song_name.strip()

        results = self.sp.search(q=song_name, limit=1)

        track  = results['tracks']['items'][0]
        song = track['uri']

        print(track['name'])

        self.sp.start_playback(uris=[song])