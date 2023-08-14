NAMES = ["John", "Paul", "George", "Ringo"] # the variable names with strings as elements in the list data structure
AGES = [20, 21, 22, 23] # the variable ages with int as elements in the list data structure

JOHN = NAMES[0] # defining the variable John with indexed position 0 in the names list
PAUL = NAMES[1] # defining the variable Paul with indexed position 1 in the names list

JOHN_PAUL = NAMES[:2] # list slicing operation that extracts subset of elements up to (but not including) the lement indexed a OR elemnts at indices 0 and 1.
GEORGE_RINGO = NAMES[2:] # list slicing operation that extract subset of elements starting with element in indice 2 up until the end of the list.
REVERSE = NAMES[::-1] # list slicing operation that creates a new list with elements in reverse order from the original list
EVERY_OTHER = NAMES[::2] # creates a new list that includes every second element from the original listclear

print(sum(AGES)) # sum function returning sum of all ints in ages list
print(min(AGES)) # min function returning the minimum int element in the list
print(max(AGES)) # max function returning the max int elemnts in the list

print(JOHN_PAUL) 
print(GEORGE_RINGO)
print(REVERSE)
