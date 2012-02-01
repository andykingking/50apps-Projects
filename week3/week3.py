import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import week3-count

class CountPage(webapp.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__), 'index.html')
		self.response.out.write(template.render(path, {}))
	def post(self):
		# complete
		search = week1.Search()
		path = os.path.join(os.path.dirname(__file__),'' )
		self.response.out.write(template.render(path, {}))


app = webapp.WSGIApplication([('/', CountPage)], debug=True)

if __name__ == "__main__":
	run_wsgi_app(app)
