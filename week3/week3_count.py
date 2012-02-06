import sys, urllib2, string, re, json
from BeautifulSoup import BeautifulSoup, Comment

common = ['a','an','the','on','in','for','to']

def get_text(url):
	return urllib2.urlopen(url).read()

def wordify(in_string):
	words = re.sub(r'&.+;','',in_string)
	words = words.split(' ')
	words = map(lambda word: word.strip(string.punctuation+string.whitespace).lower(),words)
	words = filter(lambda word: word not in common and len(word) > 0,words)
	return words

def reduce_func(x,y):
	x.extend(y)
	return x

def parse_text(text):
	soup = BeautifulSoup(text)
	map(lambda tag: tag.extract(),soup.findAll({'script':True}))
	map(lambda tag: tag.extract(),soup.findAll(text=lambda x: isinstance(x, Comment)))
	words = filter(lambda x: len(x) > 0,map(wordify,soup.body(text=True)))
	words = reduce(reduce_func,words)
	return words

def jsonify(top10, longest, shortest):
	return json.dumps({'longest':longest, 'shortest':shortest, 'top10':top10}, indent=4)

def gen_stats(words):
	shortest = sorted(words,key=len)[0]
	longest = sorted(words,key=len,reverse=True)[0]
	words = list(set(zip(words,map(words.count,words))))
	return jsonify(sorted(words,key=lambda word: word[1], reverse=True)[:10], longest, shortest)

def get(url):
	return gen_stats(parse_text(get_text(url)))

if __name__ == "__main__":
	print get(sys.argv[1])

