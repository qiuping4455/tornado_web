from tornado.options import define

"""
在此写配置文件
"""
settings = dict(
    debug=True,
    template_path = 'templates',
    static_path = 'static',
)


"""
配置项目运行默认端口信息
"""
define(
    'port',
    default='8888',
    help ='Listening port',
    type = int
)