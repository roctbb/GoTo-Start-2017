import random

import tornado.ioloop
import tornado.web
import json

class CommentHandler(tornado.web.RequestHandler):
    def post(self):
        email = self.get_argument("email", "")
        text = self.get_argument("text", "")

        if email!="" and text!="":

            comment = {"email": email, "text": text}

            with open("comments.txt", "r") as file:
                content = file.read()

            comments = json.loads(content)
            comments.append(comment)

            content = json.dumps(comments)

            with open("comments.txt", "w") as file:
                file.write(content)

        self.redirect('/')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        with open("comments.txt", "r") as file:
            content = file.read()
        comments = json.loads(content)

        cats = [
            {"name": "Бывалый", "image": "images/1.jpg"},
            {"name": "Красавица", "image": "images/2.jpg"},
            {"name": "243", "image": "images/3.jpg"},
            {"name": "Янезнаю", "image": "images/4.jpg"},
            {"name": "Мурзик", "image": "images/5.jpg"},
        ]
        random_cat = random.choice(cats)
        self.render('cat.html', cat=random_cat, comments=comments)

routes = [
    (r"/", MainHandler),
    (r"/add_comment", CommentHandler),
    (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': 'images'})
]
app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()