import json

'''# converting from python to json 

# A python object (dict)
x = {
	"name": "James",
	"age": 30,
	"city": "Los Angeles"
}

#  Convert into JSON
y = json.dumps(x)
# print(x)
# print(y)'''

'''# converting From JSON to python
# Some JSON
a = '{ "name":"James, "age":30, "city":"New York"}'

# Parse - the conversion
b = json.loads(a)

print(b["age"]) '''

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
