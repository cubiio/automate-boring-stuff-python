#! /usr/bin/env python3
# lucky.py - opens several search engine results

import requests
import sys
# import webbrowser
import bs4


print('DuckDuckGoing...')  # display text while downloading search results
res = requests.get('https://duckduckgo.com/html/?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result
# Note, this only returns only top body info
# Scraping against ToS so no search results found, even if select() amended
# eg ('.r a') for Google
# eg ('.result__url a') for DuckDuckGo
# linkElems = soup.select('body a')
linkElems = soup.select('a[href]')
print(linkElems)

# Open first five results or all results, whichever is smallest
# numOpen = min(5, len(linkElems))

# for i in range(numOpen):
#     webbrowser.open('https://duckduckgo.com/?q=' + linkElems[i].get('href'))
