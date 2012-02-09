from tornado.options import define, options


def parse_dictionary(settings):
    for key, value in settings.iteritems():
        if key in options:
            options[key].set(value)


define('debug', type=bool, default=True, help="Run in debug/development mode")
define('dump_settings', type=bool, default=False, help="Dump evaluated settings and exit")

# app settings
define('cookie_secret', metavar="SECRET", help="Secret to use for encoding secure cookies")
define('xsrf_cookies', type=bool, default=True, help="Use Tornado XSRF protection")
define('on_port', default=8000, help="Run on port")
define('login_url', default="/sign-in", help="Set the default login url when not signed in.")
# infrastructure
define('database_host', metavar="HOST", help="Hostname for database connection")
define('database_name', metavar="DATABASE", help="Database name for database connection")
define('database_user', metavar="NAME", help="Username for database connection")
define('database_password', metavar="PASSWORD", help="Password for database connection")

# APIs
define('twitter_consumer_key', metavar='KEY', help="Twitter API consumer key")
define('twitter_consumer_secret', metavar='SECRET', help="Twitter API consumer secret")
