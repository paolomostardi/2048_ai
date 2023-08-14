import pygame
import random
from logic2048 import Logic2048
import math
import copy

"""

0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15


rect = pygame.Rect(i * 110 + 350, j * 110 + 50, 100, 100)




"""




class Board2048:
    def __init__(self, size, padding, screen):

        self.grey = [224, 224, 224]
        self.orange = [255, 127, 80]
        self.screen = screen

        self.padding = padding
        self.square_list = []
        self.size = size//4
        self.logical_board = Logic2048()

    def render(self):
        for index, square in enumerate(self.logical_board.square_list):

            x, y = self.calculate_coordinates(index)
            color = self.get_color_from_number(square)

            rectangle = pygame.Rect(x,y, self.size-5, self.size-5)

            pygame.draw.rect(self.screen, color, rectangle)

    def calculate_coordinates(self, index):
        padding = self.padding

        if index == 0:
            return padding, padding

        x = index % 4
        y = index // 4

        x *= self.size
        y *= self.size
        x += padding
        y += padding

        return x, y

    def on_move_down(self):
        self.logical_board.on_down()

    def get_color_from_number(self,square):
        color = self.grey

        if square != 0:

            r = 255
            g = 255 - (255/11) * math.log2(square)
            b = 0
            color = (r, g, b)

        return color


def main():

    WIDTH = 800
    HEIGHT = 800
    board_size = 750
    padding = 25

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



        screen.fill((200, 200, 200))
        rectangle = (20,20, 100, 50)
        color = (50, 200, 200)

        board.render()

        pygame.display.update()
        clock.tick(framerate)

main()