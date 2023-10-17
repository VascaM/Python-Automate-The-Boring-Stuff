# Escape Characters
print('Add a single quote here: Bob\'s.')
print('Add a tab \t here.')
print('Add a newline \n here.')

# Raw strings
print(r'That is Carol\'s cat.')

# Multiline Strings with Triple Quotes
print('''Dear Reader,

This is a mulitiline string writtenn with triple Quotes.

Sincerely,
Bob''')

# Multiline Comments
"""This is a Python program that uses info from:
Automate the boring stuff chapter 6.
"""

# Indexing and Slicing Strings
spam = 'Hello, world!'
print (spam[4])
print (spam[0:5])

# The in and not in Operators with Strings
print ('Hello' in 'Hello, World')
print ('' not in 'beeb')

# Putting Strings Inside Other Strings
name = 'Unknown'
age = 25
print ('My name is %s. I am %s years old.' % (name, age))
print (f'My name is {name}. Next year I will be {age + 1}.')

# The upper(), lower(), isupper(), and islower() Methods
spam = 'Hello, world!'
spam = spam.upper()
print (spam)

spam = 'Hello, world!'
print(spam.islower())       #False
print(spam.isupper())       #False
print('HELLO'.isupper())    #True
print('abc12345'.islower()) #True
print('12345'.islower())    #False
print('2345'.isupper())     #False

# The isX() Methods
print('hello'.isalpha())                    #True
print('hello'.isalnum())                    #True
print('123'.isdecimal())                    #True
print('    '.isspace())                     #True
print('This Is Title Case 123'.istitle())   #True

# The startswith() and endswith() Methods
print('Hello, world!'.startswith('Hello'))	    	#True
print('abc123'.endswith('12'))			        #False
print('Hello, world!'.startswith('Hello, world!'))	#True
print('Hello, world!'.endswith('Hello, world!'))	#True

# The join() and split() Methods
print('ABC'.join(['My', 'name', 'is', 'Simon'])	)
print ('My name is Simon'.split('m'))

# Splitting Strings with the partition() Method
print('Hello, world!'.partition('world'))
print('Hello, world!'.partition('o'))
print('Hello, world!'.partition('XYZ'))

# Justifying Text with the rjust(), ljust(), and center() Methods
print('Hello'.rjust(10, '*'))
print('Hello'.ljust(10, '-'))
print('Hello'.center(10, '='))

# Removing Whitespace with the strip(), rstrip(), and lstrip() Methods
spam = '    Hello, World    '
print(spam.rstrip())
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

# Numeric Values of Characters with the ord() and chr() Functions
print(ord('A'))
print(chr(65))
print(ord('B'))
print(ord('A') < ord('B'))
print(chr(ord('A') + 1))
