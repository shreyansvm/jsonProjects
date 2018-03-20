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