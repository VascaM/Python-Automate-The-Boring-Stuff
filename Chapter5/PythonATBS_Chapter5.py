# The Dictionary Data Type
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print (myCat['size'])

# Dictionaries vs. Lists
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print (spam == bacon) #List

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print (eggs == ham) #Dictionarie

# The keys(), values(), and items() Methods
spam = {'color': 'red', 'age': 42}
for k in spam.keys():       
    print(k)                

for v in spam.values(): 
    print(v)

for i in spam.items():
    print(i)                # prints tule

print (list(spam.keys()))   # prints lists

for k, v in spam.items():
   # multiple assignment trick
    print('Key: ' + k + ' Value: ' + str(v))


# Checking Whether a Key or Value Exists in a Dictionary
spam = {'name': 'Zophie', 'age': 7}
   
print ('name' in spam.keys())	    #True
print ('Zophie' in spam.values())   #True
print ('color' in spam.keys())      #False
print ('color' not in spam.keys())  #True
print  ('color' in spam)            #False

# The get() Method
picnicItems = {'apples': 5, 'cups': 2}
print ('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print ('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# The setdefault() Method
spam = {'name': 'Pooka', 'age': 5}
print (spam.setdefault('color', 'black'))
print (spam.setdefault('color', 'white'))

# Pretty Printing
import pprint

count = {' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2,
'i': 6, 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}

pprint.pprint(count)
print(pprint.pformat(count))





