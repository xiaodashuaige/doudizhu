import asyncio
import logging.config
import sys
from concurrent.futures import ThreadPoolExecutor

import tornado.locks
import tornado.web
import tornado.websocket

# 动态加载 uvloop（仅在非 Windows 环境生效）
if not sys.platform.startswith("win"):
    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except ImportError:
        pass  # 忽略导入失败

from tornado.process import cpu_count

from api.auth import IndexHandler, LoginHandler, UserInfoHandler
from api.game.views import SocketHandler
from api.wx import WechatConfig, WechatHandler
from config import DEBUG, LOGGING, PORT, SECRET_KEY, TEMPLATE_ROOT, STATIC_ROOT, STATIC_URL

logging.config.dictConfig(LOGGING)

class Application(tornado.web.Application):
    def __init__(self):
        settings = {
            'debug': DEBUG,
            'cookie_secret': SECRET_KEY,
            'xsrf_cookies': False,
            'gzip': False,
            'autoescape': 'xhtml_escape',
            'template_path': TEMPLATE_ROOT,
            'static_path': STATIC_ROOT,
            'static_url_prefix': STATIC_URL,
            'login_url': '/login',
        }

        url_patterns = [
            ('/', IndexHandler),
            ('/login', LoginHandler),
            ('/userinfo', UserInfoHandler),
            ('/ws', SocketHandler),
            ('/social/config', WechatConfig),
            ('/social/index', WechatHandler),
        ]
        super().__init__(url_patterns, **settings)
        self.executor = ThreadPoolExecutor(cpu_count() * 2)
        self.allow_robot = True

async def main():
    app = Application()
    app.listen(PORT)
    logging.info(f'server on http://127.0.0.1:{PORT}')
    await asyncio.Event().wait()

if __name__ == '__main__':
    # 仅在非 Windows 环境调用 uvloop.install()
    if not sys.platform.startswith("win"):
        uvloop.install()
    asyncio.run(main())