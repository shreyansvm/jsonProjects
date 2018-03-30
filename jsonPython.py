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

print "------------ Posting HTTP request on MOCKBIN --------------"
import requests

url = "https://requestloggerbin.herokuapp.com/bin/2d892377-0f30-4125-86b8-1967853f236a"

querystring = {"foo":["bar","baz"]}

payload = "foo=bar&bar=baz"
headers = {
    'cookie': "foo=bar; bar=baz",
    'accept': "application/json",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)

print "------------ Reading HTTP posts from MOCKBIN --------------"
import json
#queryUrl = 'https://requestloggerbin.herokuapp.com/bin/<id>/log'
queryUrl = 'https://requestloggerbin.herokuapp.com/bin/2d892377-0f30-4125-86b8-1967853f236a/log'

result = urllib2.urlopen(queryUrl).read()
file = open('testJson2.json','w')
file.write(result)
file.close()
with open('testJson2.json') as data_file:
    mockbinData = json.load(data_file)

print mockbinData
print mockbinData['log']
print mockbinData['log']['entries']
print mockbinData['log']['entries'][0]
print mockbinData['log']['entries'][0]['request']
print mockbinData['log']['entries'][0]['startedDateTime']
print mockbinData['log']['entries'][0]['clientIPAddress']
print mockbinData['log']['entries'][0]['request']['postData']

for entry in mockbinData['log']['entries']:
    print entry['clientIPAddress']
    print entry['startedDateTime']
    print entry['request']['method']
    print entry['request']['postData']
    print entry['request']['postData']['params']
    for param in entry['request']['postData']['params']:
        print param

# with open('testJson.json') as data_file:
#     data = json.load(data_file)
# print data
# print data['log']