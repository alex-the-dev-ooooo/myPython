# Import JSON module
import json

#import REST API library
import requests

#just so our dictionaries look pretty
import pprint

#USE json.dumps() TO CONVERT DATA TO A STRING OF A JSON OBJECT
#AND json.loads() TO CREATE A JSON OBJECT.

# Array of JSON Pokemon - type is a list of dict objects.
pokemon = [{"name": "Eevee", "type": "Normal", "level": 10},
            {"name": "Charizard", "type": "Fire", "level": 80},
            {"name": "Pikachu", "type": "Electric", "level": 70}]

print('Type of pokemon is ' + str(type(pokemon)))

# Read & print original data
print("The original data:\n{0}".format(pokemon))
print('\n')

# Convert to JSON object after sorting
sorted_json_str = json.dumps(pokemon, sort_keys=True) #Creates a string
print('Type of sorted_json_str is ' + str(type(sorted_json_str)))

sorted_json_obj = json.loads(sorted_json_str) #Creates a list
print('Type of data is ' + str(type(sorted_json_obj)))

# Print sorted JSON
print("The sorted JSON data based on the keys:\n{0}".format(sorted_json_str))
print('\n')

# Sort JSON data based on the value of 'type' key
pokemon.sort(key=lambda x: (x["type"]==None, x["type"]))

# Print sorted JSON
print("The sorted JSON data based on the value of the type:\n{0}".format(pokemon))
print('\n')

#Now we move on to REST API practice

#-----------------------------------------------------------------#

#Example of using query parameters.
query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print('Initial, untouched data: ' + response.text)

json_data = json.loads(response.text) #Creates a json object from the http request - a dict
response_list = json_data["response"] #Grab only the "response" subset of the json, so that we can sort based on duration.

# Sort response data based on the value of 'duration' key, and then assign the original json's 'response' list to the sorted list we just created
response_list.sort(key=lambda x: (x["duration"]==None, x["duration"]))
json_data["response"] = response_list
print('Data after response has been sorted ascending on duration: ')
pprint.pprint(json_data)

#turning it back into a string for practice
json_string = json.dumps(json_data)

#Accessing REST headers
print('The date: ' + response.headers["date"]) 

