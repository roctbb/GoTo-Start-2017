import random

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cats = [
            {"name": "Бывалый", "image": "images/1.jpg"},
            {"name": "Красавица", "image": "images/2.jpg"},
            {"name": "243", "image": "images/3.jpg"},
            {"name": "Янезнаю", "image": "images/4.jpg"},
            {"name": "Мурзик", "image": "images/5.jpg"},
        ]
        random_cat = random.choice(cats)
        self.render('cat.html', cat=random_cat)

routes = [
    (r"/", MainHandler),
    (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': 'images'})
]
app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()