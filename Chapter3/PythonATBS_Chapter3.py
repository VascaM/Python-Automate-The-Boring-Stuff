import random,sys,pyperclip

print ('Import the random module with: import random. Use random.randint(1,20) to  get a random  number like:')
print (random.randint(1,20))

print ('I coppied something to your clipboard')
pyperclip.copy('Hoi Tessa')


print('Type exit to exit.')
response = input()
if response == 'exit':
    sys.exit()

def plusOne(number):
    return number + 1
newNumber =  plusOne(5)
print(newNumber)
