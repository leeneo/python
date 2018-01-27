import pygame   #pip install pygame
from pygame.locals import *
import time

bulletSBox=[]

#app main entrence
def main():
    #创建游戏窗口
    screen=pygame.display.set_mode((480,852),0,32)

    #接收背景图片，飞机图片
    background=pygame.image.load("./feiji/background.png")
    plane=pygame.image.load("./feiji/hero1.png")

    #设置飞机位置
    x=480/2-100/2
    y=600

    #设置飞机移速
    speed=10


    while True:
        
        #粘贴图片到游戏窗口
        screen.blit(background,(0,0))

        #事件监测
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()

        #监听键盘事件
        key_pressed=pygame.key.get_pressed()
        if key_pressed[K-w] or key_pressed[K_UP]:
            print("UP")
            y-=speed
        if key_pressed[K-s] or key_pressed[K_DOWN]:
            print("DOWN")
            y+=speed
        if key_pressed[K-a] or key_pressed[K_LEFT]:
            print("LEFT")
            x-=speed
        if key_pressed[K-d] or key_pressed[K_RIGHT]:
            print("RIGHT")
            x+=speed
        if key_pressed[K-SPACE]:
            print("FIRE")
            bullet=pygame.image.load("./feiji/bullet.png")

            #定义子弹
            my_bullet={
                "子弹":bullet,
                "x":x-40,
                "y":y
            }
            bulletsBox.append(my_bullet)
        for i in bulletsBox:
            screen.blit(i["子弹"],(i["x"],i["y"]))
            i["y"]-=25

    screen.blit(plane,(x,y))

    #更新数据
    pygame.display.update()

    #减少cpu占用
    time.sleep(0.01)

main()