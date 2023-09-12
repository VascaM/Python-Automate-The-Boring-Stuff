catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + #The number of values that are in a list 
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation. Als andere variable wordt gebruikt, update de string catNames niet.
print('The cat names are:')
for name in catNames:
    print('  ' + name)
