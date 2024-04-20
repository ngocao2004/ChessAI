import pygame, sys
import Button
import ChessMain

pygame.init()

WIDTH = 768 
HEIGHT = 768
SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Menu")

BG = pygame.transform.scale(
    pygame.image.load("Chess/assets/menu/Background(1).png"),
    (WIDTH, HEIGHT),
)


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Chess/assets/menu/font.ttf", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        # PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button.Button(
            image=None,
            pos=(WIDTH * 0.5, HEIGHT * 0.75),
            text_input="BACK",
            font=get_font(75),
            base_color="White",
            hovering_color="Green",
        )
        PvP_BUTTON = Button.Button(
            image=None,  # image=pygame.image.load("Chess/assets/menu/PvP.png"),
            pos=(WIDTH * 0.5, HEIGHT * 0.25),
            text_input="PvP",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        PvE_BUTTON = Button.Button(
            image=None,  # image=pygame.image.load("Chess/assets/menu/PvE.png"),
            pos=(WIDTH * 0.5, HEIGHT * 0.5),
            text_input="PvE",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        for button in [PLAY_BACK, PvP_BUTTON, PvE_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PvE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    ChessMain.play_with_player(False)
                if PvP_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    ChessMain.play_with_player(True)
        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        # OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button.Button(
            image=None,
            pos=(WIDTH / 2, 460),
            text_input="BACK",
            font=get_font(75),
            base_color="Black",
            hovering_color="Green",
        )

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("CHESS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH * 0.5, HEIGHT * 0.15))

        PLAY_BUTTON = Button.Button(
            image=None,  # image=pygame.image.load("Chess/assets/menu/Play Rect.png"),
            pos=(WIDTH * 0.5, HEIGHT * 0.4),
            text_input="PLAY",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        OPTIONS_BUTTON = Button.Button(
            image=None,  # image=pygame.image.load("Chess/assets/menu/Options Rect.png"),
            pos=(WIDTH * 0.5, HEIGHT * 0.6),
            text_input="OPTIONS",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        QUIT_BUTTON = Button.Button(
            image=None,  # image=pygame.image.load("Chess/assets/menu/Quit Rect.png"),
            pos=(WIDTH * 0.5, HEIGHT * 0.8),
            text_input="QUIT",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
