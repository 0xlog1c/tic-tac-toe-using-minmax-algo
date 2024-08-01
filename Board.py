from setup import *

class Board:
    def __init__(self):
        self.grid = [['0','0','0'],
                     ['0','0','0'],
                     ['0','0','0']]
        self.marked_squares = 0 # keep track of marked squares

    def mark_square(self, row, col, player):
        self.grid[row][col] = player
        self.marked_squares += 1

    def is_square_empty(self, row, col):
        # for checking whether the square is marked or not so the player can mark on an empty square only
        return self.grid[row][col] == '0'

    def get_empty_squares(self):
        # returns the empty (not marked) squares
        empty_squares = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.is_square_empty(row,col):
                    empty_squares.append((row,col))
        return empty_squares

    def is_full(self):
        # return if all squares are marked
        return self.marked_squares == 9

    def is_empty(self):
        # return if all squares are empty and not marked yet
        return self.marked_squares == 0

    def final_state(self):
        # 0: no win, x: player x wins, y: player o wins

        # check for horizontal wins
        for row in range(ROWS):
            if self.grid[row][0] == self.grid[row][1] == self.grid[row][2] != '0':
                return self.grid[row][0]

        # check for vertical wins
        for col in range(COLS):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != '0':
                return self.grid[0][col]

        # check for diagonal wins
        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != '0'
            or self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != '0'):
            return self.grid[1][1]

        # no win just yet
        return '0'
