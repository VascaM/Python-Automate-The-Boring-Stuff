def collatz(number):
    while number != 1:          # While Loop repeats until number = 1
        if number % 2 == 0: 
            number = number // 2        # Update the number parameter
            print(number)

        elif number % 2 == 1:
            number = number * 3 + 1     # Update the number parameter
            print(number)

try:
    num = int(input('Hello, can you give me a number? '))
    collatz(num)
except ValueError:
    print('Please use whole numbers only.')

