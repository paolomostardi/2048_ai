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

    def merge_down(self):
        for index, square in enumerate(self.square_list):
            index = len(self.square_list) - index - 1
            if index - 3 == 0:
                return
            if self.square_list[index] == self.square_list[index - 4]:
                self.square_list[index - 4] = 0
                self.square_list[index] *= 2

        return

    def merge_up(self):

        for index, square in enumerate(self.square_list):
            if index < 3:
                print()
            elif self.square_list[index] == self.square_list[index - 4]:
                self.square_list[index - 4] = self.square_list[index] * 2
                self.square_list[index] = 0

        return

    def merge_left(self):
        for index, square in enumerate(self.square_list):

            if square == 0:
                print('')
            elif index % 4 == 0:
                print('')

            elif self.square_list[index] == self.square_list[index - 1]:
                self.square_list[index - 1] = self.square_list[index] * 2
                self.square_list[index] = 0

        return

    def merge_right(self):
        for index, square in enumerate(self.square_list):

            if square == 0:
                print('')
            elif index % 4 == 3:
                print('')

            elif self.square_list[index] == self.square_list[index + 1]:
                self.square_list[index + 1] = self.square_list[index] * 2
                self.square_list[index] = 0

        return

    def move_all_tiles_down(self):
        for index, square in enumerate(self.square_list):
            length_list = len(self.square_list)
            index = length_list - index - 1

            while index + 4 < length_list:
                if self.square_list[index + 4] == 0:
                    self.square_list[index + 4] = self.square_list[index]
                    self.square_list[index] = 0
                index += 4

        return

    def move_all_tiles_up(self):
        for index, square in enumerate(self.square_list):
            length_list = len(self.square_list)

            while index > 3:
                if self.square_list[index - 4] == 0:
                    self.square_list[index - 4] = self.square_list[index]
                    self.square_list[index] = 0
                index -= 4

        return

    def move_all_tiles_left(self):
        for index, square in enumerate(self.square_list):

            while index % 4 != 0:
                if self.square_list[index - 1] == 0:
                    self.square_list[index - 1] = self.square_list[index]
                    self.square_list[index] = 0
                index -= 1

        return

    def move_all_tiles_right(self):
        for index, square in enumerate(self.square_list):

            while index % 4 != 3:
                if self.square_list[index + 1] == 0:
                    self.square_list[index + 1] = self.square_list[index]
                    self.square_list[index] = 0
                index += 1

        return

    def on_down(self):
        self.move_all_tiles_down()
        self.merge_down()
        self.generate_entry()

    def on_left(self):
        self.move_all_tiles_left()
        self.merge_left()
        self.generate_entry()
        return

    def on_right(self):
        self.move_all_tiles_right()
        self.merge_right()
        self.generate_entry()
        return

    def on_up(self):
        self.move_all_tiles_up()
        self.merge_up()
        self.generate_entry()
        return

    def game_finish(self):
        return

board = Logic2048()

a = board.get_all_full_squares()
print(a)
print(board.square_list[a[0]])
