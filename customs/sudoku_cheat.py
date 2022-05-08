from sudoku import Sudoku
from sudoku.sudoku import UnsolvableSudoku

# Create sudoku
puzzle = Sudoku(3).difficulty(0.5)

# Solve a sudoku
solution = puzzle.solve()

# Show grafically the sudoku
puzzle.show()

# Show grafically the solution
solution.show()

# Get the obj sudoku
puzzle.board

# Get the obj solution
solution.board

# Create sudoku with a seed
puzzle = Sudoku(3, seed=None).difficulty(0.5)
input("Ready?\n")
solution = puzzle.solve()
solution.show()

input("Now you should have a error\n")
try:
	board = [
	    [0,0,7,0,4,0,0,0,0],
	    [0,0,0,0,0,8,0,0,6],
	    [0,4,1,0,0,0,9,0,0],
	    [0,0,0,0,0,0,1,7,0],
	    [0,0,0,0,0,6,0,0,0],
	    [0,0,8,7,0,0,2,0,0],
	    [3,0,0,0,0,0,0,0,0],
	    [0,0,0,1,2,0,0,0,0],
	    [8,6,0,0,7,6,0,0,5]
	]
	puzzle = Sudoku(3, 3, board=board)

	puzzle.show_full()
	puzzle.solve(raising=True).show_full()

except Exception as e:
			print(e)

(
	[
		[5, None, None, None, 9, None, None, 4, None], [7, None, 9, None, 6, 4, None, None, 3], [None, 4, 3, 5, None, None, 6, 9, 1], 
		[6, None, 5, 9, None, 3, None, None, None], [3, None, None, 8, None, 7, 1, 2, None], [None, 8, 7, None, None, None, 9, 3, None], 
		[None, None, 1, None, None, 5, 8, 6, 9], [None, None, 2, 1, 8, 6, None, None, None], [None, 5, None, None, 3, 9, 2, 1, None]
	], 
	[
		[5, 6, 8, 3, 9, 1, 7, 4, 2], [7, 1, 9, 2, 6, 4, 5, 8, 3], [2, 4, 3, 5, 7, 8, 6, 9, 1], 
		[6, 2, 5, 9, 1, 3, 4, 7, 8], [3, 9, 4, 8, 5, 7, 1, 2, 6], [1, 8, 7, 6, 4, 2, 9, 3, 5], 
		[4, 3, 1, 7, 2, 5, 8, 6, 9], [9, 7, 2, 1, 8, 6, 3, 5, 4], [8, 5, 6, 4, 3, 9, 2, 1, 7]
	]
)