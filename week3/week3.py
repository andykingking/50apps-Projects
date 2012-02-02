import os
import webapp2
import jinja2
import week3-count

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class CountPage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('index.html')
		self.response.out.write(template.render({}))
	def post(self):
		# complete
		search = week1.Search()
		template = jinja_environment.get_template('')
		self.response.out.write(template.render({}))


app = webapp2.WSGIApplication([('/', CountPage)], debug=True)
