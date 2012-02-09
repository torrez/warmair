import handlers

routes = [
    (r"/", handlers.IndexHandler),
   (r"/sign-in", handlers.SignInHandler),
    (r"/sign-out", handlers.SignOutHandler),
    (r".*", handlers.NotFoundHandler)
]
