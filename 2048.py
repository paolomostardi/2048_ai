import pygame
import random


"""

0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15

"""




class Board2048:
    def __init__(self, size, screen):

        self.square_list = []
        self.orange = (255, 127, 80)
        self.size = size
        for i in range(4):
            for j in range(4):
                rect = pygame.Rect(i * 110 + 350, j * 110 + 50, 100, 100)
                self.square_list.append([screen, [255, 255, 255], rect, 0])

        self.generate_entry()

    def render(self):
        for square in self.square_list:
            pygame.draw.rect(square[0], square[1], square[2])

    def get_all_empty_squares(self):
        empty_squares = []
        for square in self.square_list:
            if square[3] == 0:
                empty_squares.append(square)
        return empty_squares

    def get_all_full_squares(self):
        full_squares = []
        for square in self.square_list:
            if square[3] is not 0:
                full_squares.append(square)
        return full_squares

    def get_position_of_square(self):

        return

    def generate_entry(self):
        empty_squares = self.get_all_empty_squares()
        if not empty_squares:
            self.game_finish()
            return
        square = random.choice(empty_squares)
        square[3] = 2
        square[1] = self.orange
        return

    def on_move_down(self):
        full_squares = self.get_all_full_squares()

        return

    def game_finish(self):

        return

def main():

    WIDTH = 1200
    HEIGHT = 800
    board_size = 700

    running = True

    clock = pygame.time.Clock()
    framerate = 15
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    board = Board2048(board_size, screen)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
               print('hello')

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    board.on_move_down()
                elif event.key == pygame.K_UP:
                    print('hello')
                board.generate_entry()


        screen.fill((200, 200, 200))
        rectangle = (20,20, 100, 50)
        color = (50, 200, 200)

        board.render()

        pygame.display.update()
        clock.tick(framerate)

main()