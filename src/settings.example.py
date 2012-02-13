import os

settings = {
    "host":"warmair.local",
    "database_host":"localhost",
    "database_name":"warmair",
    "database_user":"root",
    "database_password":"",
    "cookie_secret":"$cookie_secret",
    "twitter_consumer_key":"",
    "twitter_consumer_secret":"",
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path":  os.path.join(os.path.dirname(__file__), "templates"),
    "debug":True,
    "login_url":"/twitter/auth",
    "twitter_access_token": {
        "secret": "", 
        "user_id": "", 
        "screen_name": "", 
        "key": ""
    }
}
