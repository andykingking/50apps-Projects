import BeautifulSoup from BeautifulSoup
import urllib2

class PageSearch():
	def __init__(self, level, search_term, url):
		self.level = level
		self.search_term = search_term
		self.url = url
		self.text = urllib2.urlopen(url).read()
	def search():
		soup = BeautifulSoup(text)
		strings = soup.findAll(text=search_term)
		if len(strings) > 0:
			return True
		else:
			return False
	def find_links():
		soup = BeautifulSoup(text)
		anchors = soup.a
		return [PageSearch(level+1,search_term,a) for a in anchors]

class Search():
	pages_to_search = []
	searched_pages = []
	urls_found = []
	def __init__(self, search_term, initial_url):
		pages_to_search.append(PageSearch(1, search_term, initial_url))
	def run():
		while len(pages_to_search) > 0 && pages_to_search[0].level <= 5:
			if pages_to_search[0].search():
				urls_found.append(pages_to_search[0].url)
			pages_to_search.extend(a for a in pages_to_search[0].find_links() if a.url not in searched_pages)
			searched_pages.append(pages_to_search.pop([0]).url)

if __name___ == "__main__":
	s = Search()
	s.run()
	print s.urls_found
