import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup


url = input("Enter URL: ")
temp = urllib.request.Request(
        url,
        data=None,
        # disguise as google bot to download FT articles
        headers={
            'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html',
            'Referer': 'http://www.google.com/'
        })
response = urllib.request.urlopen(temp)
webContent = response.read()

f = open("website.html", 'wb')
f.write(webContent)
f.close

