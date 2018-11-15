import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    """
    首页，显示用户关注图片流
    """
    def get(self, *args, **kwargs):
        self.render('index.html')
class ExploreHandler(tornado.web.RequestHandler):
    """
    发现页，最近上传图片
    """
    def get(self, *args, **kwargs):
        self.render('explore.html')

class PostHandler(tornado.web.RequestHandler):
    """
    单个图片详情页
    """
    def get(self, *args, **kwargs):
        self.render('post.html',post_id = kwargs['post_id'])
