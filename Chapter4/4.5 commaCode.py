# input spam = ['apples', 'bananas', 'tofu', 'cats']
# output 'apples, bananas, tofu, and cats'.

myList = ['apples', 'pizza', 'dogs', 'cats']

def comma(items):
    for i in range(len(items) -2):
        print(items[i], end=", ") 
    print(items[-2] + ' and ' + items[-1]) 

comma(myList)




