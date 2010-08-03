from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from handlers.MainHandler import *


def main():
    application = webapp.WSGIApplication([
#        ('/Task/CreateTask', CreateNewTaskHandler),
#        ('/Task/Delete', DeleteTaskHandler),
#        ('/Task/GetUpdates', UpdatedTasksHandler),
        ('/', MainHandler)],
        debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()

