import spotipy,sys,datetime
from spotify_token import Spotify_token
from logging import getLogger, StreamHandler, DEBUG

#user_name
user_name=sys.argv[1]
#client ID
my_id =sys.argv[2]
#client secret
my_secret = sys.argv[3]
#search limit
seach_limit=max((int(sys.argv[4])),1)

redirect_uri = 'http://localhost:8888/callback' 
scope = 'user-library-read user-read-playback-state playlist-read-private user-read-recently-played playlist-read-collaborative playlist-modify-public playlist-modify-private'
keys=['C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B']
d_today = datetime.date.today()

ST = Spotify_token(user_name, my_id, my_secret, redirect_uri)
token = ST.set()
sp = spotipy.Spotify(auth = token)

def getPlaylists(query,limit):
  response=sp.search(query,limit=20,type='playlist')
  countPlaylist=0
  extractPlaylists=[]
  nextPlaylists=response
  while(countPlaylist<limit):
    for playlist in nextPlaylists["playlists"]["items"]:
      countPlaylist+=1
      extractPlaylists.append(playlist)
      if(countPlaylist>=limit):break
    
    if(countPlaylist>=limit):break
    if(nextPlaylists["playlists"]["next"]==None):break
    nextPlaylists=sp.next(nextPlaylists["playlists"])
  return extractPlaylists

def getPlaylistItems(id):
  response=sp.playlist_items(playlist_id=id)
  extractItems=[]
  nextItems=response
  while(1):
    for item in nextItems["items"]:
      extractItems.append(item["track"]["id"])
    if(nextItems["next"]==None):break
    nextItems=sp.next(nextItems)
  return extractItems

def getTracks(query,limit=10):
  extractPlaylists=getPlaylists(query,limit)
  trackIDs=[]
  Count=1
  for playlist in extractPlaylists:
    trackIDs.extend(getPlaylistItems(playlist["id"]))
    trackIDs=list(set(trackIDs))
    if Count%5==0:logger.debug('Get tracks from '+str(Count)+' playlists ')
    Count+=1
  return trackIDs


def createPlaylist(trackIDs,title):
    playlist=sp.user_playlist_create(user_name,title+str(d_today))
    playlistID=playlist["id"]
    Count=100
    logger.debug("playlist size:"+str(len(trackIDs)))
    while trackIDs:
      try:
        sp.user_playlist_add_tracks(user_name, playlistID, trackIDs[:100])
        if Count%1000==0:logger.debug('Add '+str(Count)+' tracks ')
        elif Count==10000:break
        Count+=100
      except Exception as e:
        logger.debug(e)
      trackIDs=trackIDs[100:]




if __name__ == "__main__":
  logger = getLogger(__name__)
  handler = StreamHandler()
  handler.setLevel(DEBUG)
  logger.setLevel(DEBUG)
  logger.addHandler(handler)
  logger.propagate = False

  logger.debug('Enter a title to create a playlist associated with it: ')
  title=input()
  while(title!="exit"):
    logger.debug('start to get tracks...')
    trackIDs=getTracks(title,seach_limit)
    logger.debug('start to create playlist...')
    createPlaylist(trackIDs,title)
    logger.debug('finnish to create '+title+str(d_today))
    logger.debug('Enter a title to create a playlist associated with it: ')
    title=input()