grid = [['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#For loop in a  for loop
for j in range(len(grid[0])):    # columns (goes to the right, 0 to 5= 6)
    for i in range(len(grid)):   # rows (goes down, 0 to 8 = 9)
        print(grid[i][j],end='') # prints the element located on the current row (i) and column (j)//
                                 # without moving to a new line.

    # After completing the column, print a new line to go to the next column.    
    print()                     

