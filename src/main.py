#!/usr/bin/env python
import os.path
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.database
import tornado.options
from tornado.options import define, options

from routes import routes
import warmairoptions
from settings import settings


class WarmairApplication(tornado.web.Application):
    @classmethod
    def app_settings(cls):
        dirname = os.path.dirname(os.path.abspath(__file__))
        return {
            "debug": options.debug,
            "cookie_secret": options.cookie_secret,
            "xsrf_cookies": options.xsrf_cookies,
            "twitter_consumer_key" : options.twitter_consumer_key,
            "twitter_consumer_secret" : options.twitter_consumer_secret,

            "login_url": options.login_url,
            "static_path": os.path.join(dirname, "static"),
            "template_path":  os.path.join(dirname, "templates"),
        }

    def __init__(self, *args, **settings):
        self.db = tornado.database.Connection(
            host=options.database_host,
            database=options.database_name, 
            user=options.database_user,
            password=options.database_password)
        super(WarmairApplication, self).__init__(*args, **settings)

if __name__ == "__main__":
    warmairoptions.parse_dictionary(settings)
    tornado.options.parse_command_line()

    if options.dump_settings:
        from pprint import pprint
        pprint({'options': dict((k, opt.value()) for k, opt in options.iteritems()), 'app_settings': app_settings})
        sys.exit(0)

    app_settings = WarmairApplication.app_settings()
    application = WarmairApplication(routes, **app_settings)
    http_server = tornado.httpserver.HTTPServer(application)
    
    print "starting on port %s" % (options.on_port)
    http_server.listen(int(options.on_port))
    tornado.ioloop.IOLoop.instance().start()
