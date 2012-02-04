from BeautifulSoup import BeautifulSoup
import re, urllib2, sys

def good_url():
	return # True if good url, False if not
	# i need to make a way to validate urls to follow

def get_text(url):
	return urllib2.urlopen(url).read()

def make_search_func(name_value, text_value):
	return lambda x: x.findAll(name=name_value,text=text_value)

def is_search_term_present(url, term):
	return make_search_func(True, re.compile(term))(BeautifulSoup(get_text(url)))

def get_anchors(url):
	anchors = make_search_func('a', True)(BeautifulSoup(get_text(url)))
	return [anchor for anchor in anchors if lambda x: good_url(x)]

def process_page(url, term):
	return (is_search_term_present(url, term), get_anchors(url))	

def search(seed_url, term):
	urls_to_search = [seed_url]
	searched = {}	
	for i in range(5):
		for url in urls_to_search:
			if searched[url] == None:
				page = process_page(url, term)
				urls_to_search.remove(url)
				searched[url] = page+(i+1,)
				urls_to_search.extend([a['href'] for a in page[1]])
	return [search for search in searched if search[1] != None]

if __name__ == "__main__":
	print search(sys.argv[1],sys.argv[2])
