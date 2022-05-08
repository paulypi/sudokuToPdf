# SudokuToPdf
Create a sudoku book content pdf with printing size as Letter and puzzles difficulty Easy / Medium / Hard.

## Installing process

1. Create a virtual environment
    > python -m venv sudokuToPdf

2. Activate the virtual environment
    > .\sudokuToPdf\Scripts\activate

3. Import requirements
    > pip install -r requirement.txt

4. Execute the program
    > python sudokuToPdf.py

## Usage
1. Insert the number of sudoku (per difficulty)
    > EX. Puzzles number: 36
   - The minimum puzzles number is 36  
   - 36 *(puzzles)* * 3 *(difficulty)* = 108 puzzles + 108 solutions
   - The number should be divisible by 4 and 9
   - The program auto choice the nearest number of puzzles having the criteria listed above <br>
*(if your input is 30, he will choose 36 and so on)*


2. Insert the name of the book
    > EX. Name of book: MyPuzzleBook

3. #### Grab a coffee and take a brake **!!**


4. Find your book content **inside a folder** with **the current date and hours of creation as name**  

**_EX._**  
Inside folder named "**02-05-2022_12-27-58**" you will find:
- **MyPuzzleBook.pdf**      =>  as complete book content<br>     
- **puzzle_content.pdf**    =>  as the puzzle only content<br>
- **solution_content.pdf**  =>  as the solution only content