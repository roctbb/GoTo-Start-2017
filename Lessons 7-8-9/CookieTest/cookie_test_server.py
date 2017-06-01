import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_cookie("person"):
            self.write("<form method='post'>"
                       "<h3>Ваш любимый персонаж:</h3>"
                       "<select name='person'>"
                       "<option value='Lupa'>Лупа</option>"
                       "<option value='Pupa'>Пупа</option>"
                       "<option value='petrovich'>Петрович</option>"
                       "<option value='pig'>Свинья</option>"
                       "</select>"
                       "<input type='submit' />"
                       "</form>")
        else:
            self.write("Ваш любимый персонаж - {0}".format(self.get_cookie("person")))
    def post(self):
        person = self.get_argument("person")
        print(person)
        self.set_cookie("person", person)
        self.write("Спасибо за ответ!")

class SecureHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("password"):
            self.write("<form method='post'>"
                       "<h3>Ваш пароль:</h3>"
                       "<input type='password' name='password'/>"
                       "<input type='submit' />"
                       "</form>")
        else:
            self.write("Привет, {0}".format(self.get_secure_cookie("password")))
    def post(self):
        password = self.get_argument("password")
        if (password=="123456"):
            self.set_secure_cookie("password", "John")
            self.write("Вы вошли!")

        else:
            self.write("Неправильный пароль!")

routes = [
    (r"/", MainHandler),
    (r"/admin", SecureHandler),
]
app = tornado.web.Application(routes, debug=True, cookie_secret="myCookieSecret")
app.listen(8888)
tornado.ioloop.IOLoop.current().start()[[]]