NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0 # intiaitlize the while loop variable
while i < len(NAMES): # the condition is true while 1 is less than # of elements in the names list 
    print(NAMES[i], AGES[i]) # print the current index of i in both names and ages list
    i += 1 # take current value of the loop and add 1 until condition is false

for name in NAMES: # print the current index of i in names list
    print(name)

for name, age in zip(NAMES, AGES):# this code does the same thing as the while loop 
    # but uses the for loop to iterate and zip method which combine elements from multiple lists into pairs.
    print(f"{name} {age}") #here the f-string literal (notation used to represent a fixed value in source code) to print out each pair from the for loop.

for name in reversed(NAMES): #using the reserve method in a for loop to iterate through the list and reverse the positions of the elements
    print(name)

for i in range(5): # setting the i variable in the for loop then iterating over a range of 5 numbers produced by the range function, in this case 0-4.
    print(i)

# enumerate
for i, name in enumerate(NAMES): # set i and name variable in for loop then use enumerate method to iterate over elements in names list, keeping track of indices and elements. 
    print(f"{i} {name}") # print the results of the enumerate method 

