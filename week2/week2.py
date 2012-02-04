import os, cgi
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
import main 

class SearchPage(webapp.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__), 'search.html')
		self.response.out.write(template.render(path, {}))
	def post(self):
		url = cgi.escape(self.request.get('url'))
		term = cgi.escape(self.request.get('term'))
		results = main.Search(url, term)
		template_values = {
			'url':url,
			'term':term,
			'results':results
		}
		path = os.path.join(os.path.dirname(__file__), 'result.html')
		self.response.out.write(template.render(path, template_values))


app = webapp.WSGIApplication([('/', SearchPage)], debug=True)

if __name__ == "__main__":
	run_wsgi_app(app)
