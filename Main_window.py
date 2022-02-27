from random import randrange

import pygame
import os
import sys
import sqlite3

FPS = 60
SCORE = 0
DOWN = 0
UP = 1
OPTION_WINDOW_OPEN = False
RECORDS_WINDOW_OPEN = False

RED_BUTTON = pygame.K_z
BLUE_BUTTON = pygame.K_x

NOTES = ["don.png", "kacu.png"]

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
    with open("volume.txt") as volume_file:
        strings = [elem.strip() for elem in volume_file.readlines()]
    current_volume = float(strings[0])
    pygame.mixer.music.load("data/music1.mp3")
    pygame.mixer.music.set_volume(current_volume)
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
    screen = pygame.display.set_mode((552, 468))

    obstacle_event = pygame.USEREVENT + 1

    first_melody_timings = [3.5107907000000003, 0.3594379000000001, 0.40778619999999943,
                            0.39205380000000023, 0.3999587, 0.45603640000000034,
                            0.4399856, 0.4640217999999994, 0.45600229999999975, 0.43322959999999977,
                            0.4547074000000011, 0.1773264999999995, 0.08077630000000013, 0.11045079999999885,
                            0.055881600000001086, 0.1436036999999999, 0.07216619999999985, 0.8239526000000001,
                            0.23982050000000044, 0.4729478999999994, 0.0796013999999996, 0.11982679999999846,
                            0.08088910000000027, 0.8787427000000001, 0.1999809999999993, 0.08000940000000156,
                            0.4563512000000003, 0.0895949999999992, 0.10218230000000084, 0.0566620000000011,
                            0.1671711000000009, 0.784873000000001, 0.135200600000001, 0.08020529999999937,
                            0.11174709999999877, 0.40802590000000016, 0.11196480000000086, 0.08839659999999938,
                            0.11160549999999958, 0.14822440000000014, 0.6917624, 0.1040308999999997,
                            0.08923009999999998, 0.10276469999999982, 0.07281240000000011, 0.3671396999999992,
                            0.10403529999999961, 0.14413100000000156, 0.21614569999999844, 0.24787029999999888,
                            0.23181070000000048, 0.34406410000000065, 0.3120895000000026, 0.2638283000000001,
                            0.19198109999999957, 0.27203150000000065, 0.43199440000000067, 0.4160864999999987,
                            0.335938800000001, 0.21612560000000158, 0.24786399999999986, 0.27344710000000205,
                            0.4865534000000018, 0.3919789000000016, 0.3200780999999999, 0.26420750000000126,
                            0.1043883000000001, 0.2393548999999986, 0.055969100000002214, 0.1444989999999997,
                            0.32747429999999866, 0.3999486999999995, 0.3520503000000019, 0.08821239999999975,
                            0.1437849, 0.29600099999999685, 0.2480916000000022, 0.4719218999999981, 0.360673300000002,
                            0.33542190000000005, 0.11193309999999812, 0.23992849999999777, 0.27199379999999707,
                            0.2959928000000005, 0.20798750000000155, 0.40022249999999815, 0.31978750000000034,
                            0.10448279999999954, 0.1288917999999981, 0.3425876999999993, 0.23224719999999976,
                            0.46377939999999995, 0.36798049999999805, 0.3600028000000002, 0.11199140000000085,
                            0.15201240000000027, 0.1839940999999996, 0.2960335999999977, 0.2088031000000008,
                            0.2391728999999998, 0.35207809999999995, 0.2961653999999996, 0.12780030000000053,
                            0.11330419999999819, 0.15868899999999897, 0.2721868999999977, 0.19171049999999923,
                            0.41602679999999737, 0.33683839999999776, 0.3032033999999939, 0.1519462000000047,
                            0.12064780000000042, 0.30338259999999906, 0.23274179999999944, 0.45530799999999516,
                            0.3599722000000014, 0.32002549999999985, 0.09590029999999672, 0.17687489999999428,
                            0.3126255000000029, 0.2304711000000026, 0.4080695000000034, 0.3999802000000017,
                            0.3839973999999984, 0.15199989999999985, 0.3200171999999952, 0.2251753999999977,
                            0.29499330000000157, 0.24000639999999862, 0.31985450000000526, 0.24136090000000365,
                            0.22251909999999953, 0.26403179999999793, 0.23445999999999856, 0.26152790000000437,
                            0.34402960000000604, 0.4163330000000016, 0.31160340000000275, 0.1604555999999988,
                            0.2875725000000031, 0.24799349999999976, 0.21599150000000122, 0.08125880000000052,
                            0.10274009999999834, 0.04874390000000517, 0.21576929999999805, 0.31149030000000266,
                            0.25613279999999605, 0.22550009999999787, 0.27042769999999905, 0.21589889999999912,
                            0.328029199999996, 0.16000220000000098, 0.3280171999999979, 0.288027900000003,
                            0.10444439999999844, 0.11947719999999862, 0.32006179999999773, 0.23995030000000384,
                            0.43201399999999524, 0.09600110000000228, 0.11250940000000043, 0.23949509999999918,
                            0.12799680000000535, 0.3520846999999989, 0.4898106999999996, 0.5100578999999996,
                            0.41597729999999444, 0.23199329999999918, 0.23202739999999977, 0.24801270000000386,
                            0.2320338000000035, 0.22394950000000335, 0.2239834000000016, 0.1920442000000051,
                            0.336063799999998, 0.27204089999999326, 0.14460679999999826, 0.19144010000000122,
                            0.28852930000000043, 0.2072941000000057, 0.448871000000004, 0.3991074999999995,
                            0.320000499999999, 0.17601359999999744, 0.26482539999999943, 0.3111766999999972,
                            0.24798210000000154, 0.2399842000000021, 0.3055936000000017, 0.2873512999999974,
                            0.191424099999999, 0.20761849999999527, 0.21600219999999837, 0.23316670000000528,
                            0.44684879999999794, 0.4880071999999984, 0.4561092000000002, 0.46387860000000103,
                            0.4959811000000016, 0.471994500000001, 0.43997889999999984, 0.5120378000000017,
                            0.447960099999996, 0.5280132000000037, 0.4243531000000047, 0.49566130000000186,
                            0.46410739999999606, 0.48000189999999776, 0.4656484000000063, 0.510243899999999,
                            0.48014789999999863, 0.5117866999999947, 0.37615160000000003, 0.19983649999999642,
                            0.16801780000000122, 0.11201009999999201, 0.11203049999998882, 0.5521305000000041,
                            0.1284469999999942, 0.1353983999999997, 0.08929449999999406, 0.1186942000000073,
                            0.26501399999999364, 0.19100720000000138, 0.10500989999999888, 0.13497359999999503,
                            0.10525410000001045, 0.5827148999999991, 0.17599069999999983, 0.1520263999999969,
                            0.08087790000000439, 0.11910980000000393, 0.08875749999999982, 0.15185929999999814,
                            0.279453100000012, 0.12792919999999697, 0.09636370000001193, 0.12760839999999973,
                            0.664057200000002, 0.08862659999999778, 0.1272971999999868, 0.10400070000000028]
    first_level = [randrange(0, 2) for _ in first_melody_timings]
    level = first_level[:]
    print(level)
    timings = first_melody_timings[:]
    counter = 0
    counter_max = len(level)

    pygame.time.set_timer(obstacle_event, round(timings[counter] * 1000))

    up = False
    down = False
    odd = True
    color = None
    while True:
        if odd:
            color = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == RED_BUTTON:
                    color = 'red'
                if event.key == BLUE_BUTTON:
                    color = 'blue'
            # if event.type == pygame.KEYUP:
            #     if event.key == RED_BUTTON:
            #         color = None
            #     if event.key == BLUE_BUTTON:
            #         color = None
            if event.type == obstacle_event:
                if counter < counter_max:
                    create_note(NOTES[level[counter]])
                    pygame.time.set_timer(obstacle_event, round(timings[counter] * 1000))
                    counter += 1
        score_point_sprites.update()
        obstacle_sprites.update()
        cat_sprites.update(up, down)
        taiko_sprite.update(color)
        screen.fill(pygame.Color("magenta"))
        back_ground_sprites_2.draw(screen)
        taiko_hit_box_spr.draw(screen)
        game_object_sprites.draw(screen)
        cat_sprites.draw(screen)
        taiko_sprite.draw(screen)
        pygame.display.flip()
        odd = not odd
        timer.tick(FPS)


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
    mouse_pos = (0, 0)
    while RECORDS_WINDOW_OPEN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                con.close()
                terminate()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                options_buttons_sprites.update(mouse_pos, event)

        records_button_sprite.update(mouse_pos)
        records_button_sprite.draw(screen)
        pygame.display.flip()


def loading_window():
    rabbit = load_image("rabbit.png")
    screen.blit(rabbit, (0, 0))
    font = pygame.font.Font(None, 30)
    text1 = font.render("Wonderland Engine", True, pygame.Color("black"))
    text1_x = 250
    text1_y = 200
    screen.blit(text1, (text1_x, text1_y))
    text2 = font.render("X", True, pygame.Color("black"))
    text2_x = text1_x + text1.get_width() // 2 - text2.get_width() // 2
    text2_y = text1_y + 50
    screen.blit(text2, (text2_x, text2_y))
    text3 = font.render("PyGame", True, pygame.Color("black"))
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
    while OPTION_WINDOW_OPEN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                options_buttons_sprites.update(mouse_pos, event)
        options_buttons_sprites.update(mouse_pos)
        screen.fill("magenta")
        back_ground_sprites_1.draw(screen)
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


def winner_window():
    font = pygame.font.Font(None, 30)
    text = font.render("Поздравляю, вы прошли уровень!", True, pygame.Color('red'))
    screen.blit(text, (55, 50))
    image = load_image('win.png')
    image_rect = 75, 125
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
        global OPTION_WINDOW_OPEN
        global RECORDS_WINDOW_OPEN
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
                    RECORDS_WINDOW_OPEN = True
                    records()
                if self.next_window == 'options':
                    OPTION_WINDOW_OPEN = True
                    option_window()
        else:
            self.image = load_image(self.names[0])


class OptionsButton(MainSprite):
    def __init__(self, name, sound, *group):
        super().__init__(name, *group)
        self.sound = sound

    def update(self, mouse_pos, *args):
        global OPTION_WINDOW_OPEN
        global CURRENT_VOLUME
        global RECORDS_WINDOW_OPEN
        with open("volume.txt") as volume_file:
            strings = [elem.strip() for elem in volume_file.readlines()]
        current_volume = float(strings[0])
        if self.rect.collidepoint(mouse_pos) and args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.sound == 'up':
                if int(current_volume * 10) < 11:
                    current_volume = round(current_volume + 0.1, 1)
            elif self.sound == 'down':
                if int(current_volume * 10) > 0:
                    current_volume = round(current_volume - 0.1, 1)
            else:
                OPTION_WINDOW_OPEN = False
                RECORDS_WINDOW_OPEN = False
            pygame.mixer.music.set_volume(current_volume)
            with open("volume.txt", "w") as volume_file:
                volume_file.write(str(current_volume))


class Cat(MainSprite):
    def __init__(self, *args):
        super().__init__('cat.png', game_object_sprites, cat_sprites, *args)
        self.stack = 0
        self.run_images = ["cat.png", "cat_2.png", "cat_3.png"]
        self.up = False
        self.down = False
        self.set_coords(50, 600)

    def update(self, *orders):
        if orders[0]:
            pass

        elif orders[1]:
            pass

        else:
            self.up = False
            self.down = False
            self.image = load_image(self.run_images[self.stack // 5])
            self.rect = self.image.get_rect()
            self.set_coords(100, 375)
            self.stack = (self.stack + 1) % 15

    def status(self):
        return self.up, self.down


class Note(MainSprite):
    def __init__(self, note_image):
        super().__init__(note_image, game_object_sprites, obstacle_sprites)
        self.note = note_image[:-4]
        self.set_coords(445, 25)

    def update(self):
        global SCORE
        speed = -480 / FPS
        self.rect = self.rect.move(speed, 0)
        if (pygame.sprite.spritecollideany(self, taiko_hit_box_spr) and ((self.note == 'kacu' and taiko.stance == 'blue')
           or (self.note == 'don' and taiko.stance == 'red'))):
            SCORE += 20
            self.kill()
        if self.rect.x <= 0:
            self.kill()


class Taiko(MainSprite):
    def __init__(self, *args):
        super().__init__('taiko_empty.png', game_object_sprites, taiko_sprite, *args)
        self.set_coords(50, 15)
        self.stance = None

    def update(self, color):
        self.stance = color
        if color == 'blue':
            self.image = load_image('taiko_blue.png')
        elif color == 'red':
            self.image = load_image('taiko_red.png')
        else:
            self.image = load_image('taiko_empty.png')
            self.stance = None


def create_note(note):
    Note(note)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 450, 550
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color("magenta"))

    button_sprites = pygame.sprite.Group()
    back_ground_sprites_1 = pygame.sprite.Group()
    back_ground_sprites_2 = pygame.sprite.Group()
    options_buttons_sprites = pygame.sprite.Group()

    game_object_sprites = pygame.sprite.Group()
    cat_sprites = pygame.sprite.Group()
    score_point_sprites = pygame.sprite.Group()
    cat_hit_box_sprite = pygame.sprite.Group()
    obstacle_sprites = pygame.sprite.Group()
    records_button_sprite = pygame.sprite.Group()
    taiko_sprite = pygame.sprite.Group()
    taiko_hit_box_spr = pygame.sprite.Group()

    back_ground_1 = pygame.sprite.Sprite(back_ground_sprites_1)
    back_ground_1.image = load_image('back_ground_1.png')
    back_ground_1.rect = back_ground_1.image.get_rect()
    back_ground_1.rect.x = 0
    back_ground_1.rect.y = 0

    back_ground_2 = pygame.sprite.Sprite(back_ground_sprites_2)
    back_ground_2.image = load_image('back_ground_2.png')
    back_ground_2.rect = back_ground_1.image.get_rect()
    back_ground_2.rect.x = 0
    back_ground_2.rect.y = 0

    taiko_field = pygame.sprite.Sprite(game_object_sprites)
    taiko_field.image = load_image('circle_field.png')
    taiko_field.rect = taiko_field.image.get_rect()
    taiko_field.rect.x = 0
    taiko_field.rect.y = 15

    taiko_hit_box = pygame.sprite.Sprite(taiko_hit_box_spr)
    taiko_hit_box.image = load_image('taiko_hit_box.png')
    taiko_hit_box.rect = taiko_hit_box.image.get_rect()
    taiko_hit_box.rect.x = 110
    taiko_hit_box.rect.y = 75

    taiko = Taiko()

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

    back_button = OptionsButton("arrow_left.png", "exit", options_buttons_sprites,
                                records_button_sprite)
    back_button.set_coords(40, 480)



    timer = pygame.time.Clock()
    loading_window()
    pygame.quit()
