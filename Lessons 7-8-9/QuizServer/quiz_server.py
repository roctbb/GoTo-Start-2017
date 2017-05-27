import random

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('form.html')


class SubmitHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "")
        age = self.get_argument("age", "")
        color = self.get_argument("color")

        colornames = {"strange": "серобуромалиновый",
                      "red": "красный",
                      "blue": "синий",
                      "green": "зеленый",
                      }

        if name == "" or age == "":
            self.write("Заполни все поля!")
        else:
            self.write("Тебя зовут {0}, тебе {1} годиков, тебе нравится {2}."
                       .format(name, age, colornames[color]))


routes = [
    (r"/", MainHandler),
    (r"/submit", SubmitHandler),
    (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': 'images'})
]
app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
