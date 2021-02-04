import colorama
import time

from colorama import Fore, init

colorama.init()
rr = Fore.RED
rg = Fore.GREEN
rc = Fore.CYAN
ry = Fore.YELLOW
x = 0
y = 0
bs = 25
run = True
color0 = [255, 255, 255]
color1 = [0, 0, 0]
color2 = [255, 0, 0]
color3 = [0, 255, 0]
color4 = [0, 0, 255]
color5 = [255, 255, 0]
color6 = [0, 255, 255]
color7 = [255, 0, 255]

inx = 0
iny = 0


def menud(pa1, pa2):
    print(ry + "[" + rc + str(pa1) + ry + "] " + pa2)

def mapcreate(map):
    window.fill(color0)
    inx = 0
    iny = 0
    sizey = bs * iny
    sizex = bs * inx
    for list in map:
        for box in list:
            if box == 0:
                inx += 1
            elif box == 1:
                pygame.draw.rect(window, color1, (sizex, sizey, bs, bs))
                inx += 1
            elif box == 2:
                pygame.draw.rect(window, color2, (sizex, sizey, bs, bs))
                inx += 1
            elif box == 3:
                pygame.draw.rect(window, color3, (sizex, sizey, bs, bs))
                inx += 1
            elif box == 4:
                pygame.draw.rect(window, color4, (sizex, sizey, bs, bs))
                inx += 1
            elif box == 5:
                pygame.draw.rect(window, color5, (sizex, sizey, bs, bs))
                inx += 1
            elif box == 6:
                pygame.draw.rect(window, color6, (sizex, sizey, bs, bs))
                inx += 1
            elif box == 7:
                pygame.draw.rect(window, color7, (sizex, sizey, bs, bs))
                inx += 1

            sizex = bs * inx
        iny += 1
        sizey = bs * iny
        inx = 0
        sizex = bs * inx


menud(1, "draw")
menud(2, "import")
try:
    mode = int(input('num: '))
except:
    print("NumError")
if mode == 1:
    msize = input("num of cells(heigth width): ")
    msize = msize.split()
    mw = int(msize[1])
    mh = int(msize[0])
    mwl = []
    mhl = []
    for i in range(mh):
        for d in range(mw):
            mwl.append(0)
        mhl.append(mwl)
        mwl = []
    map = mhl

    import pygame

    pygame.init()
    window = pygame.display.set_mode([mw * bs + 1, mh * bs + 1])
    pygame.display.set_caption('game')

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if x != 0:
                        x = x - bs
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if x != (mw - 1) * 25:
                        x = x + bs
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if y != (mh - 1) * 25:
                        y = y + bs
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if y != 0:
                        y = y - bs
                elif event.key == pygame.K_q:
                    ms = ''
                    for e in map:
                        for i in e:
                            ms = ms + str(i) + ' '
                        print(ms)
                        ms = ''
                elif event.key == pygame.K_BACKSPACE:
                    run = False
                elif event.key == pygame.K_e:
                    if map[round(y / bs)][round(x / bs)] == 0:
                        map[round(y / bs)][round(x / bs)] = 1
                    elif map[round(y / bs)][round(x / bs)] == 1:
                        map[round(y / bs)][round(x / bs)] = 2
                    elif map[round(y / bs)][round(x / bs)] == 2:
                        map[round(y / bs)][round(x / bs)] = 3
                    elif map[round(y / bs)][round(x / bs)] == 3:
                        map[round(y / bs)][round(x / bs)] = 4
                    elif map[round(y / bs)][round(x / bs)] == 4:
                        map[round(y / bs)][round(x / bs)] = 5
                    elif map[round(y / bs)][round(x / bs)] == 5:
                        map[round(y / bs)][round(x / bs)] = 6
                    elif map[round(y / bs)][round(x / bs)] == 6:
                        map[round(y / bs)][round(x / bs)] = 7
                    elif map[round(y / bs)][round(x / bs)] == 7:
                        map[round(y / bs)][round(x / bs)] = 0

                elif event.key == pygame.K_0:
                    map[round(y / bs)][round(x / bs)] = 0
                elif event.key == pygame.K_1:
                    map[round(y / bs)][round(x / bs)] = 1
                elif event.key == pygame.K_2:
                    map[round(y / bs)][round(x / bs)] = 2
                elif event.key == pygame.K_3:
                    map[round(y / bs)][round(x / bs)] = 3
                elif event.key == pygame.K_4:
                    map[round(y / bs)][round(x / bs)] = 4
                elif event.key == pygame.K_5:
                    map[round(y / bs)][round(x / bs)] = 5
                elif event.key == pygame.K_6:
                    map[round(y / bs)][round(x / bs)] = 6
                elif event.key == pygame.K_7:
                    map[round(y / bs)][round(x / bs)] = 7
        mapcreate(map)
        pygame.draw.rect(window, [255, 0, 0], (x, y, bs, bs), 5)

        pygame.display.flip()
        pygame.display.update()
    pygame.quit()
elif mode == 2:
    msize = input("num of cells(heigth width): ")
    msize = msize.split()
    mw = int(msize[1])
    mh = int(msize[0])
    mhl = []
    mwl = []
    for i in range(mh):
        for t in input().split():
            mwl.append(int(t))
        mhl.append(mwl)
        mwl = []
    map = mhl
    import pygame

    print(map)
    pygame.init()
    window = pygame.display.set_mode([mw * bs + 1, mh * bs + 1])
    pygame.display.set_caption('game')
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if x != 0:
                        x = x - bs
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if x != (mw - 1) * 25:
                        x = x + bs
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if y != (mh - 1) * 25:
                        y = y + bs
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if y != 0:
                        y = y - bs
                elif event.key == pygame.K_q:
                    ms = ''
                    for e in map:
                        for i in e:
                            ms = ms + str(i) + ' '
                        print(ms)
                        ms = ''
                elif event.key == pygame.K_BACKSPACE:
                    run = False
                elif event.key == pygame.K_e:
                    if map[round(y / bs)][round(x / bs)] == 0:
                        map[round(y / bs)][round(x / bs)] = 1
                    elif map[round(y / bs)][round(x / bs)] == 1:
                        map[round(y / bs)][round(x / bs)] = 2
                    elif map[round(y / bs)][round(x / bs)] == 2:
                        map[round(y / bs)][round(x / bs)] = 3
                    elif map[round(y / bs)][round(x / bs)] == 3:
                        map[round(y / bs)][round(x / bs)] = 4
                    elif map[round(y / bs)][round(x / bs)] == 4:
                        map[round(y / bs)][round(x / bs)] = 5
                    elif map[round(y / bs)][round(x / bs)] == 5:
                        map[round(y / bs)][round(x / bs)] = 6
                    elif map[round(y / bs)][round(x / bs)] == 6:
                        map[round(y / bs)][round(x / bs)] = 7
                    elif map[round(y / bs)][round(x / bs)] == 7:
                        map[round(y / bs)][round(x / bs)] = 0
                elif event.key == pygame.K_0:
                    map[round(y / bs)][round(x / bs)] = 0
                elif event.key == pygame.K_1:
                    map[round(y / bs)][round(x / bs)] = 1
                elif event.key == pygame.K_2:
                    map[round(y / bs)][round(x / bs)] = 2
                elif event.key == pygame.K_3:
                    map[round(y / bs)][round(x / bs)] = 3
                elif event.key == pygame.K_4:
                    map[round(y / bs)][round(x / bs)] = 4
                elif event.key == pygame.K_5:
                    map[round(y / bs)][round(x / bs)] = 5
                elif event.key == pygame.K_6:
                    map[round(y / bs)][round(x / bs)] = 6
                elif event.key == pygame.K_7:
                    map[round(y / bs)][round(x / bs)] = 7
        mapcreate(map)
        pygame.draw.rect(window, [255, 0, 0], (x, y, bs, bs), 5)

        pygame.display.flip()
        pygame.display.update()
    pygame.quit()
else:
    pass
