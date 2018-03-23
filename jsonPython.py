'''
Simple example on use of JSON.
'''
import json

print "Hello JSON"

print "------------ JSON to Python --------------"
jsonData = '{"name": "Frank", "age": 39}'
jsonToPython = json.loads(jsonData)
print jsonToPython
print jsonToPython['name']


print "------------ Python to JSON --------------"
pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
dictionaryToJson = json.dumps(pythonDictionary)
print dictionaryToJson

print "------------ Reading a JSON file JSON to python --------------"
jsonFile = open('sampleData.json','r')
jsonFileData = json.load(jsonFile)
print jsonFileData
print jsonFileData['office']
print jsonFileData['office']['medical']
print jsonFileData['office']['medical'][0]
print jsonFileData['office']['medical'][1]
print jsonFileData['office']['medical'][1]['room-number']

print "------------ Reading a webpage using JSON --------------"
import urllib2, urllib, json
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select wind from weather.forecast where woeid=2460286"
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
print yql_url
result = urllib2.urlopen(yql_url).read()
data = json.loads(result)
print data
print data['query']['results']

print "------------ Reading a webpage using JSON --------------"

import urllib2
import json
req = urllib2.Request("http://vimeo.com/api/v2/video/260920165.json")
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())
print json
print json[0]['title']