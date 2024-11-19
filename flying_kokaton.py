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
    kk_rct = koukaton_img.get_rect() #こうかとんSurfaceに対応するこうかとんRectを取得する
    kk_rct.center = 300, 200 
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        dx = 0
        dy = 0
        if key_lst[pg.K_UP]: #全キーの押下状態（True or False）を取得する
            dy-=1 #全キーの押下状態（True or False）を取得する
        if key_lst[pg.K_DOWN]: 
            dy+=1
        if key_lst[pg.K_LEFT]: 
            dx-=1
        if key_lst[pg.K_RIGHT]: 
            dx+=1
        else:
            dx-=1
        kk_rct.move_ip((dx, dy))
        

        x = tmr%3200
        screen.blit(bg_img, [-x, 0]) #ScreenSurfaceに背景Surfaceを貼り付ける
        screen.blit(bg2_img, [-x+1600, 0]) #ScreenSurfaceに反転背景Surfaceを貼り付ける
        screen.blit(bg_img, [-x+3200, 0]) 
        screen.blit(bg2_img, [-x+4800, 0])
        screen.blit(koukaton_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()