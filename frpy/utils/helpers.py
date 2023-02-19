import requests

def getAuthorLeaderboard():
	return requests.get("https://www.freeriderhd.com/leaderboards/player/lifetime?ajax").json()

def getCategory(category):
	return requests.get(f"https://www.freeriderhd.com/{category}?ajax").json()

def getComment(track_id, comment_id):
	return requests.get(f"https://www.freeriderhd.com//track_comments/load_more/{track_id}/{comment_id}").json()

def getFeaturedGhosts():
	return requests.get("https://raw.githubusercontent.com/Calculamatrise/official_featured_ghosts/master/data.json").json()

def getHome():
	return requests.get("https://www.freeriderhd.com?ajax").json()

def getPlayerLeaderboard():
	return requests.get("https://www.freeriderhd.com/leaderboards/player/lifetime?ajax").json()

def getRace(track_id, username):
	return requests.get(f"https://www.freeriderhd.com/t/{int(track_id)}/r/{username}?ajax").json()

def getRandom():
	return requests.get("https://www.freeriderhd.com/random/track?ajax").json()

def getTrack(id):
	if id < 1001:
		raise Exception("No tracks exist with an id less than 1001!")

	return requests.get(f"https://www.freeriderhd.com/t/{id}?ajax").json()

def getTrackLeaderboard(id):
	if id < 1001:
		raise Exception("No tracks exist with an id less than 1001!")

	return requests.post("https://www.freeriderhd.com/random//track_api/load_leaderboard", { "t_id": int(id) }).json()

def getUser(uid):
	if type(uid) is int:
		return requests.post(f"https://www.freeriderhd.com//friends/remove_friend", {
			"u_id": uid
		}).json()

	return requests.get(f"https://www.freeriderhd.com/u/{uid}?ajax").json()