import random


class Logic2048:

    def __init__(self):
        self.square_list = []
        for i in range(4):
            for j in range(4):
                self.square_list.append(0)
        self.generate_entry()

    def get_all_empty_squares(self):
        empty_squares = []
        for index, square in enumerate(self.square_list):
            if square == 0:
                empty_squares.append(index)
        return empty_squares

    def get_all_full_squares(self):
        full_squares = []
        for index, square in enumerate(self.square_list):
            if square != 0:
                full_squares.append(index)
        return full_squares

    def generate_entry(self):
        empty_squares = self.get_all_empty_squares()
        if not empty_squares:
            self.game_finish()
            return
        square_index = random.choice(empty_squares)
        self.square_list[square_index] = 2

    def slide_down(self):
        self.generate_entry()
        return

    def game_finish(self):
        return

board = Logic2048()

a = board.get_all_full_squares()
print(a)
print(board.square_list[a[0]])
