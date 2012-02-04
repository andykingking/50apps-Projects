import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import week1

class SearchPage(webapp.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__), 'search.html')
		self.response.out.write(template.render(path, {}))
	def post(self):
		# add and complete when week1 is done
		search = week1.Search()
		path = os.path.join(os.path.dirname(__file__), 'result.html')
		self.response.out.write(template.render(path, {}))


app = webapp.WSGIApplication([('/', SearchPage)], debug=True)

if __name__ == "__main__":
	run_wsgi_app(app)
