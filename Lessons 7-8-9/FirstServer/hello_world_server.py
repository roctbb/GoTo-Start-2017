import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h3>Hello, world</h3>")
        self.write("<p>This is my first page.</p>")

class PageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/simple_page.html")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", 'Anon')
        self.write("<h3>Hello, {0}</h3>".format(name))

routes = [
    (r"/", MainHandler),
    (r"/page", PageHandler),
    (r"/hello", HelloHandler),
]
app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()