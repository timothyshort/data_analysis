import time
import requests
from bs4 import BeautifulSoup


def continue_crawl(search_history, target_url, max_steps=25):
	if (search_history[-1] == target_url):
		print("Search History matches Target URL")
		return False
	if (len(search_history) >= max_steps):
		print("Search History reached maximum queries of " + max_steps)
		return False
	if (search_history[-1] in search_history[0:-2]):
		print("Search History has reached a cycle")
		return False
	return True

def find_first_link(url):
	# get the HTML from "url", use the requests library
	response = requests.get(url)
	html_contents = response.text

	# feed the HTML into Beautiful Soup
	soup = BeautifulSoup(html_contents, 'html.parser')

	# find the first link in the article
	# 1. go to the article text
	article_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
	# 2. go into paragraph
	for element in article_div.find_all("p", recursive=False):
		# 3. find an a tag that is a direct child of the p tag
		if element.find("a", recursive=False):
			link = element.find("a", recursive=False).get('href')
			print("  >> ARTICLE: " + link[6:])
			return "https://en.wikipedia.org" + link
	return None


start = input("Enter the starting article: ")
home_url = 'https://en.wikipedia.org/wiki/' + start

target = input("Enter the target article: ")
target_url = 'https://en.wikipedia.org/wiki/' + target

article_chain = [home_url]

print("Performing web crawler from {} to {}".format(home_url, target_url))

while continue_crawl(article_chain, target_url, 10):
	print("LINK: " + article_chain[-1])

	# download html of last article in article_chain
	response = requests.get(target_url)

	# find the first link in that html
	first_link = find_first_link(article_chain[-1])

	# add the first link to article_chain
	article_chain.append(first_link)

	# delay for about two seconds
	time.sleep(2)

