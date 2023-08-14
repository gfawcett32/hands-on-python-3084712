greet = "Hello World" #variable
extened_grt = "Hello World, " + "this is a long string" #variable

name = "John" #variable

intrupution = f"Hello {name}" #string interpolation where name variable is embedded in the string

greet_format = "Hello {}"

formatted = greet_format.format(name) #a method for the specific name argument embedded

print(intrupution, formatted)

print(formatted.upper()) # the upper method to change the strings to all upper case
print(formatted.lower()) # the lower method to change the strings to all lower case
print(formatted.replace("John", "Paul")) # the replace method to change the name variable string from Jong to Pual

# the purpose of this program is to illustrate the difference between string interpolation for formatting 
# and the use of the format method to insert arguments into strings
# as well, to demonstrate other string-specific builtin methods for string manipulation