import asyncio
import pygame
import random


async def main():
    pygame.init()

    canvas = pyodide.globals.get("canvas")
    width, height = canvas.width, canvas.height

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame in Pyodide")

    running = True
    fill_color = (0, 0, 255)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                fill_color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )

        screen.fill(fill_color)
        pygame.draw.rect(screen, (255, 255, 255), (100, 100, 200, 200))
        pygame.display.flip()
        await asyncio.sleep(1 / 30)  # 30 FPS

    pygame.quit()


await main()
