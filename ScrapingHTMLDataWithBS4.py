import bs4
import urllib2
import re
from bs4 import BeautifulSoup
page = urllib2.urlopen("http://python-data.dr-chuck.net/comments_296837.html")
soup = BeautifulSoup(page, "html.parser")

spans = soup('span')

numbers = []
for span in spans:
   numbers.append(int(span.string))

print sum(numbers)

