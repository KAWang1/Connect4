import pygame
import sys

from butto import Button
# import game
from game import selection1

pygame.init()

SCREEN = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/connect_four.jpg")

selection = 0


def set_selection(num):
    global selection
    selection = num


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def single():
    while True:
        SINGLE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        SINGLE_TEXT = get_font(45).render("This is the SINGLE screen.", True, "White")
        SINGLE_RECT = SINGLE_TEXT.get_rect(center=(350, 260))
        SCREEN.blit(SINGLE_TEXT, SINGLE_RECT)

        SINGLE_BACK = Button(image=None, pos=(350, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        SINGLE_BACK.changeColor(SINGLE_MOUSE_POS)
        SINGLE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SINGLE_BACK.checkForInput(SINGLE_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def multi():
    while True:
        SCREEN.blit(BG, (0, 0))

        MULTI_MOUSE_POS = pygame.mouse.get_pos()

        # SCREEN.fill("black")

        MULTI_TEXT = get_font(100).render("GAMEMODE", True, "#b68f40")
        MULTI_RECT = MULTI_TEXT.get_rect(center=(350, 100))
        SCREEN.blit(MULTI_TEXT, MULTI_RECT)

        MULTI_LOCAL = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(350, 250),
                              text_input="LOCAL", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MULTI_ONLINE = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(350, 400),
                            text_input="ONLINE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MULTI_BACK = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(350, 550),
                              text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [MULTI_LOCAL, MULTI_ONLINE, MULTI_BACK]:
            button.changeColor(MULTI_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MULTI_LOCAL.checkForInput(MULTI_MOUSE_POS):
                    set_selection(1)
                    # pygame.quit()
                    # sys.exit()
                    selection1()
                    print(selection)
                if MULTI_ONLINE.checkForInput(MULTI_MOUSE_POS):
                    set_selection(3)
                if MULTI_BACK.checkForInput(MULTI_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(350, 100))

        SINGLE_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(350, 250),
                             text_input="SINGLEPLAYER", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MULTI_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(350, 400),
                                text_input="MULTIPLAYER", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(350, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [SINGLE_BUTTON, MULTI_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SINGLE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    single()
                if MULTI_BUTTON.checkForInput(MENU_MOUSE_POS):
                    multi()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
