# Chapter 4 Lists

# Getting individual values in a list with indexes
spam = ['cat', 'bat', 'rat', 'elephant']
print ('The ' + spam[1] + ' ate the ' + spam[0] + '.')

# Getting values of in a list inside a list with  multiple indexes
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


