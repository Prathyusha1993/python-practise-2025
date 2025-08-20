import json

# this is json string
json_string = '{"name": "John", "age": 30, "city": "New York"}'
# this is used to parse the api response
# convert json string to python dictionary
data = json.loads(json_string)
print(data)
print(data['name'])


# json dump is used to convert python dictionary into json string
# dumps means dump string
# this is used for sending json data to an api or saving it to a file
person = {'name': 'Alice', 'age': 30, 'city': 'San Francisco', 'gender': 'male'}
json_string_data = json.dumps(person)
print(json_string_data)
