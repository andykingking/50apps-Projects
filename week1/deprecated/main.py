from BeautifulSoup import BeautifulSoup
import urllib2, sys

class PageSearch():
	def __init__(self, level, search_term, url):
		self.level = level
		self.search_term = search_term
		self.url = url
		self.completed = False
		try:
			self.text = urllib2.urlopen(url).read()
		except:
			self.result = False
			self.completed = True
	def search(self):
		print "GET failed: " + str(self.completed)
		if self.completed == False:
			print "Searching " + self.url + " for " + self.search_term
			soup = BeautifulSoup(self.text)
			strings = soup.body.findAll(text=self.search_term)
			print strings
			if len(strings) > 0:
				self.result = True
			else:
				self.result = False
			self.completed = True
		print self.result
		return self.result
	def find_links(self):
		print "Finding links in " + self.url
		soup = BeautifulSoup(self.text)
		anchors = soup.findAll('a')
		for a in anchors:
			if getattr(s, 'href', None):
				a['href'] = a.url	
			if a['href'][0] == '/':
				a['href'] = self.url + a['href']
			if a['href'][0] == '#':
				a['href'] = self.url
			if a['href'][4] == 's':
				a['href'] = a['href'][:4] + a['href'][5:]
			print a
		return [PageSearch(self.level+1,self.search_term,a['href']) for a in anchors if not a['href'] == a.url]

class Search():
	def __init__(self, search_term, initial_url):
		self.pages_to_search = {}
		self.searched_pages = {}
		self.urls_found = {}
		self.pages_to_search.append(PageSearch(1, search_term, initial_url))
		
	def run(self):
		while len(self.pages_to_search) > 0 and self.pages_to_search[0].level <= 5:
			if self.pages_to_search[0].search():
				self.urls_found.append(self.pages_to_search[0].url)
			self.pages_to_search.extend(a for a in self.pages_to_search[0].find_links() if lambda x: x.url not in searched_pages[])
			self.searched_pages.append(self.pages_to_search.pop([0]))

if __name__ == "__main__":
	s = Search(sys.argv[1], sys.argv[2])
	s.run()
	print s.urls_found


