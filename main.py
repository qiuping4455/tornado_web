import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import options
from conf import urls,config
from handlers import handlers


class Application(tornado.web.Application):
    """
    初始化路由和设置
    """
    def __init__(self):
        super().__init__(urls.handlers_urls, **config.settings)


# 实例化对象
application = Application()


if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(options.port)
    print("Tornado server start on port: {}".format(str(options.port)))
    tornado.ioloop.IOLoop.current().start()
