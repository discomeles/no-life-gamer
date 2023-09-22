import numpy as np
import golmath as gm
import pygame

def game_main():
    pygame.init()

    display = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()

    tiles = []
    tiles.append(pygame.image.load("grass32.png"))
    tiles.append(pygame.image.load("flower32.png"))
    width = 25
    height = 15
    from_top = 40
    tm = gm.create_random_matrix(15,25)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        display.fill((0,0,0))


        for j in range(25):
            for i in range(15):
                value = tm[i][j]
                display.blit(tiles[value], (j*32, from_top + i*32))

        rm = gm.evaluate_cells(tm)
        tm = rm.copy()

        pygame.display.flip()
        clock.tick(1)


def main():
    game_main()

if __name__=="__main__":
    main()