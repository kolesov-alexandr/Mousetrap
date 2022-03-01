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
VOCABULARY = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

RED_BUTTON = pygame.K_z
BLUE_BUTTON = pygame.K_x

VOLUME = 0.0

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
    global VOLUME
    with open("volume.txt") as volume_file:
        strings = [elem.strip() for elem in volume_file.readlines()]
    VOLUME = float(strings[0])
    pygame.mixer.music.load("data/main_menu_theme.mp3")
    pygame.mixer.music.set_volume(VOLUME)
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
    global VOLUME
    pygame.mixer.music.load("data/music1.mp3")
    pygame.mixer.music.load("data/m_cot_bezhit_pod_phonk.mp3")
    pygame.mixer.music.set_volume(VOLUME)

    screen = pygame.display.set_mode((552, 468))

    obstacle_event = pygame.USEREVENT + 1

    first_level = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0,
                   1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0,
                   1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                   0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
                   1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                   0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    first_timings = [3.3896107000000004, 0.41562829999999984, 0.3842290000000004,
                     0.39177570000000017, 0.47195490000000007, 0.4319999000000001, 0.4560556,
                     0.47197330000000015, 0.4560038000000004, 0.4559899000000005,
                     0.5439984999999998, 0.2079664999999995, 0.18449120000000008,
                     1.0475451000000007, 0.2240050999999994, 0.41597229999999996,
                     0.24800999999999895, 0.17596860000000092, 0.7439905999999983,
                     0.2002127999999992, 0.37580849999999977, 0.23999499999999863,
                     0.08799189999999868, 1.0640176000000015, 0.19994289999999992,
                     0.4000244999999989, 0.25599479999999986, 0.2159986000000007,
                     0.6800069000000004, 0.2159885999999993, 0.20005390000000034,
                     0.43203429999999976, 0.19192490000000006, 0.6400062999999996,
                     0.4319891000000027, 0.4480167999999978, 0.5120041999999998, 0.5201243999999967,
                     0.4158414999999991, 0.46409519999999915, 0.4958832000000015,
                     0.5600386000000022, 0.40795900000000174, 0.49608710000000045,
                     0.2479148000000002, 0.27201599999999715, 0.47196950000000015,
                     0.4160454999999992, 0.359967300000001, 0.24798710000000312,
                     0.24001150000000138, 0.24001799999999918, 0.43997360000000185,
                     0.4000485000000005, 0.47198609999999874, 0.3039778999999996,
                     0.2719628000000007, 0.47200629999999677, 0.43998849999999834,
                     0.48001700000000014, 0.5040293000000027, 0.5439697000000017,
                     0.41599959999999925, 0.4639957000000017, 0.4640100000000018,
                     0.5200099999999992, 0.4080420000000018, 0.29590789999999956,
                     0.23198700000000017, 0.28801580000000016, 0.2799896000000004,
                     0.47203000000000017, 0.38397669999999806, 0.5120068000000018,
                     0.4639796999999959, 0.5360432000000017, 0.3919659000000024,
                     0.37604429999999667, 0.2558732999999975, 0.4481009, 0.4399328999999952,
                     0.4400217000000026, 0.40006389999999925, 0.5279518999999979,
                     0.5201141000000007, 0.42386409999999586, 0.4480195000000009,
                     0.5439621000000017, 0.48001490000000047, 0.4400000999999989,
                     0.44800759999999684, 0.49598720000000185, 0.24002109999999988,
                     0.3439752000000027, 0.3600081000000017, 0.4960550999999995,
                     0.31993169999999793, 0.2959928000000005, 0.4560256000000038,
                     0.4239809999999977, 0.46397980000000416, 0.45603129999999936,
                     0.6079879999999989, 0.43200530000000015, 0.456353, 0.4556685000000016,
                     0.5279535000000024, 0.4239996000000019, 0.45603219999999567,
                     0.3520821999999981, 0.5278698999999989, 0.48801480000000197,
                     0.5120173999999977, 0.5599465000000023, 0.5040277000000017, 0.4399987999999979,
                     0.5439999999999969, 0.5040295000000015, 0.4639535999999964, 0.4080428999999981,
                     0.4639419000000018, 0.48024819999999835, 0.5438237999999984,
                     0.47990809999999584, 0.4640018999999995, 0.49603710000000234,
                     0.4399961000000019, 0.4479609999999994, 0.504025200000001, 0.487997,
                     0.4799939999999978, 0.5039952999999997, 0.45601740000000035,
                     0.46399650000000037, 0.48000480000000323, 0.5359624000000025,
                     0.4721541999999985, 0.43984569999999934, 0.48801180000000244,
                     0.4639930000000021, 0.4000160000000008, 0.30397339999999673,
                     0.2160351999999932, 0.8559343999999953, 0.2000561999999917, 0.2399783000000042,
                     0.34398989999999685, 0.20001769999998942, 0.20001700000000255,
                     0.7759702999999973, 0.20796060000000693, 0.2000293000000113,
                     0.29598729999999307, 0.21599120000000482, 0.19201119999999605]

    second_timings = [3.4419548, 0.3481249999999996, 0.4939838999999999, 0.45600679999999993,
                      0.48002269999999925, 0.48083909999999985, 0.4550483999999999,
                      0.26413690000000045, 0.19993389999999955, 0.24793270000000156,
                      0.2504784999999998, 0.46155979999999985, 0.23428170000000037,
                      0.23769740000000006, 0.23203520000000033, 0.20793389999999867,
                      0.2640222000000012, 0.30410680000000134, 0.42385959999999834,
                      0.45768260000000005, 0.46231000000000044, 0.4560216999999991,
                      0.48800389999999894, 0.4080703999999997, 0.4718973999999996, 0.51999,
                      0.48027830000000016, 0.4419953000000003, 0.4541360000000001,
                      0.4876536999999992, 0.5439122999999988, 0.42411339999999953,
                      0.44941960000000236, 0.24643680000000145, 0.2720983999999973,
                      0.5130297000000006, 0.4230000000000018, 0.4318920999999989,
                      0.5040170999999987, 0.4959789000000008, 0.41601039999999756,
                      0.487969200000002, 0.25046069999999787, 0.2456789999999991,
                      0.4330350000000003, 0.44703429999999855, 0.47251899999999836,
                      0.46330409999999844, 0.5119845000000005, 0.41597770000000267,
                      0.4880075000000019, 0.5360276000000006, 0.4639908999999989,
                      0.4239984999999997, 0.495984, 0.4719933999999988, 0.4560627000000004,
                      0.44796750000000074, 0.4988145000000017, 0.5170916000000005,
                      0.4560358999999998, 0.44805000000000206, 0.5052530999999973,
                      0.4546959000000008, 0.4880262999999978, 0.45613200000000376,
                      0.471847700000005, 0.48798629999999577, 0.4800693000000038,
                      0.49592299999999767, 0.42397350000000245, 0.4321101999999968,
                      0.46398849999999925, 0.5199718000000004, 0.46402530000000297,
                      0.2898928999999981, 0.2238623000000004, 0.4644904000000025,
                      0.44658360000000386, 0.44712599999999725, 0.4560390000000041,
                      0.49703629999999777, 0.4468211000000011, 0.4731742999999966,
                      0.46282779999999946, 0.4800093000000061, 0.48033559999999653,
                      0.45570740000000143, 0.5373908000000043, 0.5039577000000008,
                      0.43866759999999516, 0.4813350000000014, 0.4867448999999979,
                      0.49583630000000056, 0.43212079999999986, 0.27988840000000437,
                      0.2800241999999997]
    second_level = [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1,
                    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
                    1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0]

    third_level = []
    third_timings = []

    all_levels = [first_level[:], second_level[:], third_level[:]]
    all_timings = [first_timings[:], second_timings[:], third_timings[:]]

    for i in range(2):
        pygame.mixer.music.play(0)
        level = all_levels[i][:]
        timings = all_timings[i][:]
        flag = True
        for j in range(20):
            level.pop()
        counter = 0
        pred_end = 0
        counter_max = len(level)

        pygame.time.set_timer(obstacle_event, round(timings[counter] * 1000))

        up = False
        down = False
        odd = True
        color = None
        while flag:
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
                if event.type == obstacle_event:
                    if counter < counter_max - 1:
                        create_note(NOTES[level[counter]])
                        pygame.time.set_timer(obstacle_event, round(timings[counter + 1] * 1000))
                        counter += 1
            if counter == counter_max - 1:
                pred_end += 1
                if pred_end == 100:
                    flag = False
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
    end_window()


def records():
    # вывод таблицы с рекордами
    con = sqlite3.connect('data/records.sqlite')
    cur = con.cursor()
    screen2 = pygame.display.set_mode(size)
    back_ground_sprites_1.draw(screen2)
    screen.blit(screen2, (0, 0))
    result = cur.execute("""SELECT name, kol_vo_score FROM records
            ORDER BY kol_vo_score DESC""").fetchall()

    font = pygame.font.Font(None, 30)
    font_header = pygame.font.Font(None, 40)
    header_player = font_header.render("Игрок", True, pygame.Color('dark blue'))
    screen.blit(header_player, (95, 45))

    header_score = font_header.render("Очки", True, pygame.Color('dark blue'))
    screen.blit(header_score, (95 + header_player.get_width() + 115, 45))
    height0 = 45 + 50
    for i in range(10):
        if i < len(result):
            player = font.render(result[i][0], True, pygame.Color('dark blue'))
            screen.blit(player, (95 + 15, height0))

            score = font.render('{:04}'.format(result[i][1]), True, pygame.Color('dark blue'))
            screen.blit(score, (95 + header_player.get_width() + 115 + 12, height0))

        else:
            player = font.render('NON', True, pygame.Color('dark blue'))
            screen.blit(player, (95 + 15, height0))

            score = font.render('{:04}'.format(0), True, pygame.Color('dark blue'))
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


def end_window():
    global screen, SCORE, VOCABULARY
    screen = pygame.display.set_mode(size)
    row = 0
    screen.fill('black')
    font3 = pygame.font.Font(None, 30)
    font = pygame.font.Font(None, 70)
    text1 = font.render("GAME OVER", True, pygame.Color("white"))
    screen.blit(text1, (80, 23))
    font1 = pygame.font.Font(None, 50)
    text2 = font1.render("YOUR SCORE:", True, pygame.Color("white"))
    screen.blit(text2, (110, 80))
    text3 = font1.render(str(SCORE), True, pygame.Color("white"))
    screen.blit(text3, (210, 135))
    text4 = font1.render("PLEASE,", True, pygame.Color("white"))
    screen.blit(text4, (150, 190))
    text5 = font1.render("WRITE YOUR NICKNAME", True, pygame.Color("white"))
    screen.blit(text5, (14, 230))
    font2 = pygame.font.Font(None, 100)
    text6 = font2.render('_', True, pygame.Color("white"))
    screen.blit(text6, (140, 300))
    screen.blit(text6, (200, 300))
    screen.blit(text6, (260, 300))
    text10 = font3.render('UNFAMILIAR SYMBOL', True, pygame.Color("white"))
    name = ''
    the_end = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if row == 0:
                    try:
                        text7 = font2.render(VOCABULARY[event.key - 97], True,
                                             pygame.Color("white"))
                        screen.blit(text7, (137, 297))
                        row += 1
                        pygame.draw.rect(screen, pygame.Color("black"), (127, 500, 215, 530))
                        name += VOCABULARY[event.key - 97]
                    except Exception:
                        screen.blit(text10, (127, 500))
                elif row == 1:
                    try:
                        text8 = font2.render(VOCABULARY[event.key - 97], True,
                                             pygame.Color("white"))
                        screen.blit(text8, (197, 297))
                        row += 1
                        pygame.draw.rect(screen, pygame.Color("black"), (127, 500, 215, 530))
                        name += VOCABULARY[event.key - 97]
                    except Exception:
                        screen.blit(text10, (127, 500))
                elif row == 2:
                    try:
                        text9 = font2.render(VOCABULARY[event.key - 97], True,
                                             pygame.Color("white"))
                        screen.blit(text9, (257, 297))
                        row += 1
                        pygame.draw.rect(screen, pygame.Color("black"), (127, 500, 215, 530))
                        name += VOCABULARY[event.key - 97]
                        con = sqlite3.connect('data/records.sqlite')
                        cur = con.cursor()
                        cur.execute(
                            f"""INSERT INTO records(name,kol_vo_score) VALUES('{name}',{SCORE})""")
                        con.commit()
                        con.close()
                        the_end = True
                    except Exception:
                        screen.blit(text10, (127, 500))
        if the_end:
            pygame.mixer.music.load("data/main_menu_theme.mp3")
            pygame.mixer.music.set_volume(VOLUME)
            pygame.mixer.music.play(-1)
            break
        pygame.display.flip()
        timer.tick(FPS)


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
        if (pygame.sprite.spritecollideany(self, taiko_hit_box_spr) and (
                (self.note == 'kacu' and taiko.stance == 'blue')
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
