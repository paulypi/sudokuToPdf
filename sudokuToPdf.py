import os
import glob
import shutil
from time import sleep, time
from natsort import natsorted

from customs.SudokuGenerator import GenerateSudoku
from customs.SudokuDrawer import GridDrawer
from customs.PDFPager import Pager
from customs.BackgroundDrawer import Background
from PyPDF2 import PdfFileMerger, PdfFileReader


class Worker:
    def __init__(self):
        self.sudoku = None
        self.puzzleTitles = None
        self.solutionTitle = None
        self.puzzle_content = None
        self.solution_content = None
        self.bookname = None
        self.mergedObject = PdfFileMerger()

    def book_content(self):
        self.mergedObject.append(PdfFileReader('puzzle_content.pdf'))
        self.mergedObject.append(PdfFileReader('solution_content.pdf'))
        self.mergedObject.write(self.bookname + '.pdf')

    def sort_titles(self):
        easy = natsorted(glob.glob('./jpg/#* Easy.jpg'))
        medium = natsorted(glob.glob('./jpg/#* Medium.jpg'))
        hard = natsorted(glob.glob('./jpg/#* Hard.jpg'))
        self.puzzleTitles = easy + medium + hard
        self.solutionTitle = natsorted(glob.glob('./jpg/Solution*.jpg'))
        # print(len(self.puzzleTitles))

    def content_generator(self, generate=None, difficullty=None, range_=None, last=None):
        if generate:
            # input("[!] sudokus generati, continuare? ")
            while True:
                if (range_ % 4) == 0 and (range_ % 9) == 0:
                    break
                range_ += 1
                # TODO: rimuovere seed
            self.sudoku = [GenerateSudoku(difficulty=float(difficullty), number=n).run() for n in
                           range(1, int(range_ + 1))]
            for s in self.sudoku:
                GridDrawer(s[0], s[1]).run()
                GridDrawer("Solution " + s[0], s[2]).run()
                sleep(0.5)
            # input("[!] Immagini create, continuare? ")
            # Draw background image

        if last:
            Background().run()
            # shuffle(self.puzzleTitles)
            self.sort_titles()
            # print(f' the puzzles are {self.puzzleTitles}')
            # print(f' the solutions are {self.solutionTitle}')

            # Generate pdf for puzzle and for solution
            Pager().run(self.puzzleTitles, "puzzle_content")
            Pager().run(self.solutionTitle, "solution_content")
            # input("[OK] Pagine create, continue? ")
            if not self.bookname:
                self.bookname = input("Name of book: ")
            self.book_content()

    def run(self, pages=None):
        start = time()
        # TODO: create a program interface
        # TODO: choice
        for i in [0.4, 0.6, 0.8]:
            if i != 0.8:
                self.content_generator(generate=True, difficullty=i, range_=pages)
            else:
                self.content_generator(generate=True, difficullty=i, range_=pages, last=True)
        delta = time() - start
        print("\nExecution time in minutes: ", (round(delta, 3) / 60))


print("\nSudoku book content generator\n\nJust insert the number of puzzles you want your book content to be and grab a coffee!"
      "\n\nNota: the program will choice the nearest number of pages to reach a number that is divisible for 4 AND 9 "
      "[Ex. 36 - 108...] "
      "\n\tThat operation can take a wile!\n")
try:
    if not os.path.exists("jpg"):
        os.mkdir("jpg")
    if not os.path.exists("eps"):
        os.mkdir("eps")

    book = Worker()
    number = int(input("Puzzles number: "))
    book.bookname = input("Name of book: ")

    book.run(number)

    # cleanup
    shutil.rmtree("jpg")
    shutil.rmtree("eps")
    os.remove("Letter_bg.jpg")
    os.remove("Letter_canvasBg.eps")

    import datetime
    filename = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    os.mkdir(filename)
    shutil.move(book.bookname + ".pdf", filename + "/" + book.bookname + ".pdf")
    shutil.move("puzzle_content.pdf", filename + "/" + "puzzle_content.pdf")
    shutil.move("solution_content.pdf", filename + "/" + "solution_content.pdf")

except KeyboardInterrupt:
    print("\nThe program stopped due to a Keyboard Interruption")

except Exception as e:
    print(e)
    
finally:
    sleep(1)
    if os.path.exists("./jpg"):
        shutil.rmtree("jpg")
    if os.path.exists("./eps"):
        shutil.rmtree("eps")

