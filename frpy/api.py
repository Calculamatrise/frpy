import json
import requests

__all__ = ['getFeaturedGhosts', 'getHome', 'getCategory', 'getLead', 'getUser', 'getTrack', 'getRandom', 'User', 'Track']

def getFeaturedGhosts():
    response = requests.get("https://raw.githubusercontent.com/Calculus0972/Official_Featured_Ghosts/master/ghosts.json")
    return response.json()

def getHome():
    response = requests.get("https://www.freeriderhd.com?ajax=true")
    return response.json()

def getLead():
    response = requests.get("https://www.freeriderhd.com/leaderboards/player/lifetime?ajax=true")
    return response.json()

def getCategory(category):
    response = requests.get("https://www.freeriderhd.com/{}?ajax".format(category))
    return response.json()

def getUser(username):
    response = requests.get("https://www.freeriderhd.com/u/{}?ajax=true".format(username))
    return response.json()

def getTrack(track_id):
    response = requests.get("https://www.freeriderhd.com/t/{}?ajax=true".format(track_id))
    return response.json()

def getRandom():
    response = requests.get("https://www.freeriderhd.com/random/track?ajax=true")
    return response.json()

session = requests.Session()
class User:
    def __init__(self):
        self.token = None
        self.user = None
        self.s = None
    
    def login(self, t):
        self.token = t
    
    def logout(self):
        self.token = None
    
    def defaultLogin(self, u, p):
        self.s = session.post('https://www.freeriderhd.com/auth/standard_login', data={'login': u, 'password': p})

    def verifyLogin(self):
        if self.token == None:
            return print('You are not logged in')
        response = requests.get('https://www.freeriderhd.com?ajax=!0&app_signed_request={}'.format(self.token))
        response = response.json()
        self.user = response.get('user')
        return response

    def getMyUser(self):
        if self.token == None:
            return print('You are not logged in')
        self.verifyLogin()
        user = getUser(self.user.get('d_name'))
        self.user = user.get('user')
        return user

    def getNotifications(self):
        if self.token == None:
            return print('You are not logged in')
        response = requests.get('https://www.freeriderhd.com/notifications?ajax=!0&app_signed_request={}&t_1=ref&t_2=desk'.format(self.token))
        response = response.json()
        return response

    @staticmethod
    def getComment(t, c):
        t = getTrack(t)
        for i in t.get('track_comments'):
            if i.get('comment').get('id') == c:
                return i

    def datapoll(self):
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/datapoll/poll_request/?notifications=!0&ajax=!0&app_signed_request={}&t_1=ref&t_2=desk'.format(self.token))
        response = response.json()
        return response
    
    def changeName(self, u):
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/account/edit_profile/?name=u_name&value={u}&ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(u = u, t = self.token), data={'value': u})
        response = response.json()
        return response

    def changeDesc(self, d):
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/account/edit_profile/?name=about&value={d}&ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(d = d, t = self.token), data={'value': d})
        response = response.json()
        return response

    def changePassword(self, o, n):
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/account/change_password/?old_password={o}&new_password={n}&ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(o = o, n = n, t = self.token))
        response = response.json()
        return response
    
    def changeForumsPassword(self, p):
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/account/update_forum_account/?password={p}&ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(p = p, t = self.token))
        response = response.json()
        return response
    
    def buyHead(self):
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/store/buy/?ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(t = self.token))
        response = response.json()
        return response

    def equipHead(self, i):
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/store/equip/?item_id={i}&ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(i = i, t = self.token))
        response = response.json()
        return response

    def addFriend(self, f):
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/friends/send_friend_request/?u_name={f}&ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(f = f, t = self.token))
        response = response.json()
        return response
    
    def removeFriend(self, i):
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/friends/remove_friend/?u_id={i}&ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(i = i, t = self.token))
        response = response.json()
        return response
    
    def acceptFriend(self, i):
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/friends/respond_to_friend_request/?u_id={i}&ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(i = i, t = self.token))
        response = response.json()
        return response
    
    def challenge(self, u, m, t):
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/challenge/send/?ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(p = p, t = self.token))
        response = response.json()
        return response

    def comment():
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/track_comments/post/?ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(p = p, t = self.token))
        response = response.json()
        return response

    def vote():
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/track_api/vote/?t_id={}&vote={}&ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(p = p, t = self.token))
        response = response.json()
        return response

    def subscribe():
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/track_api/subscribe/?ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(p = p, t = self.token))
        response = response.json()
        return response

    def redeemCoupon():
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/store/redeemCouponCode/?ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(p = p, t = self.token))
        response = response.json()
        return response

    def signup():
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/auth/standard_signup/?ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(p = p, t = self.token))
        response = response.json()
        return response

    def publish():
        if self.token == None:
            return print('You are not logged in')
        response = requests.post('https://www.freeriderhd.com/create/submit/?ajax=!0&app_signed_request={t}&t_1=ref&t_2=desk'.format(p = p, t = self.token))
        response = response.json()
        return response

def encode(n, N=32):
    if n > 0:
        return (encode(n//N,N)+"0123456789abcdefghijklmnopqrstuv"[n%N]).lstrip("0")
    elif n == 0:
        return "0"
    elif n < 0:
        return '-' + (encode(abs(n)//N,N)+"0123456789abcdefghijklmnopqrstuv"[abs(n)%N]).lstrip("0")

def decode(i):
    return int(str(i), 32)
    
class Track:
    def __init__(self):
        self.black = []
        self.grey = []
        self.powerups = {
            "targets": [],
            "slowmos": [],
            "bombs": [],
            "checkpoints": [],
            "antigravity": [],
            "boosters": [],
            "gravity": [],
            "teleporters": [],
            "vehicles": {
                "heli": [],
                "truck": [],
                "balloon": [],
                "blob": []
            }
        }
    
    def code(self, c):
        self.black = c[0]
        self.grey = c[1]
        self.powerups = c[2]
        # Unfinished

    def clear(self):
        self.black = []
        self.grey = []
        self.powerups = {
            "targets": [],
            "slowmos": [],
            "bombs": [],
            "checkpoints": [],
            "antigravity": [],
            "boosters": [],
            "gravity": [],
            "teleporters": [],
            "vehicles": {
                "heli": [],
                "truck": [],
                "balloon": [],
                "blob": []
            }
        }
    
    @staticmethod
    def encode(n):
        return encode(int(float(n)))

    @staticmethod
    def decode(i):
        return int(str(i), 32)

    def drawLine(self, t, x, y, ex, ey):
        if t == 'b' | t == 'black' | t == 'p' | t == 'pysics':
            self.black.append([str(x), str(y), str(ex), str(ey)])
        elif t == 'g' | t == 'grey' | t == 'gray' | t == 's' | t == 'scenery':
            self.grey.append([str(x), str(y), str(ex), str(ey)])
        else:
            return print("{} is not a line type.".format(t))

    def drawPhysicsLine(self, x, y, ex, ey):
        self.black.append([str(x), str(y), str(ex), str(ey)])
    
    def drawSceneryLine(self, x, y, ex, ey):
        self.grey.append([str(x), str(y), str(ex), str(ey)])
    
    def drawStart(self):
        self.black.append([str(-40), str(50), str(40), str(50)])

    def drawPowerup(self, p, x, y, t, ey):
        if p == 'target':
            self.powerups['targets'].append([x, y])
        elif p == 'slowmo':
            self.powerups['slowmos'].append([x, y])
        elif p == 'bomb':
            self.powerups['bombs'].append([x, y])
        elif p == 'checkpoint':
            self.powerups['checkpoints'].append([x, y])
        elif p == 'antigravity':
            self.powerups['antigravity'].append([x, y])
        elif p == 'boost':
            self.powerups['boosters'].append([x, y, t])
        elif p == 'gravity':
            self.powerups['gravity'].append([x, y, t])
        elif p == 'teleport':
            self.powerups['teleporters'].append([x, y, t, ex])
        elif p == 'heli':
            self.powerups['vehicles']['heli'].append([x, y, 1, t])
        elif p == 'truck':
            self.powerups['vehicles']['truck'].append([x, y, 2, t])
        elif p == 'balloon':
            self.powerups['vehicles']['balloon'].append([x, y, 3, t])
        elif p == 'blob':
            self.powerups['vehicles']['blob'].append([x, y, 4, t])
        else:
            return print("{} is not a powerup.".format(p))

    def drawTarget(self, x, y):
        self.powerups['targets'].append([x, y])
    
    def drawSlowmo(self, x, y):
        self.powerups['slowmos'].append([x, y])

    def drawBomb(self, x, y):
        self.powerups['bombs'].append([x, y])
    
    def drawCheckpoint(self, x, y):
        self.powerups['checkpoints'].append([x, y])
    
    def drawAntigravity(self, x, y):
        self.powerups['antigravity'].append([x, y])
    
    def drawBoost(self, x, y):
        self.powerups['boosters'].append([x, y, t])
    
    def drawGravity(self, x, y):
        self.powerups['gravity'].append([x, y, t])

    def drawTeleport(self, x, y, ex, ey):
        self.powerups['teleporters'].append([x, y, ex, ey])
    
    def drawVehicle(self, v, x, y, t):
        if v == 'heli':
            self.powerups['vehicles']['heli'].append([x, y, 1, t])
        elif v == 'truck':
            self.powerups['vehicles']['truck'].append([x, y, 2, t])
        elif v == 'balloon':
            self.powerups['vehicles']['balloon'].append([x, y, 3, t])
        elif v == 'blob':
            self.powerups['vehicles']['blob'].append([x, y, 4, t])
        else:
            return print("{} is not a vehicle.".format(v))

    def drawHeli(self, x, y, t):
        self.powerups['vehicles']['heli'].append([x, y, 1, t])
    
    def drawTruck(self, x, y, t):
        self.powerups['vehicles']['truck'].append([x, y, 2, t])
    
    def drawBalloon(self, x, y, t):
        self.powerups['vehicles']['balloon'].append([x, y, 3, t])
    
    def drawBlob(self, x, y, t):
        self.powerups['vehicles']['blob'].append([x, y, 4, t])

    def encodePhysics(self):
        b = self.black
        self.black = []
        for a in b:
            c = a
            a = []
            for x in c:
                x = self.encode(x)
                a.append(x)
            a = " ".join(a)
            self.black.append(a)
        return ",".join(self.black)
        
    def encodeScenery(self):
        g = self.grey
        self.grey = []
        for a in g:
            b = a
            a = []
            for x in b:
                x = self.encode(x)
                a.append(x)
            a = " ".join(a)
            self.grey.append(a)
        return ",".join(self.grey)

    def encodePowerups(self):
        p = self.powerups
        self.powerups = []
        for a in p:
            if type(p[a]).__name__ == 'list':
                if a == 'targets':
                    b = p[a]
                    p[a] = []
                    for c in b:
                        x = c
                        c = []
                        c.append('T')
                        for i in x:
                            x = self.encode(i)
                            c.append(x)
                        p[a] = " ".join(c)
                elif a == 'slowmos':
                    b = p[a]
                    p[a] = []
                    for c in b:
                        x = c
                        c = []
                        c.append('S')
                        for i in x:
                            x = self.encode(i)
                            c.append(x)
                        p[a] = " ".join(c)
                elif a == 'bombs':
                    b = p[a]
                    p[a] = []
                    for c in b:
                        x = c
                        c = []
                        c.append('O')
                        for i in x:
                            x = self.encode(i)
                            c.append(x)
                        p[a] = " ".join(c)
                elif a == 'checkpoints':
                    b = p[a]
                    p[a] = []
                    for c in b:
                        x = c
                        c = []
                        c.append('C')
                        for i in x:
                            x = self.encode(i)
                            c.append(x)
                        p[a] = " ".join(c)
                elif a == 'antigravity':
                    b = p[a]
                    p[a] = []
                    for c in b:
                        x = c
                        c = []
                        c.append('A')
                        for i in x:
                            x = self.encode(i)
                            c.append(x)
                        p[a] = " ".join(c)
                elif a == 'boosters':
                    b = p[a]
                    p[a] = []
                    for c in b:
                        x = c
                        c = []
                        c.append('B')
                        for i in x:
                            x = self.encode(i)
                            c.append(x)
                        p[a] = " ".join(c)
                elif a == 'gravity':
                    b = p[a]
                    p[a] = []
                    for c in b:
                        x = c
                        c = []
                        c.append('G')
                        for i in x:
                            x = self.encode(i)
                            c.append(x)
                        p[a] = " ".join(c)
                elif a == 'teleporters':
                    b = p[a]
                    p[a] = []
                    for c in b:
                        x = c
                        c = []
                        c.append('W')
                        for i in x:
                            x = self.encode(i)
                            c.append(x)
                        p[a] = " ".join(c)
            elif type(p[a]).__name__ == 'dict':
                for b in p[a]:
                    if b == 'heli':
                        c = p[a][b]
                        p[a][b] = []
                        for d in c:
                            x = d
                            d = []
                            d.append('V')
                            for i in x:
                                i = self.encode(i)
                                d.append(i)
                            p[a][b] = " ".join(d)
                    elif b == 'truck':
                        c = p[a][b]
                        p[a][b] = []
                        for d in c:
                            x = d
                            d = []
                            d.append('V')
                            for i in x:
                                i = self.encode(i)
                                d.append(i)
                            p[a][b] = " ".join(d)
                    elif b == 'balloon':
                        c = p[a][b]
                        p[a][b] = []
                        for d in c:
                            x = d
                            d = []
                            d.append('V')
                            for i in x:
                                i = self.encode(i)
                                d.append(i)
                            p[a][b] = " ".join(d)
                    elif b == 'blob':
                        c = p[a][b]
                        p[a][b] = []
                        for d in c:
                            x = d
                            d = []
                            d.append('V')
                            for i in x:
                                i = self.encode(i)
                                d.append(i)
                            p[a][b] = " ".join(d)
        r = []
        r.append(str(p['targets'])) if p['targets'] else None
        r.append(str(p['slowmos'])) if p['slowmos'] else None
        r.append(str(p['bombs'])) if p['bombs'] else None
        r.append(str(p['checkpoints'])) if p['checkpoints'] else None
        r.append(str(p['antigravity'])) if p['antigravity'] else None
        r.append(str(p['boosters'])) if p['boosters'] else None
        r.append(str(p['gravity'])) if p['gravity'] else None
        r.append(str(p['teleporters'])) if p['teleporters'] else None
        r.append(str(p['vehicles']['heli'])) if p['vehicles']['heli'] else None
        r.append(str(p['vehicles']['truck'])) if p['vehicles']['truck'] else None
        r.append(str(p['vehicles']['balloon'])) if p['vehicles']['balloon'] else None
        r.append(str(p['vehicles']['blob'])) if p['vehicles']['blob'] else None
        return ",".join(r)

    def export(self):
        return "{black}#{grey}#{powerups}".format(black = self.encodePhysics(), grey = self.encodeScenery(), powerups = self.encodePowerups())
