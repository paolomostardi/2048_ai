import pygame
import random
from logic2048 import Logic2048
import math

"""

0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15

"""




class Board2048:
    def __init__(self, size, padding, screen):

        self.grey = (224, 224, 224)
        self.screen = screen

        self.padding = padding
        self.square_list = []
        self.orange = (255, 127, 80)
        self.size = size/4
        self.logical_board = Logic2048()

    def render(self):
        for index, square in enumerate(self.logical_board.square_list):
            x, y = self.calculate_coordinates(index)
            color = self.get_color_from_number(square)
            rectangle = pygame.Rect(self.size, self.size, x, y)

            pygame.draw.rect(self.screen, color, rectangle)

    def calculate_coordinates(self, index):
        padding = self.padding

        if index == 0:
            return 0, 0

        x = 4 % index
        y = index // 4
        x *= self.size + padding
        y *= self.size + padding

        return x, y

    def on_move_down(self):
        self.logical_board.slide_down()


    def get_color_from_number(self,square):
        color = self.grey

        if square != 0:
            color = math.log2(square)

        return self.grey

def main():

    WIDTH = 1200
    HEIGHT = 800
    board_size = 700
    padding = 100

    running = True

    clock = pygame.time.Clock()
    framerate = 15
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    board = Board2048(board_size, padding, screen)

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