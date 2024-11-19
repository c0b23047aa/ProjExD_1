import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景Surfaceを生成する
    bg2_img = pg.transform.flip(bg_img, True, False) #反転背景Surfaceを生成する
    koukaton_img = pg.image.load("fig/3.png")#こうかとんSurfaceを生成する
    koukaton_img = pg.transform.flip(koukaton_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%4800
        screen.blit(bg_img, [-x, 0]) #ScreenSurfaceに背景Surfaceを貼り付ける
        screen.blit(bg2_img, [-x+1600, 0]) #ScreenSurfaceに反転背景Surfaceを貼り付ける
        screen.blit(bg_img, [-x+3200, 0]) 
        screen.blit(bg2_img, [-x+4800, 0])
        screen.blit(koukaton_img, [300, 200]) #ScreenSurfaceにこうかとんSurfaceを貼り付ける
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()