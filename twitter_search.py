import sys 
import urllib
import json 

def search_twitter(query='python'):
	url = 'http://search.twitter.com/search.json?q=' + query
	response = urllib.urlopen(url).read()
	data = json.loads(response)
	return data['results']

def print_tweets(tweets):
	for tweet in tweets:
		print tweet['from_user'] + ': ' + tweet['text'] + '\n'
		
if __name__ == "__main__":
	query = sys.argv[1]
	results = search_twitter(query)
	print_tweets(results) 