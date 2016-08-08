import urllib2
import ssl
import bs4
from bs4 import BeautifulSoup


#url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://python-data.dr-chuck.net/known_by_Thumbiko.html'
#position=3
#repeat = 4

position = 18
repeat = 7

#position = 18
#count = 7


for i in range(repeat+1):
    print("Retrieving :",url)
    data=urllib2.urlopen(url).read()
    soup = BeautifulSoup(data,"html.parser")
    tags = [tag.get('href',None) for tag in soup('a')]
    url = tags[position-1]

