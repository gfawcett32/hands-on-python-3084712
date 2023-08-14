import csv
from datetime import datetime # a standard library that provides classes for working with dates and times. 
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}
# below is the same context manager construct which is creating a list of dictionaries. Not that this is unrelated to the dict data structure
with open("/workspaces/hands-on-python-3084712/Ex_Files/03_02_begin/laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        print("============")
        year_date = datetime.strptime(laureate["year"], "%Y") # year laureate won. strptime method (string parse time) is used to convert a strong representation for a date and time into a 'datetime' object.
        born_date = datetime.strptime(laureate["born"], "%Y-%m-%d") #DOB of winning laureate
        print("age", year_date.year - born_date.year) # output is how old the laureate winner is the year he won
        break
