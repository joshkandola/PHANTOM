import webapp2
import random


ghostList=["a","b","c","d"]
nameList=[]

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
                <input type="submit" value="Choose Name">
                <p>nameList<p>
              </form>
            </body>
            </html>""")


class Greeting(webapp2.RequestHandler):
    def post(self,a):
        xlist=[random.randint(0,len(ghostList))]*3
        firstName = self.request.get("my_first_name")
        lastName = self.request.get("my_last_name")
        ghostName0= firstName+ghostList[xlist[0]]+lastName
        ghostName1= firstName+ghostList[xlist[1]]+lastName
        ghostName2= firstName+ghostList[xlist[2]]+lastName
        name_buttons = """<html><body>
                          <button name=ghostName0 type="submit" value="HTML">HTML</button>
                          <button name=ghostName1 type="submit" value="HTML">HTML</button>
                          <button name=ghostName2 type="submit" value="HTML">HTML</button>
                          </body></html>"""
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(welcome_string)


routes = [('/', MainPage), ('/welcome', Greeting)]
my_app = webapp2.WSGIApplication(routes, debug=True)
