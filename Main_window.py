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


class MainMenuButton(pygame.sprite.Sprite):
    # это класс для кнопок в главном меню
    # для кнопок должно быть 2 картинки, одна светлая, другая темнее
    # когда мышка будет наводится на кнопку надо чтобы одна картинка меняла другую
    # и когда мышка уводится с кнопки обратно на первую
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("main_menu_button_0.png")
        self.rect = self.image.get_rect()
        # инициализация

    def set_coords(self, x, y):
        # функция для выставления значений координат спрайта
        self.rect.x = x
        self.rect.y = y

    def update(self, mouse_pos):
        x, y = mouse_pos
        if (x in range(self.rect[0], self.rect[0] + self.rect.x)
                and y in range(self.rect[1], self.rect[1] + self.rect.y)):
            self.image = load_image("main_menu_button_1.png")
        else:
            self.image = load_image("main_menu_button_0.png")


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1024, 1024
    screen = pygame.display.set_mode(size)
    button_sprites = pygame.sprite.Group()
    button_1 = MainMenuButton(button_sprites)
    button_1.set_coords(500, 500)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                button_sprites.update(event.pos)
        screen.fill((0, 0, 0))
        button_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
