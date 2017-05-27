import random

import tornado.ioloop
import tornado.web
import json

class CommentHandler(tornado.web.RequestHandler):
    def post(self):
        email = self.get_argument("email", "")
        text = self.get_argument("text", "")
        cat_id = int(self.get_argument("cat_id"))

        if email!="" and text!="":

            comment = {"email": email, "text": text, "cat_id": cat_id}

            with open("comments.txt", "r") as file:
                content = file.read()

            comments = json.loads(content)
            comments.append(comment)

            content = json.dumps(comments)

            with open("comments.txt", "w") as file:
                file.write(content)

        self.redirect('/?id={0}'.format(cat_id))


class MainHandler(tornado.web.RequestHandler):
    def get(self):

        id = int(self.get_argument("id", -1))

        with open("comments.txt", "r") as file:
            content = file.read()
        all_comments = json.loads(content)

        cats = [
            {"name": "Бывалый", "image": "images/1.jpg", "id": 1},
            {"name": "Красавица", "image": "images/2.jpg", "id": 2},
            {"name": "243", "image": "images/3.jpg", "id": 3},
            {"name": "Янезнаю", "image": "images/4.jpg", "id": 4},
            {"name": "Мурзик", "image": "images/5.jpg", "id": 5},
        ]
        random_cat = random.choice(cats)
        if id != -1:
            for cat in cats:
                if cat['id'] == id:
                    random_cat = cat

        comments = []
        for comment in all_comments:
            if comment['cat_id'] == random_cat['id']:
                comments.append(comment)

        self.render('cat.html', cat=random_cat, comments=comments)

routes = [
    (r"/", MainHandler),
    (r"/add_comment", CommentHandler),
    (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': 'images'})
]
app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()