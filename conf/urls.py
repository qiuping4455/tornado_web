from handlers import handlers

"""
在此写页面路由
"""
handlers_urls = [
            ('/', handlers.IndexHandler),
            ('/explore', handlers.ExploreHandler),
            ('/post/(?P<post_id>[0-9]+)', handlers.PostHandler),

        ]