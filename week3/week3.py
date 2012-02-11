import os
import webapp2
import jinja2
import week3_count

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class CountPage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('index.html')
		self.response.out.write(template.render({}))

class Results(webapp2.RequestHandler):
	def post(self):
		url = self.request.body
		#url = 'http://www.cnn.com'
		self.response.out.write(week3_count.get(url))
		#self.response.out.write(url)

app = webapp2.WSGIApplication([('/', CountPage),
				('/results.json', Results)]
				, debug=True)
