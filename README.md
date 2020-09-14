# Coding Side Projects

## Sudoku Solver

A sudoku solver written in python using backtracking.

Sudokus are encoding using 2 dimensional numpy arrays. 
Example:
```python
sudoku = np.array([[2, 0, 0, 0, 0, 0, 0 ,0, 1],
                   [0, 5, 0, 1, 9, 0, 0, 0, 7],
                   [7, 0, 0, 4, 3, 5, 0, 0, 9],
                   [4, 0, 0, 0, 6, 7, 9, 0, 0],
                   [9, 2, 3, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 4, 0, 0, 0],
                   [0, 0, 0, 0, 8, 0, 0, 0, 6],
                   [0, 0, 0, 7, 0, 3, 0, 0, 0],
                   [1, 0, 9, 0, 0, 0, 7, 3, 0]])
```

Algorithm contains two functions:
 ```python
 is_possible(sudoku)
 #checks wether there are any mistakes in a (partially) solved sudoku. Return True when there are no mistakes.
 ```
and
```python
solve(sudoku)
#tries to solve the sudoku using backtracking. Returns a generator object containing all possible solutions.
```
Usage:

```python
#define sudoku
#using an empty sudoku will generate ALL solutions
sudoku = np.array([[0, 0, 0, 0, 0, 0, 0 ,0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]])
#generate solutions
s = solve(sudoku)
#show first solution
next(s)

>array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
       [4, 5, 6, 7, 8, 9, 1, 2, 3],
       [7, 8, 9, 1, 2, 3, 4, 5, 6],
       [2, 1, 4, 3, 6, 5, 8, 9, 7],
       [3, 6, 5, 8, 9, 7, 2, 1, 4],
       [8, 9, 7, 2, 1, 4, 3, 6, 5],
       [5, 3, 1, 6, 4, 2, 9, 7, 8],
       [6, 4, 2, 9, 7, 8, 5, 3, 1],
       [9, 7, 8, 5, 3, 1, 6, 4, 2]])