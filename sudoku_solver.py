import numpy as np

sudoku = np.array([[0, 0, 0, 0, 0, 0, 0 ,0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]])

def is_possible(sudoku):
    import collections
    #check rows and columns
    for i in range(9):
        row_n_count = collections.Counter(sudoku[i, : ]) #count how many times each number occurs in each row
        column_n_count = collections.Counter(sudoku[:, i]) #count how many times each number occurs in each column
        for i in range(9):
            #test if a number between 1 and 9 (inclusive) occurs more than once in each row and/or column
            #if so return False
            if row_n_count[i + 1] > 1 or column_n_count[i + 1] > 1:
                return False
    #check squares
    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            square = sudoku[row:row+3, column:column+3].flatten() #generate a 1D array of each square
            for i in range(9):
                #count how many times each number occurs in the square (which is now a 1D array)
                #and check if a number between 1 and 9 (inclusive) occurs more than once in the square
                #if so return False
                if collections.Counter(square)[i + 1] > 1:
                    return False
    #if a number occurs at most once in each row, column or square return True
    return True

def solve(sudoku):
    #loop through the entire sudoku grid
    for y in range(9):
        for x in range(9):
            #find the first empty spot
            if sudoku[y][x] == 0:
                #loop through every number between 1 and 9 (inclusive)
                for n in range(1, 10):
                    #make a copy of the sudoku to test the new number at the empty spot
                    test_sudoku = sudoku.copy()
                    test_sudoku[y][x] = n
                    if is_possible(test_sudoku):
                        #if the number can be place at the empty spot solve the new sudoky with the extra number
                        sudoku = test_sudoku.copy()
                        yield from solve(sudoku)
                        #make spot empty of no solution could be found
                        sudoku[y][x] = 0
                #return if no number could be filled in
                return
    #yield if all spots have been filled in
    yield sudoku