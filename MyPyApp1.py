# Import JSON module
import json
import requests

# Array of JSON Pokemon
pokemon = [{"name": "Eevee", "type": "Normal", "level": 10},
            {"name": "Charizard", "type": "Fire", "level": 80},
            {"name": "Pikachu", "type": "Electric", "level": 70}]

# Read and print the original data
print("The original data:\n{0}".format(pokemon))
print('\n')

# Convert into the JSON object after sorting
sorted_json_data = json.dumps(pokemon, sort_keys=True)

# Print sorted JSON data
print("The sorted JSON data based on the keys:\n{0}".format(sorted_json_data))
print('\n')

# Sort the JSON data based on the value of the type key
pokemon.sort(key=lambda x: x["type"])

# Print sorted JSON data
print("The sorted JSON data based on the value of the type:\n{0}".format(pokemon))
print('\n')

response = requests.get("http://api.open-notify.org/astros.json")
print(response)
print("test")