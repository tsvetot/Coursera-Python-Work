import urllib2
import json
serviceurl = 'http://python-data.dr-chuck.net/comments_296838.json'

connection = urllib2.urlopen(serviceurl)
data = connection.read()
parsed_data = json.loads(data)
counts = []

comments = parsed_data["comments"]

for comment in comments:
    counts.append(comment['count'])

print "Count: {0}".format(len(counts))
print "Sum: {0}".format(sum(counts))
