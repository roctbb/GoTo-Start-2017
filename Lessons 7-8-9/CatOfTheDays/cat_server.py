import random

import tornado.ioloop
import tornado.web
import json
from pymongo import MongoClient

connection = MongoClient("mongodb://user:password@ds155191.mlab.com:55191/goto_cats")
database = connection['goto_cats']
cats_collection = database['cats']


class CommentHandler(tornado.web.RequestHandler):
    def post(self):
        email = self.get_argument("email", "")
        text = self.get_argument("text", "")
        cat_id = int(self.get_argument("cat_id"))

        if email != "" and text != "":
            comment = {"email": email, "text": text}

            cat = cats_collection.find_one({"id": cat_id})
            cat['comments'].append(comment)

            cats_collection.update({"id": cat_id}, cat)

        self.redirect('/?id={0}'.format(cat_id))


class MainHandler(tornado.web.RequestHandler):
    def get(self):

        id = int(self.get_argument("id", -1))

        cats = list(cats_collection.find())
        random_cat = random.choice(cats)
        if id != -1:
            for cat in cats:
                if cat['id'] == id:
                    random_cat = cat

        self.render('cat.html', cat=random_cat)


routes = [
    (r"/", MainHandler),
    (r"/add_comment", CommentHandler),
    (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': 'images'})
]
app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
