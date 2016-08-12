import urllib2
import json
serviceurl = 'http://python-data.dr-chuck.net/geojson?'
place = "Nagpur University"
url = serviceurl + urllib2.urlencode({'sensor':'false', 'address': place})
data = urllib2.urlopen(url).read()
js = json.loads(data)
print "Place id", js['results'][0]['place_id']