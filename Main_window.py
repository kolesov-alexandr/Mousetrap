import pygame
import os
import sys

CURRENT_VOLUME = 0.5


# ну тут сверху надеюсь все понятно


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
        return image


# ну вот тут обычная функция загрузки изображения


def terminate():
    pygame.quit()
    sys.exit()


def main_menu():
    pygame.mixer.music.load("data/Mantis.mp3")
    pygame.mixer.music.set_volume(CURRENT_VOLUME)
    pygame.mixer.music.play()
    mouse_pos = (0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_sprites.update(mouse_pos, event)
        button_sprites.update(mouse_pos)
        screen.fill(pygame.Color("mediumblue"))
        back_ground_sprites_1.draw(screen)
        button_sprites.draw(screen)
        pygame.display.flip()
        timer.tick(7)


def option_window():
    mouse_pos = (0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                options_buttons_sprites.update(mouse_pos, event)
        options_buttons_sprites.update(mouse_pos)
        screen.fill("mediumblue")
        options_buttons_sprites.draw(screen)
        pygame.display.flip()


class MainMenuButton(pygame.sprite.Sprite):
    # это класс для кнопок в главном меню
    # для кнопок должно быть 2 картинки, одна светлая, другая темнее
    # когда мышка будет наводится на кнопку надо чтобы одна картинка меняла другую
    # и когда мышка уводится с кнопки обратно на первую
    def __init__(self, picture_name, *group):
        super().__init__(*group)
        self.image = load_image(picture_name)
        self.rect = self.image.get_rect()
        # инициализация

    def set_coords(self, x, y):
        # функция для выставления значений координат спрайта
        self.rect.x = x
        self.rect.y = y


class PlayGameButton(MainMenuButton):
    def __init__(self, names, next_window, *group):
        super().__init__(names[0], *group)
        self.names = names
        self.next_window = next_window
        self.stack = 0

    def update(self, mouse_pos, *args):
        if self.rect.collidepoint(mouse_pos):
            if self.stack == 0:
                self.image = load_image(self.names[1])
            else:
                self.image = load_image(self.names[2])
            self.stack = (self.stack + 1) % 2
            if args and args[0].type == pygame.MOUSEBUTTONDOWN:
                if self.next_window == 'exit':
                    terminate()
                if self.next_window == 'option_window':
                    option_window()
        else:
            self.image = load_image(self.names[0])


class OptionsButton(MainMenuButton):
    def __init__(self, name, sound, *group):
        super().__init__(name, *group)
        self.sound = sound

    def update(self, mouse_pos, *args):
        global CURRENT_VOLUME
        if self.rect.collidepoint(mouse_pos) and args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.sound == 'up':
                if int(CURRENT_VOLUME * 10) < 11:
                    CURRENT_VOLUME += 0.1
            else:
                if int(CURRENT_VOLUME * 10) > 0:
                    CURRENT_VOLUME -= 0.1
            pygame.mixer.music.set_volume(CURRENT_VOLUME)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 450, 550
    screen = pygame.display.set_mode(size)
    button_sprites = pygame.sprite.Group()

    back_ground_sprites_1 = pygame.sprite.Group()

    options_buttons_sprites = pygame.sprite.Group()

    back_ground_1 = pygame.sprite.Sprite(back_ground_sprites_1)
    back_ground_1.image = load_image('back_ground_1.png')
    back_ground_1.rect = back_ground_1.image.get_rect()
    back_ground_1.rect.x = 0
    back_ground_1.rect.y = 0

    play_button = PlayGameButton(('play1.png', 'play2.png', 'play3.png'), 'name_window',
                                 button_sprites)
    play_button.set_coords(150, 50)
    options_button = PlayGameButton(('options1.png', 'options2.png', 'options3.png'), 'option_window',
                                    button_sprites)
    options_button.set_coords(150, 150)
    exit_button = PlayGameButton(('exit1.png', 'exit2.png', 'exit3.png'), 'exit', button_sprites)
    exit_button.set_coords(150, 350)

    sound_up_button = OptionsButton("sound.png", "up", options_buttons_sprites)
    sound_up_button.set_coords(50, 50)

    sound_down_button = OptionsButton("sound_off.png", "down", options_buttons_sprites)
    sound_down_button.set_coords(250, 50)

    timer = pygame.time.Clock()
    main_menu()
    pygame.quit()
