from BeautifulSoup import BeautifulSoup
import re, urllib2, sys

def good_url(url):
	print "testing", url
	return False if re.search('http://.+',url) == None else True

def fix_url(seed, url):
	print "fixing", url
	if len(url) == 0:
		return '#'
	elif url[0] == '/':
		if seed[-1] != '/':
			return seed + url
		else:
			return seed[:-1] + url
	elif url[:5] == 'https':
		return url.replace('https','http',1)
	elif good_url(url) == True:
		return url
	else:
		return '#'

def get_text(url):
	print "getting text for", url
	return urllib2.urlopen(url).read()

def make_search_func(name_value, text_value):
	print "making search func for text value:", text_value
	return lambda x: x.findAll(name=name_value,text=text_value)

def is_search_term_present(url, term):
	print "searching for term:", term, url
	try:
		search = make_search_func(True, re.compile(term))(BeautifulSoup(get_text(url)))
	except:
		search = []
	return True if len(search) > 0 else False

def get_anchors(url):
	print "getting anchors for ", url
	anchors = make_search_func('a', None)(BeautifulSoup(get_text(url)))
	# start of issue
	print "start of issue len:", len(anchors)
	anchors = [anchor['href'] for anchor in anchors if anchor.has_key('href')]
	print "end of issue len:", len(anchors)
	# end of issue
	anchors = [fix_url(url, anchor) for anchor in anchors]
	return [anchor for anchor in anchors if lambda x: good_url(x) == True]

def process_page(url, term):
	print "processing:", url
	return (is_search_term_present(url, term), get_anchors(url))	

def search(seed_url, term):
	urls_to_search = set([seed_url])
	add_to_urls_to_search = set()
	remove_from_urls_to_search = set()
	searched = {}	
	for i in range(5):
		for url in urls_to_search:
			if searched.has_key(url) == False:
				page = process_page(url, term)
				print "page: ", url, page
				remove_from_urls_to_search.add(url)
				searched[url] = (page[0],)+(i+1,)
				add_to_urls_to_search.update(page[1])
		urls_to_search.update(add_to_urls_to_search)
		urls_to_search.difference_update(remove_from_urls_to_search)
		print "urls_to_search: ", urls_to_search
		print "searched: ", searched
	return [search for search in searched if searched[search][1] == True]

if __name__ == "__main__":
	print search(sys.argv[1],sys.argv[2])
