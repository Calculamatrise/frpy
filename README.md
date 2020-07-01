# Usage

This api requests data from Free Rider HD

Example 1 - Getting User Info:

```python
from frpy import *

username = "Guest"
print(getUser(username))
# getUser(username).get('user')
# Pretty print: print(json.dumps(getUser(username),indent=4))
```
Expected Output:

```JSON
{
    "user": {
        "u_id": 117248,
        "u_name": "guest",
        "d_name": "Guest",
        "img_url_medium": "https://secure.gravatar.com/avatar/16f000fecd4582f8aa6f424b2d9789c9/?s=100&d=mm&r=pg",
        "current_user": false,
        "classic": false,
        "admin": false,
        "plus": false,
        "cosmetics": {
            "head": {
                "img": "head_icons_4 head_icons_4-classic"
            }
        }
    },
    "user_stats": {
        "u_id": 117248,
        "tot_pts": 2,
        "cmpltd": 1,
        "rtd": 0,
        "cmmnts": 0,
        "crtd": 0,
        "head_cnt": 1,
        "total_head_cnt": 200
    },
    "user_info": false,
    "user_mobile_stats": {
        "lvl": "--",
        "wins": "--",
        "headCount": "--",
        "connected": "1"
    },
    "user_notification": false,
    "user_verify_reminder": false,
    "is_profile_owner": false,
    "recently_played_tracks_active": false,
    "recently_played_tracks": {
        "track_list_1_ad": false,
        "tracks": [
            {
                "title": "the canvas rider war",
                "slug": "5279-the-canvas-rider-war",
                "author": "railgrindsrule",
                "author_slug": "railgrindsrule",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/1/0c/5279/250x150-v5.png",
                "featured": false,
                "vote_percent": 94,
                "votes": 141,
                "best_time": "0:16.40",
                "img_url_small": "https://www.freeriderhd.com/u/railgrindsrule/pic?size=50"
            }
        ]
    },
    "recently_ghosted_tracks_active": true,
    "recently_ghosted_tracks": {
        "track_list_1_ad": true,
        "tracks": [
            {
                "title": "the canvas rider war",
                "slug": "5279-the-canvas-rider-war/r/guest",
                "author": "railgrindsrule",
                "author_slug": "railgrindsrule",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/1/0c/5279/250x150-v5.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/railgrindsrule/pic?size=50",
                "vote_percent": 94,
                "votes": 141,
                "best_time": "0:16.40"
            }
        ]
    },
    "created_tracks_active": false,
    "created_tracks": {
        "track_list_1_ad": false,
        "tracks": []
    },
    "show_liked_tracks": false,
    "liked_active": false,
    "liked_tracks": {
        "tracks": []
    },
    "friends_active": false,
    "friends": {
        "friend_cnt": 0,
        "friends_data": []
    },
    "friend_requests": {
        "request_cnt": 0,
        "request_data": []
    },
    "has_max_friends": false,
    "show_friends": true,
    "subscribe": false,
    "total_head_count": 200,
    "social_forum_url": "http://community.freeriderhd.com",
    "app_title": "Guest | Free Rider HD",
    "header_title": "Guest",
    "app_version": "d633437bb6"
}
```

Example 2 - Getting Track Data:

```python
from frpy import *

track_id = "1001"
print(getTrack(track_id))
# getTrack(track_id).get('track')
# Pretty print: print(json.dumps(getTrack(track_id),indent=4))
```
Expected Output:

```JSON
{
    "track": {
        "id": 1001,
        "title": "Wild West",
        "descr": "Wild West is a Free Rider community classic track by weewam.",
        "slug": "1001-wild-west",
        "u_id": 1001,
        "author_is_user": true,
        "u_url": "weewam",
        "author": "weewam",
        "author_slug": "weewam",
        "author_img_small": "https://cdn.freeriderhd.com/free_rider_hd/sprites/guest_profile_v2.png",
        "vehicle": "MTB",
        "cdn": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/b/8c/1001/track-data-v1.js",
        "date": "11/19/13",
        "img": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/b/8c/1001/250x150-v5.png",
        "img_768x250": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/b/8c/1001/768x250-v5.png",
        "kb_size": 66,
        "vehicles": [
            "BMX",
            "MTB"
        ],
        "date_ago": "7 years ago",
        "featured": false,
        "hide": 0
    },
    "track_stats": {
        "up_votes": 223,
        "dwn_votes": 62,
        "votes": 285,
        "vote_percent": 78,
        "plays": "36.0k",
        "runs": 371,
        "frst_runs": 163,
        "avg_time": "0:33.97",
        "cmpltn_rate": 0.03
    },
    "race_leaderboard": false,
    "show_race_leaderboard": false,
    "right_side_content": {
        "tracks": [
            {
                "id": 728104,
                "title": "Dont ask",
                "slug": "728104-dont-ask",
                "author": "KEELAN-KING-V2",
                "author_slug": "keelan-king-v2",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/c/88/728104/250x150-v12.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/KEELAN-KING-V2/pic?size=50",
                "vote_percent": 100,
                "votes": 11,
                "best_time": "0:08.63"
            },
            {
                "id": 728047,
                "title": "Detailed Trial",
                "slug": "728047-detailed-trial",
                "author": "Sharkfin",
                "author_slug": "sharkfin",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/d/73/728047/250x150-v12.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/Sharkfin/pic?size=50",
                "vote_percent": 74,
                "votes": 23,
                "best_time": "0:03.37"
            },
            {
                "id": 727751,
                "title": "Impromptu Squish Course",
                "slug": "727751-impromptu-squish-course",
                "author": "Coated_Badger",
                "author_slug": "coated_badger",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/9/d1/727751/250x150-v12.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/Coated_Badger/pic?size=50",
                "vote_percent": 82,
                "votes": 38,
                "best_time": "0:12.30"
            },
            {
                "id": 728112,
                "title": "Things to say",
                "slug": "728112-things-to-say",
                "author": "Sltg28",
                "author_slug": "sltg28",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/f/9e/728112/250x150-v12.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/Sltg28/pic?size=50",
                "vote_percent": 100,
                "votes": 8,
                "best_time": "0:52.60"
            },
            {
                "id": 728042,
                "title": "this town",
                "slug": "728042-this-town",
                "author": "Kazarx",
                "author_slug": "kazarx",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/2/3d/728042/250x150-v12.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/Kazarx/pic?size=50",
                "vote_percent": 91,
                "votes": 11,
                "best_time": "0:05.20"
            },
            {
                "id": 727916,
                "title": "NTBF",
                "slug": "727916-ntbf",
                "author": "a_drain",
                "author_slug": "a_drain",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/d/19/727916/250x150-v12.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/a_drain/pic?size=50",
                "vote_percent": 71,
                "votes": 34,
                "best_time": "0:12.27"
            },
            {
                "id": 728131,
                "title": "Blob wheelie idea",
                "slug": "728131-blob-wheelie-idea",
                "author": "Sharkfin",
                "author_slug": "sharkfin",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/9/fe/728131/250x150-v12.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/Sharkfin/pic?size=50",
                "vote_percent": 100,
                "votes": 8,
                "best_time": "0:01.73"
            },
            {
                "id": 728032,
                "title": "Los \u00c1rboles",
                "slug": "728032-los-rboles",
                "author": "TheGreatGnome",
                "author_slug": "thegreatgnome",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/6/e9/728032/250x150-v12.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/TheGreatGnome/pic?size=50",
                "vote_percent": 86,
                "votes": 36,
                "best_time": "0:02.87"
            },
            {
                "id": 728132,
                "title": "MTB uptube",
                "slug": "728132-mtb-uptube",
                "author": "Sharkfin",
                "author_slug": "sharkfin",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/0/5c/728132/250x150-v12.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/Sharkfin/pic?size=50",
                "vote_percent": 86,
                "votes": 7,
                "best_time": "0:02.27"
            },
            {
                "id": 727913,
                "title": "Eaorrrr, Kesaooooh...",
                "slug": "727913-eaorrrr-kesaooooh",
                "author": "copycatxel",
                "author_slug": "copycatxel",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/d/03/727913/250x150-v12.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/copycatxel/pic?size=50",
                "vote_percent": 80,
                "votes": 25,
                "best_time": "0:02.03"
            },
            {
                "id": 728021,
                "title": "Speed run",
                "slug": "728021-speed-run",
                "author": "ig0rhanelll",
                "author_slug": "ig0rhanelll",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/1/78/728021/250x150-v12.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/ig0rhanelll/pic?size=50",
                "vote_percent": 86,
                "votes": 14,
                "best_time": "0:12.80"
            },
            {
                "id": 727701,
                "title": "In Frame",
                "slug": "727701-in-frame",
                "author": "TheGreatGnome",
                "author_slug": "thegreatgnome",
                "thmb": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/c/ec/727701/250x150-v12.png",
                "featured": false,
                "img_url_small": "https://www.freeriderhd.com/u/TheGreatGnome/pic?size=50",
                "vote_percent": 85,
                "votes": 33,
                "best_time": "0:16.53"
            }
        ],
        "title": false,
        "list_only": true,
        "hide_ads": false,
        "ads_override": false
    },
    "track_comments": [
        {
            "user": {
                "u_name": "trickghoster3108",
                "d_name": "Trickghoster3108",
                "img_url_small": "https://secure.gravatar.com/avatar/a394303765630c93cc14d8d953e8fe90/?s=50&d=mm&r=pg"
            },
            "comment": {
                "id": 1909789,
                "msg": "<a href=\"https://www.freeriderhd.com/u/notverygood\">NotVeryGood</a> works weird but eh, watever",
                "time": "3 days ago",
                "can_delete": false,
                "flagged": false
            }
        },
        {
            "user": {
                "u_name": "notverygood",
                "d_name": "NotVeryGood",
                "img_url_small": "https://lh5.googleusercontent.com/-NTLshuX0ucU/AAAAAAAAAAI/AAAAAAAABMQ/KrUSdyUMRSo/photo.jpg?sz=50"
            },
            "comment": {
                "id": 1909767,
                "msg": "<a href=\"https://www.freeriderhd.com/u/trickghoster3108\">Trickghoster3108</a> just how it works",
                "time": "3 days ago",
                "can_delete": false,
                "flagged": false
            }
        },
        {
            "user": {
                "u_name": "trickghoster3108",
                "d_name": "Trickghoster3108",
                "img_url_small": "https://secure.gravatar.com/avatar/a394303765630c93cc14d8d953e8fe90/?s=50&d=mm&r=pg"
            },
            "comment": {
                "id": 1909543,
                "msg": "<a href=\"https://www.freeriderhd.com/u/notverygood\">NotVeryGood</a> what confused me is why it starts at 1001",
                "time": "3 days ago",
                "can_delete": false,
                "flagged": false
            }
        },
        {
            "user": {
                "u_name": "a_drain",
                "d_name": "a_drain",
                "img_url_small": "https://lh4.googleusercontent.com/-QmqWoGSia10/AAAAAAAAAAI/AAAAAAAAABA/xfqmJVggxNc/photo.jpg?sz=50"
            },
            "comment": {
                "id": 1735080,
                "msg": "<a href=\"https://www.freeriderhd.com/u/notverygood\">NotVeryGood</a> oh that's why. Yeah I 've seen that",
                "time": "4 weeks ago",
                "can_delete": false,
                "flagged": false
            }
        }
    ],
    "track_comments_load_more": true,
    "max_comment_length": 500,
    "logged_in_user": false,
    "user_track_stats": false,
    "campaign": false,
    "show_preroll_ads": true,
    "hide_ads": false,
    "ads_override": false,
    "is_admin": false,
    "totd": {
        "gems": 500,
        "lives": 30,
        "refill_cost": 10,
        "entries": []
    },
    "subscribe": {
        "is_subscribed": false,
        "count": 51
    },
    "race_uids": [],
    "game_settings": {
        "user": {
            "d_name": "Guest",
            "u_id": false,
            "cosmetics": {
                "head": {
                    "id": "1",
                    "title": "Classic Hat",
                    "type": "1",
                    "name": "classic",
                    "cost": "0",
                    "options": {
                        "back": "white"
                    },
                    "classname": "forward_cap",
                    "equiped": true,
                    "spritesheet_id": "4",
                    "img": "head_icons_4 head_icons_4-classic",
                    "show": true,
                    "script": "https://cdn.freeriderhd.com/free_rider_hd/assets/inventory/head/scripts/v5/forward_cap.js",
                    "limited": false
                }
            },
            "guest": true
        },
        "showHelpControls": true,
        "isCampaign": false,
        "track": {
            "id": 1001,
            "title": "Wild West",
            "descr": "Wild West is a Free Rider community classic track by weewam.",
            "url": "1001-wild-west",
            "vehicle": "MTB",
            "vehicles": [
                "BMX",
                "MTB"
            ],
            "size": 65606,
            "cdn": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/b/8c/1001/track-data-v1.js",
            "pwrups": {
                "gls": 1,
                "chkpts": 0,
                "bsts": 0,
                "grvty": 0,
                "slwmtn": 0,
                "bmbs": 0
            },
            "u_id": 1001,
            "author_is_user": true,
            "u_url": "weewam",
            "author": "weewam",
            "img": "https://cdn.freeriderhd.com/free_rider_hd/tracks/prd/b/8c/1001/250x150-v5.png",
            "ft_ts": 0,
            "featured": false,
            "p_ts": 1384895497,
            "hide": 0,
            "admin": false
        },
        "userTrackStats": false,
        "campaignData": false,
        "trackUploadCost": 25,
        "raceUids": [],
        "raceData": false,
        "soundsEnabled": true,
        "bestGhostEnabled": false,
        "requireTrackVerification": true
    },
    "app_title": "Wild West by weewam | Free Rider HD Track",
    "header_title": "Wild West",
    "app_version": "d633437bb6"
}
```