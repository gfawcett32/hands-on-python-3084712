import csv # functionality from Python's standard library for working with CSV files.
from pprint import pprint # pretty-print is a standard python module that allows for printing of data strucutres in a well-formatted and visually appealing manner.

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'
# defining a csv variable in string format
EINSTEIN = { # defining a dictionary 
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

with open("Ex_Files/03_01_begin/laureates.csv", "r") as f: #opens function opens the file named lauretes.csv in read mode "r" using with as a context manage that ensures the file is properly closed after the specific block of code is executed.
    reader = csv.DictReader(f) #the reader variable is set as the csv.DictReader class and passed the argument f which instantiates the class. The DictReader will then open and read laureates csv file and create a dictionary where the keys are the coumn headers and the values are the corresponding values from the row. 
    laureates = list(reader) # this lines reads all the rows form the CSV file using the reader object and converts them into a list of dictionaries. 

for laureate in laureates: # defining f loop variable laureate in laureates generated list
    if laureate["surname"] == "Einstein": # in reference to the laureate dictionary, the ["surname"] brackets are used to access the specific item in the dictionary
        pprint(laureate)
        break
