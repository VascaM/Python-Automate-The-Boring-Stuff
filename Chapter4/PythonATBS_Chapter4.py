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
print (random.choice(pets))

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)

# Augmented Assignment Operators
spam = 42
spam += 1
print (spam)

# Finding a Value in a List with the index() Method
spam = ['hello', 'hi', 'howdy', 'heyas']
print (spam.index('hello'))

# Adding Values to Lists with the append() and insert() Methods
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print (spam)
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print (spam)

# Removing Values from Lists with the remove() Method
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print (spam)

# Sorting the Values in a List with the sort() Method
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print (spam)

# Reversing the Values in a List with the reverse() Method
spam = ['cat', 'dog', 'moose']
spam.reverse()
print (spam)

# Mutate mutable Data Types with append() Method
eggs = [1, 2]
del eggs[1]
del eggs[0]
eggs.append(3)
eggs.append(4)
print (eggs)

# Mutate immutable Data Types by copying from parts
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
name = 'Zophie a cat'
print (newName)

# The Tuple Data Type
eggs = ('hello', 42, 0.5) #() instead of [], tuples are immutable

# Converting Types with the list() and tuple() Functions
print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
print(list('hello'))

# References
spam = 42
cheese = spam
spam = 100
print (spam)
print (cheese)

spam = [0, 1, 2, 3, 4, 5]
cheese = spam 		    # The reference is being copied, not the list
cheese[1] = 'Hello!' 	    # This changes the list value
print (spam)
print (cheese)  	    # The cheese variable refers to the same list

# id() Function
print (id('Howdy'))

# Passing References
def eggs(cheese):
    cheese.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam)
                #  Cheese gets destroyed, but it made changes to the same list spam refers to

# The copy Module’s copy() Function
import copy 
spam = ['A', 'B', 'C', 'D']
id(spam)								
cheese = copy.copy(spam)
id(cheese)                  # cheese is a different list with different identity.	
cheese[1] = 42
print (spam)
print (cheese)						    

