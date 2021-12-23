import pygame
import os
import sys


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
    pygame.mixer.music.set_volume(0.1)
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
        screen.fill((0, 0, 0))
        button_sprites.draw(screen)
        pygame.display.flip()
        timer.tick(7)


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

    def update(self, *args):
        x, y = args[0]
        if (x in range(self.rect[0], self.rect[0] + self.rect[2])
                and y in range(self.rect[1], self.rect[1] + self.rect[3])):
            if self.stack == 0:
                self.image = load_image(self.names[1])
            else:
                self.image = load_image(self.names[2])
            self.stack = (self.stack + 1) % 2
            if len(args) == 2 and args[1].type == pygame.MOUSEBUTTONDOWN:
                if self.next_window == 'exit':
                    terminate()
        else:
            self.image = load_image(self.names[0])


if __name__ == '__main__':
    pygame.init()
    size = width, height = 450, 550
    screen = pygame.display.set_mode(size)
    button_sprites = pygame.sprite.Group()
    play_button = PlayGameButton(('play1.png', 'play2.png', 'play3.png'), 'name_window',
                                 button_sprites)
    play_button.set_coords(150, 100)
    exit_button = PlayGameButton(('exit1.png', 'exit2.png', 'exit3.png'), 'exit', button_sprites)
    exit_button.set_coords(150, 400)
    timer = pygame.time.Clock()
    main_menu()
    pygame.quit()
