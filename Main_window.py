import pygame
import os
import sys
import sqlite3

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
    pygame.mixer.music.play(-1)
    mouse_pos = (0, 0)
    screen.fill(pygame.Color("magenta"))
    button_sprites.draw(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_sprites.update(mouse_pos, event)
        button_sprites.update(mouse_pos)
        screen.fill(pygame.Color("magenta"))
        back_ground_sprites_1.draw(screen)
        button_sprites.draw(screen)
        pygame.display.flip()
        timer.tick(7)


def game():
    global screen
    screen = pygame.display.set_mode((600, 500))

    obstacle_event = pygame.USEREVENT + 1

    level = [0, 1, 0, 1, 0, 0, 0, 0]
    counter = 0
    counter_max = len(level)

    pygame.time.set_timer(obstacle_event, 1000)

    up = False
    down = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    up = True
                if event.key == pygame.K_DOWN:
                    down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_DOWN:
                    down = False
            if event.type == obstacle_event:
                if counter < counter_max:
                    create_obstacle(level, counter)
                    counter += 1
        obstacle_sprites.update()
        cat_sprites.update(up, down)
        screen.fill(pygame.Color("magenta"))
        game_object_sprites.draw(screen)
        cat_sprites.draw(screen)
        pygame.display.flip()
        timer.tick(60)


def records():
    # вывод таблицы с рекордами
    con = sqlite3.connect('data/records.sqlite')
    cur = con.cursor()
    screen.fill(pygame.Color("magenta"))
    result = cur.execute("""SELECT name, kol_vo_score FROM records
            ORDER BY kol_vo_score DESC""").fetchall()

    font = pygame.font.Font(None, 30)
    font_header = pygame.font.Font(None, 40)
    header_player = font_header.render("Игрок", True, pygame.Color('cyan'))
    screen.blit(header_player, (95, 45))

    header_score = font_header.render("Очки", True, pygame.Color('cyan'))
    screen.blit(header_score, (95 + header_player.get_width() + 115, 45))
    height0 = 45 + 50
    for i in range(10):
        if i < len(result):
            player = font.render(result[i][0], True, pygame.Color('cyan'))
            screen.blit(player, (95 + 15, height0))

            score = font.render('{:04}'.format(result[i][1]), True, pygame.Color('cyan'))
            screen.blit(score, (95 + header_player.get_width() + 115 + 12, height0))

        else:
            player = font.render('NON', True, pygame.Color('cyan'))
            screen.blit(player, (95 + 15, height0))

            score = font.render('{:04}'.format(0), True, pygame.Color('cyan'))
            screen.blit(score, (95 + header_player.get_width() + 115 + 12, height0))
        height0 += 41
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                con.close()
                terminate()


def loading_window():
    rabbit = load_image("rabbit.png")
    screen.blit(rabbit, (50, 100))
    font = pygame.font.Font(None, 30)
    text1 = font.render("Wonderland Engine", True, pygame.Color("yellow"))
    text1_x = 250
    text1_y = 200
    screen.blit(text1, (text1_x, text1_y))
    text2 = font.render("X", True, pygame.Color("yellow"))
    text2_x = text1_x + text1.get_width() // 2 - text2.get_width() // 2
    text2_y = text1_y + 50
    screen.blit(text2, (text2_x, text2_y))
    text3 = font.render("PyGame", True, pygame.Color("yellow"))
    text3_x = text2_x + text2.get_width() // 2 - text3.get_width() // 2
    text3_y = text2_y + 50
    screen.blit(text3, (text3_x, text3_y))
    pygame.display.flip()
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        if count < 3:
            count += 1 * timer.tick() / 1000
        else:
            main_menu()
        pygame.display.flip()


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
        screen.fill("magenta")
        options_buttons_sprites.draw(screen)
        pygame.display.flip()


def game_over():
    font = pygame.font.Font(None, 30)
    text = font.render("Увы, вы проиграли(", True, pygame.Color('red'))
    screen.blit(text, (130, 50))
    image = load_image('game_over.png')
    image_rect = 75, 125
    image = pygame.transform.scale(image, (300, 300))
    screen.blit(image, image_rect)
    pygame.display.flip()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()


class MainSprite(pygame.sprite.Sprite):
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


class Button(MainSprite):
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
                if self.next_window == 'play':
                    game()
                if self.next_window == 'records':
                    records()
                if self.next_window == 'options':
                    option_window()
        else:
            self.image = load_image(self.names[0])


class OptionsButton(MainSprite):
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


class Cat(MainSprite):
    def __init__(self):
        super().__init__('cat.png', game_object_sprites, cat_sprites)
        self.up = False
        self.down = False

    def update(self, *orders):
        if orders[0]:
            self.set_coords(100, 100)
            self.up = True
            self.down = False

        elif orders[1]:
            self.set_coords(100, 300)
            self.up = False
            self.down = True
        else:
            self.set_coords(100, 300)
            self.up = False
            self.down = False

    def status(self):
        return self.up, self.down


class Obstacle(MainSprite):
    def __init__(self, pos):
        super().__init__('obstacle.png', game_object_sprites, obstacle_sprites)
        self.set_coords(pos[0], pos[1])

    def update(self, *orders):
        self.rect = self.rect.move(-20, 0)
        if pygame.sprite.spritecollideany(self, cat_sprites) and (cat.status()[0] or
                                                                  cat.status()[1]):
            self.kill()


def create_obstacle(level, i):
    if level[i] == 0:
        Obstacle((400, 100))
    else:
        Obstacle((400, 300))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 450, 550
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color("magenta"))

    button_sprites = pygame.sprite.Group()
    game_object_sprites = pygame.sprite.Group()
    cat_sprites = pygame.sprite.Group()
    obstacle_sprites = pygame.sprite.Group()
    back_ground_sprites_1 = pygame.sprite.Group()
    options_buttons_sprites = pygame.sprite.Group()

    back_ground_1 = pygame.sprite.Sprite(back_ground_sprites_1)
    back_ground_1.image = load_image('back_ground_1.png')
    back_ground_1.rect = back_ground_1.image.get_rect()
    back_ground_1.rect.x = 0
    back_ground_1.rect.y = 0

    cat = Cat()
    cat.set_coords(100, 300)

    play_button = Button(('play1.png', 'play2.png', 'play3.png'), 'play', button_sprites)
    play_button.set_coords(150, 50)

    options_button = Button(('options1.png', 'options2.png', 'options3.png'), 'options',
                            button_sprites)
    options_button.set_coords(150, 150)

    records_button = Button(('records1.png', 'records2.png', 'records3.png'), 'records',
                            button_sprites)
    records_button.set_coords(150, 250)

    exit_button = Button(('exit1.png', 'exit2.png', 'exit3.png'), 'exit', button_sprites)
    exit_button.set_coords(150, 350)

    sound_up_button = OptionsButton("sound.png", "up", options_buttons_sprites)
    sound_up_button.set_coords(50, 50)

    sound_down_button = OptionsButton("sound_off.png", "down", options_buttons_sprites)
    sound_down_button.set_coords(250, 50)

    timer = pygame.time.Clock()
    loading_window()
    pygame.quit()
