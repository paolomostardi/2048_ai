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
        action_performed = False

        for index, square in enumerate(self.square_list):
            index = len(self.square_list) - index - 1
            if index - 3 == 0:
                return action_performed
            if self.square_list[index] == 0:
                continue
            elif self.square_list[index] == self.square_list[index - 4]:
                self.square_list[index - 4] = 0
                self.square_list[index] *= 2
                print(self.square_list[index])
                print(self.square_list[index - 4])
                action_performed = True

    def merge_up(self):
        action_performed = False

        for index, square in enumerate(self.square_list):
            if index < 3:
                continue
            if self.square_list[index] == 0:
                continue
            elif self.square_list[index] == self.square_list[index - 4]:
                self.square_list[index - 4] = self.square_list[index] * 2
                self.square_list[index] = 0
                action_performed = True

        return action_performed

    def merge_left(self):
        action_performed = False

        for index, square in enumerate(self.square_list):

            if square == 0:
                continue
            elif index % 4 == 0:
                continue

            elif self.square_list[index] == self.square_list[index - 1]:
                self.square_list[index - 1] = self.square_list[index] * 2
                self.square_list[index] = 0
                action_performed = True

        return action_performed

    def merge_right(self):
        action_performed = False

        for index, square in enumerate(self.square_list):

            index = len(self.square_list) - index - 1

            if self.square_list[index] == 0:
                continue
            elif index % 4 == 3:
                continue

            elif self.square_list[index] == self.square_list[index + 1]:
                self.square_list[index + 1] = self.square_list[index] * 2
                self.square_list[index] = 0
                action_performed = True

        return action_performed

    def move_all_tiles_down(self):
        action_performed = False

        for index, square in enumerate(self.square_list):
            length_list = len(self.square_list)
            index = length_list - index - 1

            if self.square_list[index] == 0:
                continue
            else:
                while index + 4 < length_list:
                    if self.square_list[index + 4] == 0:
                        self.square_list[index + 4] = self.square_list[index]
                        self.square_list[index] = 0
                        action_performed = True

                    index += 4

        return action_performed

    def move_all_tiles_up(self):
        action_performed = False

        for index, square in enumerate(self.square_list):

            if square == 0:
                continue

            while index > 3:
                if self.square_list[index - 4] == 0:
                    self.square_list[index - 4] = self.square_list[index]
                    self.square_list[index] = 0
                    action_performed = True

                index -= 4

        return action_performed

    def move_all_tiles_left(self):
        action_performed = False

        for index, square in enumerate(self.square_list):

            if square == 0:
                continue

            while index % 4 != 0:
                if self.square_list[index - 1] == 0:
                    self.square_list[index - 1] = self.square_list[index]
                    self.square_list[index] = 0
                    action_performed = True

                index -= 1

        return action_performed

    def move_all_tiles_right(self):
        action_performed = False
        for index, square in enumerate(self.square_list):

            if square == 0:
                continue
            while index % 4 != 3:
                if self.square_list[index + 1] == 0:
                    self.square_list[index + 1] = self.square_list[index]
                    self.square_list[index] = 0
                    action_performed = True
                index += 1

        return action_performed

    def on_down(self):
        action_performed = self.move_all_tiles_down()
        action_performed2 = self.merge_down()
        action_performed3 = self.move_all_tiles_down()

        if action_performed or action_performed2 or action_performed3:
            self.generate_entry()

    def on_left(self):
        action_performed = self.move_all_tiles_left()
        action_performed2 = self.merge_left()
        action_performed3 = self.move_all_tiles_left()

        if action_performed or action_performed2 or action_performed3:
            self.generate_entry()
        return

    def on_right(self):
        action_performed = self.move_all_tiles_right()
        action_performed2 = self.merge_right()
        action_performed3 = self.move_all_tiles_right()

        if action_performed or action_performed2 or action_performed3:
            self.generate_entry()

        return

    def on_up(self):
        action_performed = self.move_all_tiles_up()
        action_performed2 = self.merge_up()
        action_performed3 = self.move_all_tiles_up()

        if action_performed or action_performed2 or action_performed3:
            self.generate_entry()
        return

    def game_finish(self):
        return

board = Logic2048()

a = board.get_all_full_squares()
print(a)
print(board.square_list[a[0]])
