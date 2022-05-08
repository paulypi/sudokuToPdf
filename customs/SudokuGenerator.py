import random

from sudoku import Sudoku


class GenerateSudoku:
    # TODO: se utilizzo seed non posso dividere per difficolta perche easy con seed 100 == hard con seed 100
    def __init__(self, difficulty=0.5, number=None):
        self.title = None
        self.puzzle = None
        self.solution = None
        self.difficulty = difficulty
        self.number = number

    def title_generator(self):
        # TODO: regolare difficolta con antonio
        if 0 < self.difficulty < 0.5:
            self.title = "#" + str(self.number) + " Easy"
        elif 0.5 < self.difficulty < 0.7:
            self.title = "#" + str(self.number) + " Medium"
        elif 0.7 < self.difficulty <= 0.9:
            self.title = "#" + str(self.number) + " Hard"

    def run(self):
        self.puzzle = Sudoku(seed=random.random()).difficulty(self.difficulty)

        self.solution = self.puzzle.solve()

        self.title_generator()

        return self.title, self.puzzle.board, self.solution.board
