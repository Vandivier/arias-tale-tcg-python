import pygame
import sys


def main():
    pygame.init()

    canvas = pyodide.globals.get("canvas")
    width, height = canvas.width, canvas.height

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame in Pyodide")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 255))
        pygame.draw.rect(screen, (255, 255, 255), (100, 100, 200, 200))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


main()
