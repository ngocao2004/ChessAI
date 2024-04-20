import pygame, sys
import Button
import ChessMain

pygame.init()

WIDTH = HEIGHT = 768
SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Menu")

BG = pygame.transform.scale(
    pygame.image.load("Chess/assets/menu/Background(1).png"),
    (WIDTH, HEIGHT),
)


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Chess/assets/menu/font.ttf", size)


def play_menu():
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
                    ChessMain.play_with_player()
                if PvP_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    ChessMain.play_with_player()
        pygame.display.update()


def guide_menu():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))

        GUIDE1_TEXT = get_font(60).render("Z : Undo", True, "WHITE")
        GUIDE1_RECT = GUIDE1_TEXT.get_rect(center=(WIDTH / 2, HEIGHT * 0.2))
        SCREEN.blit(GUIDE1_TEXT, GUIDE1_RECT)

        GUIDE2_TEXT = get_font(60).render("R : Reset", True, "WHITE")
        GUIDE2_RECT = GUIDE2_TEXT.get_rect(center=(WIDTH / 2, HEIGHT * 0.4))
        SCREEN.blit(GUIDE2_TEXT, GUIDE2_RECT)

        GUILD3_TEXT = get_font(60).render("Esc : Pause", True, "WHITE")
        GUIDE3_RECT = GUILD3_TEXT.get_rect(center=(WIDTH / 2, HEIGHT * 0.6))
        SCREEN.blit(GUILD3_TEXT, GUIDE3_RECT)

        OPTIONS_BACK = Button.Button(
            image=None,
            pos=(WIDTH / 2, WIDTH * 0.8),
            text_input="BACK",
            font=get_font(75),
            base_color="White",
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


def pause_menu():
    while True:
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))

        HOME_BUTTON = Button.Button(
            image=None,
            pos=(WIDTH / 2, WIDTH * 0.2),
            text_input="HOME",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="GREEN",
        )

        RESUME_BUTTON = Button.Button(
            image=None,
            pos=(WIDTH / 2, WIDTH * 0.4),
            text_input="RESUME",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        RESTART_BACK = Button.Button(
            image=None,
            pos=(WIDTH / 2, WIDTH * 0.6),
            text_input="RESTART",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        QUIT_BUTTON = Button.Button(
            image=None,  # image=pygame.image.load("Chess/assets/menu/Quit Rect.png"),
            pos=(WIDTH * 0.5, HEIGHT * 0.8),
            text_input="QUIT",
            font=get_font(75),
            base_color="WHITE",
            hovering_color="RED",
        )

        for button in [RESUME_BUTTON, RESTART_BACK, HOME_BUTTON, QUIT_BUTTON]:
            button.changeColor(PAUSE_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    continue
                if RESTART_BACK.checkForInput(PAUSE_MOUSE_POS):
                    continue
                if HOME_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    main_menu()
                if QUIT_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def end_menu():
    while True:
        END_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))

        HOME_BUTTON = Button.Button(
            image=None,
            pos=(WIDTH / 2, WIDTH * 0.3),
            text_input="HOME",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="GREEN",
        )

        RESTART_BACK = Button.Button(
            image=None,
            pos=(WIDTH / 2, WIDTH * 0.5),
            text_input="RESTART",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        QUIT_BUTTON = Button.Button(
            image=None,  # image=pygame.image.load("Chess/assets/menu/Quit Rect.png"),
            pos=(WIDTH * 0.5, HEIGHT * 0.7),
            text_input="QUIT",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="RED",
        )

        for button in [HOME_BUTTON, RESTART_BACK, QUIT_BUTTON]:
            button.changeColor(END_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HOME_BUTTON.checkForInput(END_MOUSE_POS):
                    main_menu()
                if RESTART_BACK.checkForInput(END_MOUSE_POS):
                    continue
                if QUIT_BUTTON.checkForInput(END_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

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
        GUIDE_BUTTON = Button.Button(
            image=None,  # image=pygame.image.load("Chess/assets/menu/Options Rect.png"),
            pos=(WIDTH * 0.5, HEIGHT * 0.6),
            text_input="GUIDE",
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
            hovering_color="RED",
        )

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, GUIDE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_menu()
                if GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    guide_menu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    end_menu()
