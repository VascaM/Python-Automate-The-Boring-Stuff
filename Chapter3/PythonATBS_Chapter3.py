import random,pyperclip


# Importing Modules
print ('Import the random module with: import random. Use random.randint(1,20) to  get a random  number like:')
print (random.randint(1,20))



# Use of a function
print ('This function adds +1 to a given number. In this case the input is 5 so the output is:')
def plusOne(number):
    return number + 1
newNumber =  plusOne(5)
print(newNumber)



# Return Values and return Statements
print ('This functions returns a different string depending on what number it is passed as an argument.') 
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Computer gaf 1'
    elif answerNumber == 2:
        return 'Computer gaf 2'
    elif answerNumber == 3:
        return 'Computer gaf 3'

r = random.randint(1, 3)
fortune = getAnswer(r)
print(fortune)



# Local and Global Scope
print ('Global vs local scope') 
def spam():
    global eggs
    eggs = 'Global' # this is the global
def bacon():
    eggs = 'Local' # this is a local
def ham():
    print(eggs) # this is the global
eggs = 42 # this is the global
bacon()
#If you called the function spam, the answer would be "Global"
print(eggs)



# Use the pyperclip module
print ('I coppied something to your clipboard')
pyperclip.copy('exit')



# Ending a Program Early with the sys.exit() function + try and except statement
try:
    print('Type exit to exit. Or copy paste.')
    response = input()
    if response == 'exit':
        sys.exit('You exited the program')
    else:
        print('You did not type exit')
except NameError:
    print('name -sys- is not defined')
