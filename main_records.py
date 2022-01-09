import sys
import sqlite3
import pygame


def terminate():
    pygame.quit()
    sys.exit()


def rec():
    # вывод таблицы с рекордами
    con = sqlite3.connect('data/records.sqlite')
    cur = con.cursor()
    result = list(sorted(cur.execute("""SELECT name, kol_vo_score FROM records
            ORDER BY kol_vo_score DESC""").fetchall(), key=lambda elem: elem[1]))

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


if __name__ == '__main__':
    pygame.init()
    size = width, height = 450, 550
    screen = pygame.display.set_mode(size)
    button_sprites = pygame.sprite.Group()
    rec()
    pygame.quit()
