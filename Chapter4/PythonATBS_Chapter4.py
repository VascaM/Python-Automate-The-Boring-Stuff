# /// Chapter 4 Lists

# Getting individual values in a list with indexes
spam = ['cat', 'bat', 'rat', 'elephant']
print ('The ' + spam[1] + ' ate the ' + spam[0] + '.')

# Getting values of in a list inside a list with multiple indexes
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print (spam[1][4])

# Negative indexes
spam = ['cat', 'bat', 'rat', 'elephant']
print ('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')

# Getting a List from another list with slices
spam = ['cat', 'bat', 'rat', 'elephant']
print (spam[1:3])

# Getting a list’s length with the len() function
spam = ['cat', 'dog', 'moose']
print (len(spam))

# Changing values in a list with indexes
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
print(spam)

# List concatenation and list replication
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

# Removing values from lists with del statements
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)

# Using for Loops with Lists
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# The list() function
print (list(range(0,10,2)))

# The in and not in Operators
spam = ['hello', 'hi', 'howdy', 'heyas']		
if 'cat' not in spam:
    print('Cat is not in spam')

# The Multiple Assignment Trick
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print (color)

# Using the enumerate() Function with Lists
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# Using the random.choice() and random.shuffle() Functions with Lists
import random
pets = ['Dog', 'Cat', 'Moose']
print (random.choice(pets)
)

people = ['Alice', 'Bob', 'Carol', 'David']
print (random.shuffle(people))

# Augmented Assignment Operators
spam = 42
spam += 1
print (spam)


