import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Enter your name...</title></head>
            <body>
              <form action="/welcome" method="post">
                <input type="text" name="my_name"><br>
                <input type="submit" value="Sign In">
              </form>
            </body>
            </html>""")


class Greeting(webapp2.RequestHandler):
    def post(self):
        a=["a","b","c"]
        username = self.request.get("my_name")
        ghostName= username+a[0]
        welcome_string = """<html><body>
                          Hi there, {}!
                          </body></html>""".format(ghostName)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(welcome_string)


routes = [('/', MainPage), ('/welcome', Greeting)]
my_app = webapp2.WSGIApplication(routes, debug=True)