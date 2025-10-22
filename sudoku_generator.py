import math,random
import pygame

#tester

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = math.sqrt(self.row_length)
        self.board = [[0 for i in range(self.row_length)] for i in range(self.row_length)]
    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
	second comment testing
    '''
    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        for row in self.board:  # row: ["-", "-", "-"]
            for col in row:
                print(col, end=" ")
            print()

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        for i in range(self.row_length):
            if num == self.board[row][i]:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        col = int(col)
        for i in range(self.row_length):
            if num == self.board[i][col]:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        # print(f"Checking 3x3 box starting at ({row_start}, {col_start}) for number {num}")
        col_start = int(col_start)
        nums_in_box = set()
        if row_start / 3 != 0:
            row_start = (row_start//3) * 3
        if col_start / 3 != 0:
            col_start = (col_start//3) * 3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if i < self.row_length and j < self.row_length:
                    # print(f"Checking cell ({i}, {j}): {self.board[i][j]}")
                    nums_in_box.add(num)
                    if num == self.board[i][j]:
                        # print('false')
                        return False
        # print('True')
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num)

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        # for i in range(row_start, row_start + 3):
        #     for j in range(col_start, col_start + 3):
        #         random_num = random.randint(1, 9)
        #         # print((i, j, random_num))
        #         if self.is_valid(i, j, random_num):
        #             self.board[i][j] = random_num
        stack = []
        x_coordinate = row_start
        y_coordinate = col_start

        while True:
            value = random.randint(1, 9)
            if value in stack:
                pass
            else:
                stack.append(value)
                self.board[x_coordinate][y_coordinate] = value
                x_coordinate += 1
                if x_coordinate > row_start + 2:
                    x_coordinate = row_start
                    y_coordinate += 1
                    col_start += 1

                if len(stack) == 9:
                    break

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        count = 0
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                col = int(col)
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
                count +=1
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        # print(self.board)
        num_removed = 0
        while num_removed < self.removed_cells:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                num_removed += 1


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

class Cell:
   def __init__(self, value, row, col, screen):
       self.value = value
       self.row = row
       self.col = col
       self.screen = screen
       self.sketched_value = 0
       self.selected = False


   def set_cell_value(self, value):
       self.value = value


   def set_sketched_value(self, value):
       self.sketched_value = value

   def draw(self):
       num_font = pygame.font.SysFont("arial", 40, bold= True, italic = False)
       if self.value != 0:
           numwriting =num_font.render(str(self.value), True, (0, 0, 0))
           text_rect = numwriting.get_rect()
           text_rect.center = (self.col * 50 + 25, self.row * 50 + 25)
           self.screen.blit(numwriting, text_rect)
       elif self.sketched_value != 0:
           numwriting = num_font.render(str(self.value), True, (0, 0, 0))
           text_rect = numwriting.get_rect()
           text_rect.center = (self.col * 50 + 25, self.row * 50 + 25)
           self.screen.blit(numwriting, text_rect)

class Board:
   pygame.init()
   def __init__(self, width, height, screen, difficulty):
           self.board = generate_sudoku(9, difficulty)
           self.width = width
           self.height = height
           self.screen = screen
           self.difficulty = difficulty
           self.original_board = [[self.board[row][col] for col in range(len(self.board[0]))] for row in
                                  range(len(self.board))]
           self.board_cells = [[Cell(self.board[row][col], row, col, screen) for col in range(len(self.board[0]))] for
                               row in range(len(self.board))]
           self.chosen_cell = None
           self.past_row = -1
           self.past_col = -1

   def draw(self):
       black = (0,0,0)
       #rows
       for i in range(10):
           if i % 3 == 0:
               pygame.draw.line(self.screen, black, (0, (i*50)), (self.height, (i*50)), width = 10)


           else:
               pygame.draw.line(self.screen, black, (0, (i*50)), (self.height, (i*50)))


       #cols
       for i in range(10):
           if i % 3 == 0:
               pygame.draw.line(self.screen, black, ((i*50), 0), ((i*50), self.width), width = 10)


           else:
               pygame.draw.line(self.screen, black, ((i*50), 0), ((i*50), self.width))

       if self.difficulty == 30:
           for i in range(9):
               for j in range(9):
                   value = self.board[i][j]
                   n_cell = Cell(value, i, j, self.screen)
                   n_cell.draw()
           pygame.display.update()


       if self.difficulty == 40:
           for i in range(9):
               for j in range(9):
                   value = self.board[i][j]
                   n_cell = Cell(value, i, j, self.screen)
                   n_cell.draw()
           pygame.display.update()

       if self.difficulty == 50:
           for i in range(9):
               for j in range(9):
                   value = self.board[i][j]
                   n_cell = Cell(value, i, j, self.screen)
                   n_cell.draw()
           pygame.display.update()


   def select(self, row, col):
       if self.original_board[col][row] != 0:
           self.chosen_cell = None
       else:
           self.chosen_cell = self.board_cells[col][row]

           # Unselecting previous cell
           if self.past_row != -1 and self.past_col != -1:
               self.board_cells[self.past_col][self.past_row].selected = False
               self.board_cells[self.past_col][self.past_col].draw()

           self.past_row, self.past_col = row, col
           self.board_cells[col][row].selected = True
       return self.chosen_cell

   def click(self, x, y):
       x_coordinate = x // 50
       y_coordinate = y // 50
       if x_coordinate >= 9 or y_coordinate >= 9:
           return None, None
       return x_coordinate, y_coordinate

   # cell cleared
   def clear(self):
       if self.chosen_cell and self.board[self.chosen_cell.row][self.chosen_cell.col] != 0:
           self.chosen_cell.set_cell_value(0)
           self.chosen_cell.set_sketched_value(0)
           self.update_board()
           self.draw()

   def sketch(self, value):
       if self.chosen_cell:
           self.chosen_cell.set_sketched_value(value)

   def place_number(self, value):
       if self.chosen_cell:
           self.chosen_cell.set_cell_value(value)
           self.chosen_cell.set_sketched_value(0)
           self.chosen_cell.draw()
           self.chosen_cell.selected = False

   def reset_to_original(self):
       for i in range(len(self.board)):
           for j in range(len(self.board[0])):
               self.board[i][j] = self.original_board[i][j]
               self.board_cells[i][j].set_cell_value(self.original_board[i][j])

   def is_full(self):
       for i in range(len(self.board)):#len(self.height)
           for j in range(len(self.board[0])):
               if self.board_cells[i][j].value == 0:
                   return False
       return True

   def update_board(self):
       if self.chosen_cell != None:
           self.board_cells[self.chosen_cell.row][self.chosen_cell.col].value = self.chosen_cell.value
           self.board[self.chosen_cell.row][self.chosen_cell.col] = self.chosen_cell.value
           # Keeps original board as original
           self.original_board[self.chosen_cell.row][self.chosen_cell.col] = 0

   def find_empty(self):
       for row in range(self.height):
           for col in range(self.width):
               # If the cell is empty, its coordinates are returned as a tuple.
               if self.board_cells[row][col].value == 0:
                   return row, col
       return None

   def check_board(self):
       def valid_in_row(row, num):
           counter = 0
           for count in range(len(self.board[row])):
               if num == self.board[row][count]:
                   print(f'{num} == {self.board}')
                   counter += 1
                   if counter > 1:
                       print('False')
                       return False
           print('True')
           return True

       def valid_in_col(col, num):
           counter = 0
           for count in range(len(self.board)):
               if num == self.board[count][col] and count != col:
                   counter += 1
                   if counter > 1:
                       return False
           return True

       def valid_in_box(row_start, col_start, num):
           counter = 0
           for i in range(row_start, row_start + 3):
               for p in range(col_start, col_start + 3):
                   if num == self.board[i][p]:
                       counter += 1
                       if counter > 1:
                           return False
           return True

       def is_valid(row, col, num):
           row_copy = row
           col_copy = col
           while row_copy != 0:
               if row_copy % 3 == 0:
                   break
               row_copy -= 1
           while col_copy != 0:
               if col_copy % 3 == 0:
                   break
               col_copy -= 1
           if valid_in_row(row, num) is True:
               if valid_in_col(col, num) is True:
                   if valid_in_box(row_copy, col_copy, num) is True:
                       return True
                   else:
                       return False
               else:
                   return False
           else:
               return False

       for row in range(self.height):
           for col in range(self.width):
               try:
                if is_valid(row, col, self.board[row][col]):
                    pass
               except IndexError:
                   print(f'{row}{col}{self.board}')
               else:
                   return False
       return True



if __name__ == "__main__":
    screen = pygame.display.set_mode((450, 450))
    screen.fill('light pink')
    b = Board(450, 450, screen, 30)
    b.draw()
    pygame.display.flip()

