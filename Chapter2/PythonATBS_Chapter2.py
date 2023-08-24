# Boolean Operators
print ('(4 < 5) and (5 < 6) = true')
print ('(1 == 2) or (2 == 2) = true')
print ('(2 + 2 == 4) and not (2 + 2 == 5) = true')
print(' ')

# Blocks of code
name = 'Kim'
password = '1234'
if name == 'Kim':
    print('Hello, Kim')
if password == 'Kim':
    print('Access granted.')
else:
    print('Wrong password.')
print(' ')

# If, elif, else
print('What number is spam?')

spam = int(input())

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
print('Important! : Input() saves your input as a string. You have to first convert your input to an integer.')
print(' ')

#For loop
print ('The next lines prints the numbers 1 to 10 using a for loop and a while loop.')
for i in range(1,11):
    print(i)

#While loop
a = 1
while a <= 10:
    print(a)
    a+=1
