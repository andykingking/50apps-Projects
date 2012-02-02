import sys
import urllib2
from BeautifulSoup import BeautifulSoup
import string

common = ['a','an','the','on','in','for','to']

def get_text(url):
	return urllib2.urlopen(url).read()

def wordify(in_string):
	words = in_string.split(' ')
	words = [word.strip(string.punctuation.replace('\'','')+string.whitespace).lower() for word in words]
	words = [word for word in words if len(word) > 0]
	return words

def reduce_func(x,y):
	x.extend(y)
	return x

def parse_text(text):
	soup = BeautifulSoup(text)
	[tag.extract() for tag in soup.findAll({'script':True})]
	words = filter(lambda x: len(x) > 0,[wordify(s) for s in soup.body(text=True)])
	words = reduce(reduce_func,words)
	return words

def jsonify(top10, longest, shortest):
	pass

def gen_stats(words):
	

if __name__ == "__main__":
	print parse_text(get_text(sys.argv[1]))

