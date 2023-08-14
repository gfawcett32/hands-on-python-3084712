import csv
import json # built-in module for working with JavaScript Object Notation which allows for encoding python data structures as JSON strongs and decoding JSON strongs back into Python data structures.
from pprint import pprint

EINSTEIN = { # the dictionary is again defined
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN) # stands for JSON DUMP string and is used to encode (serialize) Python objects into a JSON formatted string. In this case, the Einstein Dict strucutre.
back_to_dict = json.loads(einstein_json) # stands for JSON load string and is used to decode (deserialize) a JSON string and convert it into a python object. Decoding the dict make into a dict structure.
print(einstein_json) # the print functions will show a comparison of the data structures.
pprint(back_to_dict)

#the context manager creating a list of dictionaries
with open("Ex_Files/03_03_begin/laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

#a context manager that writes the laureate list of dictionaries into a json file with formatted indentation.
with open("Ex_Files/03_03_begin/laureates.csv", "w") as f:
    json.dump(laureates, f, indent=2) # f is the file-like object where the JSON data will be written. Indent=2 argument specifies that the JSON data should be formatted with an indentation of 2 spaces for readability. 
    #json.dump function is used to serialize a Python object and write it directly to a file-like object (such as a giled opened in write mode)