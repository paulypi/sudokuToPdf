import turtle
from time import sleep
from PIL import Image, EpsImagePlugin


class Background:
    def __init__(self, format_='Letter', color="#000000"):
        self.format_ = format_
        self.color = color

    def setup(self):
        if self.format_ == 'A4':
            # self.width=210
            # self.height=297
            self.topLeft_x = -362
            self.topLeft_y = 455
            self.row_x = 720
            self.row_y = 920
            self.screen = turtle.Screen()
            self.screen.setup(width=770, height=950)

        if self.format_ == 'Letter':
            self.width = 215.9
            self.height = 279.4
            self.topLeft_x = -362
            self.topLeft_y = 455
            self.row_x = 720
            self.row_y = 920
            self.screen = turtle.Screen()
            self.screen.setup(width=770, height=950)

    def saveimg(self):
        """ Export a canvas and convert the canvas in jpg """
        import_ = self.format_ + '_canvasBg.eps'
        export_ = self.format_ + '_bg.jpg'
        # print(export_)
        self.myPen.getscreen().getcanvas().postscript(file=import_)
        EpsImagePlugin.gs_windows_binary = "D:\\gs\\gs9.55.0\\bin\\gswin64c.exe"
        img = Image.open(import_)
        # Test measurement
        # img = img.resize((580, 800), Image.ANTIALIAS)
        # img = img.resize((self.width, self.height))
        img.save(export_)

    def run(self):
        self.setup()
        self.myPen = turtle.Turtle()
        self.myPen.speed(0)
        self.myPen.color(self.color)
        self.myPen.hideturtle()
        self.myPen.pensize(2)
        self.myPen.penup()
        self.myPen.goto(self.topLeft_x, self.topLeft_y)
        self.myPen.pendown()
        self.myPen.goto(self.topLeft_x + self.row_x, self.topLeft_y)
        self.myPen.goto(self.topLeft_x + self.row_x, self.topLeft_y - self.row_y)
        self.myPen.goto(self.topLeft_x, self.topLeft_y - self.row_y)
        self.myPen.goto(self.topLeft_x, self.topLeft_y)
        self.myPen.getscreen().update()
        self.saveimg()
        self.screen.clear()
