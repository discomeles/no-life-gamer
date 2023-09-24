import numpy as np
import golmath as gm
import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, img: str, img_pushed: str, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)        
        self.img_up = pygame.image.load(img).convert()
        self.img_pushed = pygame.image.load(img_pushed).convert()
        self.img = self.img_up
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 146, 45)

    def set_button(self, value):
        if value == "push":
            self.img = self.img_pushed
        if value == "up":
            self.img = self.img_up

class Logo(pygame.sprite.Sprite):
    def __init__(self, img: str, x: int, y: int):
        self.img = pygame.image.load(img).convert()
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, dx, dy):
        self.x += dx
        self.rect.x += dx
        self.y += dy
        self.rect.y += dy


# def start_screen(display):
#     display.fill((0, 0, 0))
#     font1 = pygame.font.SysFont('mono', 20, bold = True)
#     logo = Logo("resources/discomeles-logo.png", 88, -241)
#     display.blit(logo, (88, 80))
#     pygame.display.update()

def game_main():
    pygame.init()

    display = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    pygame.display.set_caption('No Life Gamer ~ Yet Another Game of Life')
    icon = pygame.image.load("resources/icon.png").convert_alpha()
    pygame.display.set_icon(icon)

    update_matrix = pygame.USEREVENT+1
    pygame.time.set_timer(update_matrix, 1000)
    counter = pygame.USEREVENT+2
    pygame.time.set_timer(counter, 1000)
    count = 0

    tiles = []
    tiles.append(pygame.image.load("resources/grass.png").convert())
    tiles.append(pygame.image.load("resources/flower.png").convert())

    title = pygame.image.load("resources/title.png").convert()

    pause_button = Button("resources/pause-button.png", "resources/pause-button-pushed.png", 27, 538)
    continue_button = Button("resources/cont-button.png", "resources/cont-button-pushed.png", 227, 538)
    reset_button = Button("resources/reset-button.png", "resources/reset-button-pushed.png", 427, 538)
    quit_button = Button("resources/quit-button.png", "resources/quit-button-pushed.png", 627, 538)
    logo = Logo("resources/discomeles-logo.png", 88, -241)
    start_txt = Logo("resources/start-txt.png", 244, 300)
    start_title = Logo("resources/start-title.png", 72, 600)

    state = "startscreen"
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
                    pause_button.set_button("push")
                if continue_button.rect.collidepoint(event.pos):
                    continue_button.set_button("push")
                if reset_button.rect.collidepoint(event.pos):
                    reset_button.set_button("push")
                if quit_button.rect.collidepoint(event.pos):
                    quit_button.set_button("push")

            if event.type == pygame.MOUSEBUTTONUP:
                if pause_button.rect.collidepoint(event.pos):
                    pause_button.set_button("up")
                    pause = True
                if continue_button.rect.collidepoint(event.pos):
                    continue_button.set_button("up")
                    pause = False
                if reset_button.rect.collidepoint(event.pos):
                    reset_button.set_button("up")
                    reset = True
                if quit_button.rect.collidepoint(event.pos):
                    quit_button.set_button("up")
                    pygame.quit()
                    quit()

            if event.type == update_matrix:
                # if game is paused, the matrix is not evaluated
                if not pause:
                    rm = gm.evaluate_cells(tm)
                    tm = rm.copy()

            if event.type == counter:
                if state == "startscreen":
                    count += 1

            if event.type == pygame.QUIT:
                exit()



        display.fill((0,0,0))

        if state == "startscreen":
            display.blit(logo.img, (logo.x, logo.y))
            if logo.y < 60:
                logo.move(0,2)
            if count > 5:
                display.blit(start_txt.img, (start_txt.x, start_txt.y))
            if count > 6:
                display.blit(start_title.img, (start_title.x, start_title.y))
                if start_title.y > 360:
                    start_title.move(0,-2)
            if count > 12:
                state = "game"
                continue

        if state == "game":
            display.blit(title, (89, 8))
            display.blit(pause_button.img, (pause_button.x, pause_button.y))
            display.blit(continue_button.img, (continue_button.x, continue_button.y))
            display.blit(reset_button.img, (reset_button.x, reset_button.y))
            display.blit(quit_button.img, (quit_button.x, quit_button.y))

            if reset or (pause and reset):
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
        clock.tick(30)


def main():
    game_main()

if __name__=="__main__":
    main()