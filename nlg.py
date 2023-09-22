import numpy as np
import golmath as gm
import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, img: str, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(img).convert()
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 146, 45)

def game_main():
    pygame.init()

    display = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()

    update_matrix = pygame.USEREVENT+1
    pygame.time.set_timer(update_matrix, 1000)

    tiles = []
    tiles.append(pygame.image.load("resources/grass.png").convert())
    tiles.append(pygame.image.load("resources/flower.png").convert())

    title = pygame.image.load("resources/title.png").convert()

    pause_button = Button("resources/pause-button.png", 27, 538)
    continue_button = Button("resources/cont-button.png", 227, 538)
    reset_button = Button("resources/reset-button.png", 427, 538)
    quit_button = Button("resources/quit-button.png", 627, 538)

    pause = False
    reset = False

    width = 25
    height = 15
    from_top = 40
    tm = gm.create_random_matrix(15,25)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button.rect.collidepoint(event.pos):
                    pause = True
                if continue_button.rect.collidepoint(event.pos):
                    pause = False
                if reset_button.rect.collidepoint(event.pos):
                    reset = True
                    current_time = pygame.time.get_ticks()
                    reset_timer = current_time + 500
                if quit_button.rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()

            if event.type == update_matrix:
                rm = gm.evaluate_cells(tm)
                tm = rm.copy()

            if event.type == pygame.QUIT:
                exit()

        display.fill((0,0,0))

        display.blit(title, (89, 8))
        display.blit(pause_button.img, (pause_button.x, pause_button.y))
        display.blit(continue_button.img, (continue_button.x, continue_button.y))
        display.blit(reset_button.img, (reset_button.x, reset_button.y))
        display.blit(quit_button.img, (quit_button.x, quit_button.y))

        if pause:
            pygame.time.wait(100)
            continue

        if reset:
            zm = gm.create_zero_matrix(15,25)
            for j in range(25):
                for i in range(15):
                    value = zm[i][j]
                    display.blit(tiles[value], (j*32, from_top + i*32))
            tm = gm.create_random_matrix(15,25)
            pygame.display.flip()
            pygame.time.wait(500)
            reset = False
            continue

        if not reset:
            for j in range(25):
                for i in range(15):
                    value = tm[i][j]
                    display.blit(tiles[value], (j*32, from_top + i*32))

        pygame.display.flip()
        clock.tick(5)


def main():
    game_main()

if __name__=="__main__":
    main()