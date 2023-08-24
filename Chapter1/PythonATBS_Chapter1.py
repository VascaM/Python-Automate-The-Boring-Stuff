# Expressions in interactive  shell
print ('3 + 2 = ' + str(3+2))

print ('Alice' * 3)
print('\n')


# Changing varibale
spam = 40
eggs = 2
print('spam = 40 and eggs = 2')
print ('spam + eggs = ' + str(spam + eggs))

spam = 60
print('spam is now 60')
print ('spam + eggs = ' + str(spam + eggs))
print('\n')


# Hello worlld exercise
print('Hello, world!')
print('What is your name?')
userName = input()
print('Hello, ' + userName)
print('The length of your name is:')
print(len(userName))
print('What is your age?')
userAge = input()
print('You will be ' + str(int(userAge) + 1) + ' in a year.')
print('\n')


# Convert data types
print ("int('99.99') will give you an error. But int('99') =")
print (int('99'))
print('\n')


# Assignment statement
bacon = 20
print ('bacon = 20', end='\n')
print ('bacon + 1')
print (bacon)
print ('The +1 expression does not  reassign the value  in bacon. You must use: bacon = bacon + 1') 
