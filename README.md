# Demo Code

```py
from frpy import Client

client = Client()

def ready(self):
    print("Ready!")

client.on("ready", ready)
client.login("token")
# client.login(
#     username = "Guest",
#     password = "password"
# )
```

# Data Retrievers

This api requests data from Free Rider HD

Example 1 - Getting User Info:

```python
from frpy import getUser

username = "Guest"
user = getUser(username)

print(user.toJSON())
```
Expected Output:

```JSON
{
	"admin": false,
	"avatar": "https://cdn.freeriderhd.com/free_rider_hd/sprites/guest_profile_v2.png",
	"classic": false,
	"cosmetics": {
		"head": {
			"img": "head_icons_4 head_icons_4-classic"
		}
	},
	"createdTracks": [],
	"displayName": "Guest",
	"forums": null,
	"friendLimitReached": false,
	"friends": [],
	"id": 0,
	"likedTracks": [],
	"mobileStats": {
		"connected": "1",
		"headCount": "--",
		"level": "--",
		"wins": "--"
	},
	"moderator": false,
	"plus": false,
	"recentlyCompleted": [],
	"recentlyPlayed": [],
	"stats": {
		"comments": 0,
		"completed": 0,
		"created": 0,
		"headCount": 1,
		"rated": 0,
		"totalHeadCount": 200,
		"totalPoints": 0
	},
	"username": "guest"
}
```

Example 2 - Getting Track Data:

```python
from frpy import getTrack

track_id = 1001
track = getTrack(track_id)

print(getTrack(track_id).toJSON())
```
Expected Output:

```JSON
{
	"author": "weewam",
	"comments": [],
	"createdAt": "11/19/13",
	"createdDateAgo": "9 years ago",
	"description": "Wild West is a Free Rider community classic track by weewam.",
	"featured": false,
	"hidden": 0,
	"id": 1001,
	"maxCommentLength": 500,
	"size": 66,
	"stats": {
		"averageRating": 79,
		"averageTime": "38:37.83",
		"completionRate": 0.03,
		"downVotes": 67,
		"firstRuns": null,
		"plays": "59.5k",
		"runs": 571,
		"upVotes": 257,
		"votes": 324
	},
	"thumbnail": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/b/8c/1001/768x250-v5.png",
	"title": "Wild West",
	"trackOfTheDay": {
		"entries": [],
		"gems": 500,
		"lives": 30,
		"refillCost": 10
	},
	"vehicle": "MTB",
	"vehicles": [
		"BMX",
		"MTB"
	]
}
```