# -*- coding: utf-8 -*-

import tornado.web
from tornado.auth import TwitterMixin
from tornado.escape import json_encode, json_decode
from lib.utilities import pretty_date
from datetime import datetime
import pprint

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = self.application.db
    
    def get_current_user(self):
        pid = self.get_secure_cookie("pid")
        if pid:
            return tornado.escape.json_decode(pid)
        else:
            return None

    def render(self, template_name, **kwargs):
        kwargs['settings'] = self.settings
        template_name = "%s/%s" % (self.settings['template_path'], template_name)
        return super(BaseHandler, self).render(template_name, **kwargs)

    def sign_person_in(self, user):
        """
        If we’ve seen the user before, update their info, otherwise create
        a brand new user record and set their cookie.
        
        """ 
        e_user = self.db.get("SELECT * FROM user WHERE twitter_id = %s", user['id'])
        print "post here"
        if e_user:
            self.db.execute("""UPDATE user 
                SET name=%s, screen_name=%s, description=%s, location=%s, url=%s,
                    profile_image_url=%s, time_zone=%s, access_token=%s, 
                    updated_at=NOW()
                WHERE twitter_id = %s""", user['name'], 
                    user['username'], user['description'], user['location'],
                    user['url'], user['profile_image_url'], user['time_zone'], 
                    json_encode(user['access_token']),e_user['twitter_id'])
        else:
            self.db.execute("""INSERT INTO user (   
                    twitter_id, name, screen_name, description, location, url, 
                    profile_image_url, time_zone, access_token, created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW())""",
                    user['id'], user['name'], user['username'], user['description'], user['location'],
                    user['url'], user['profile_image_url'], user['time_zone'],
                    json_encode(user['access_token']))
        
        pid = {'id':user['id'], 'name':user['name'], 'username':user['username']}
        self.set_secure_cookie("pid", tornado.escape.json_encode(pid), expires_days=365)
        
    def get_login_url(self):
        self.require_setting("login_url", "@tornado.web.authenticated")
        return self.application.settings["login_url"]
       
    def pretty_print(self, sent_in):
        pp = pprint.PrettyPrinter(indent=4)

        if sent_in:
            pp.pprint(sent_in)
        else:
            pp.pprint(self.__dict__)
        
        
    def sign_user_out(self):
        """
        Clears out any session keys.  
         oid stores a dict representing user.
        """
        self.clear_cookie("pid")
    

class IndexHandler(BaseHandler, TwitterMixin):
    def get(self):
        return self.render("index.html")    

class SignOutHandler(BaseHandler):
    def get(self):
        self.sign_user_out()
        return self.redirect("/")

class SignInHandler(BaseHandler, TwitterMixin):
    @tornado.web.asynchronous
    def get(self):
        try:
            if self.get_argument("oauth_token", None):
                self.get_authenticated_user(self.async_callback(self._on_auth))
                return
            self.authorize_redirect()
        except Exception as e:
            print "error 1"
            print e
            
    def _on_auth(self, user):
        try:
            if not user:
                raise tornado.web.HTTPError(500, "Twitter auth failed")
            self.sign_person_in(user)
            return self.redirect('/')
        except Exception as e:
            print "error 2"
            print e

class NotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("error.html")
