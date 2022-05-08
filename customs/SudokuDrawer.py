# Thanks to:
# Sudoku Generator Algorithm - www.101computing.net/sudoku-generator-algorithm/

import turtle
from PIL import Image
from PIL import EpsImagePlugin


class GridDrawer:
    """ Generate Sudoku image """

    def __init__(self, title: str, grid: list):
        self.title = title
        self.grid = grid

    def setup(self, size=50, color="#000000", intDim=100, topLeft_xy=(-452, 452)):
        self.screen = turtle.Screen()
        self.screen.setup(width=950, height=950)
        self.myPen = turtle.Turtle()
        self.myPen.speed(0)
        self.myPen.color(color)
        self.myPen.hideturtle()
        self.topLeft_x, self.topLeft_y = topLeft_xy
        self.size = size
        self.intDim = intDim

    def text(self, message, x, y, size):
        FONT = ('Arial', size, 'normal')
        self.myPen.penup()
        self.myPen.goto(x, y)
        self.myPen.write(message, align="left", font=FONT)

    def drawGrid(self, grid):
        """ A procedure to draw the grid on screen using Python Turtle """
        for row in range(0, 10):
            if (row % 3) == 0:
                self.myPen.pensize(7)
            else:
                self.myPen.pensize(2)
            self.myPen.penup()
            self.myPen.goto(self.topLeft_x, self.topLeft_y - row * self.intDim)
            self.myPen.pendown()
            self.myPen.goto(self.topLeft_x + 9 * self.intDim, self.topLeft_y - row * self.intDim)
        for col in range(0, 10):
            if (col % 3) == 0:
                self.myPen.pensize(7)
            else:
                self.myPen.pensize(2)
            self.myPen.penup()
            self.myPen.goto(self.topLeft_x + col * self.intDim, self.topLeft_y)
            self.myPen.pendown()
            self.myPen.goto(self.topLeft_x + col * self.intDim, self.topLeft_y - 9 * self.intDim)

        for row in range(0, 9):
            for col in range(0, 9):
                if self.grid[row][col] != None:
                    self.text(self.grid[row][col], self.topLeft_x + col * self.intDim + 35,
                              self.topLeft_y - row * self.intDim - self.intDim + 20, self.size)

    def saveimg(self):
        """ Export a canvas and convert the canvas in jpg """
        import_ = '.\\eps\\' + self.title + '.eps'
        export_ = '.\\jpg\\' + self.title + '.jpg'
        self.myPen.getscreen().getcanvas().postscript(file=import_)
        EpsImagePlugin.gs_windows_binary = "D:\\gs\\gs9.55.0\\bin\\gswin64c.exe"
        img = Image.open(import_)
        # img = img.resize((300, 300), Image.ANTIALIAS)
        img.save(export_)

    def biutify_pdf(self):
        self.myPen.pensize(5)
        self.myPen.penup()
        self.myPen.goto(self.topLeft_x, self.topLeft_y)
        self.myPen.pendown()
        self.myPen.goto(self.topLeft_x + 20, self.topLeft_y)

    def exit(self):
        self.screen.done()

    def run(self):
        self.setup()  # Add auguments to modify setup

        self.drawGrid(self.grid)
        self.myPen.getscreen().update()
        self.saveimg()
        self.screen.clear()

        # print(f"Sudoku Grid < {self.title} > Ready")
