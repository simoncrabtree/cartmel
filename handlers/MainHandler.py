from google.appengine.ext import webapp
from google.appengine.api import users
import os
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            model = {'message':user.nickname()}
            path = os.path.join(os.path.dirname(__file__), '..', 'templates','main.html')
            self.response.out.write(template.render(path, model))
        else:
            self.redirect(users.create_login_url(self.request.uri))
