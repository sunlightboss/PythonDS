import json

with open('file.txt', 'w') as f:
    f.write('Hello ')

with open('file.txt', 'a') as f:
    f.write('My friend')

data = [{
    "name": "Aidana",
    "age": 19,
    "city": "Bishkek",
    "skills": ["Python", "Machine Learning", "Data Science"]
}]

# Creating a JSON file
with open('data.json', 'a') as json_file:
    json.dump(data, json_file, indent=4)
