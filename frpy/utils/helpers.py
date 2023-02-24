from ..structures.Track import Track
from ..structures.User import User
from ..utils.RequestHandler import RequestHandler
import requests

def getAuthorLeaderboard():
    return RequestHandler.get('/leaderboards/player/lifetime')

def getCategory(category):
    return RequestHandler.get('/' + category)

def getComment(track_id, comment_id):
    return RequestHandler.get(f'/track_comments/load_more/{track_id}/{comment_id}')

def getFeaturedGhosts():
    return requests.get("https://raw.githubusercontent.com/Calculamatrise/official_featured_ghosts/master/data.json")

def getPlayerLeaderboard():
    return RequestHandler.get('/leaderboards/player/lifetime')

def getRace(track_id, username):
    return RequestHandler.get(f'/t/{int(track_id)}/r/{username}')

def getRandom():
    return RequestHandler.get('/random/track')

def getTrack(tid):
    tid = int(tid)
    if tid < 1001:
        raise Exception("No tracks exist with an id less than 1001!")

    return Track(RequestHandler.get('/t/' + str(tid)))

def getTrackLeaderboard(tid):
    tid = int(tid)
    if tid < 1001:
        raise Exception("No tracks exist with an id less than 1001!")

    return RequestHandler.post('/track_api/load_leaderboard', data = {
        't_id': tid
    })

def getUser(uid):
    if isinstance(uid, int):
        uid = RequestHandler.post('/friends/remove_friend', False, data = {
            'u_id': uid
        }).get('msg')[25:-31]

    return User(RequestHandler.get('/u/' + str(uid)))