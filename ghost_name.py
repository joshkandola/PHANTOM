import webapp2
import random

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Enter your name...</title></head>
            <body>
              <form action="/welcome" method="post">
                <input type="text" first name="my_first_name"><br>
                <input type="text" last name="my_last_name"><br>
                <input type="submit" value="Sign In">
              </form>
            </body>
            </html>""")


class Greeting(webapp2.RequestHandler):
    def post(self):
        a=["a","b","c"]
        x=random.randint(0,len(a))
        firstName = self.request.get("my_first_name")
        lastName = self.request.get("my_last_name")
        ghostName= firstName+a[x]+lastName
        a.pop(x)
        welcome_string = """<html><body>
                          Hi there, {}!
                          </body></html>""".format(ghostName)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(welcome_string)


routes = [('/', MainPage), ('/welcome', Greeting)]
my_app = webapp2.WSGIApplication(routes, debug=True)
