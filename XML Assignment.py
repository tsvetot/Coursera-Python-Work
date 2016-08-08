import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_296834.xml'

data = urllib.urlopen(serviceurl).read()

tree = ET.fromstring(data)

counts = tree.findall('.//count')

total = 0

for count in counts:
    total += int(count.text)
    
print 'total: ', total


