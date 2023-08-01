import pygame




class Board2048:
    def __init__(self):
        return
    def render(self, screen):
        color = (50, 200, 200)

        for i in range(4):
            for j in range(4):
                rect = pygame.Rect(10,10,j*11,i*11)
                pygame.draw.rect(screen, color, rect )



def main():

    WIDTH = 1200
    HEIGHT = 800
    board_size = 700

    running = True

    clock = pygame.time.Clock()
    framerate = 15
    screen = pygame.display.set_mode((WIDTH, HEIGHT))



    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
               print('hello')

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    print('hello')
                elif event.key == pygame.K_UP:
                    print('hello')

        screen.fill((200, 200, 200))
        rectangle = (20,20, 100, 50)
        color = (50, 200, 200)

        for i in range(4):
            for j in range(4):
                rect = pygame.Rect(101 * i, 101 * j,  100,100)
                pygame.draw.rect(screen, color, rect)

        pygame.display.update()
        clock.tick(framerate)

main()