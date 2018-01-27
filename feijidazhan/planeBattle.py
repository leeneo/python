import pygame   #pip install pygame
from pygame.locals import *

#1. 初始化 pygame
pygame.init()

#2. 设置游戏界面大小、背景图片及标题
# 游戏界面像素大小
screen = pygame.display.set_mode((480, 800))

# 游戏界面标题
pygame.display.set_caption('飞机大战')

# 背景图
background = pygame.image.load('feiji/background.png').convert()

# Game Over 的背景图
game_over = pygame.image.load('feiji/gameover.png')

# 飞机图片
plane_img = pygame.image.load('feiji/hero1.png')

# 截取玩家飞机图片
player = plane_img.subsurface(pygame.Rect(0, 9, 10, 12))

#3. 游戏主循环内需要处理游戏界面的初始化、更新及退出
while True:
    # 初始化游戏屏幕
    screen.fill(0)
    screen.blit(background, (0, 0))

    # 显示玩家飞机在位置[200,600]
    screen.blit(player, [200, 600])

    # 更新游戏屏幕
    pygame.display.update()

    # 游戏退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            #1. 获取键盘事件（上下左右按键）
key_pressed = pygame.key.get_pressed()

#2. 处理键盘事件（移动飞机的位置）
if key_pressed[K_w] or key_pressed[K_UP]:
    player.moveUp()
if key_pressed[K_s] or key_pressed[K_DOWN]:
    player.moveDown()
if key_pressed[K_a] or key_pressed[K_LEFT]:
    player.moveLeft()
if key_pressed[K_d] or key_pressed[K_RIGHT]:
    player.moveRight()

    #1. 生成子弹，需要控制发射频率
# 首先判断玩家飞机没有被击中
if not player.is_hit:
    if shoot_frequency % 15 == 0:
        player.shoot(bullet_img)
    shoot_frequency += 1
    if shoot_frequency >= 15:
        shoot_frequency = 0

for bullet in player.bullets:
    #2. 以固定速度移动子弹
    bullet.move()
    #3. 移动出屏幕后删除子弹
    if bullet.rect.bottom < 0:
        player.bullets.remove(bullet)            

# 显示子弹
player.bullets.draw(screen)

#1. 生成敌机，需要控制生成频率
if enemy_frequency % 50 == 0:
    enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
    enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
    enemies1.add(enemy1)
enemy_frequency += 1
if enemy_frequency >= 100:
    enemy_frequency = 0


for enemy in enemies1:
    #2. 移动敌机
    enemy.move()
    #3. 敌机与玩家飞机碰撞效果处理
    if pygame.sprite.collide_circle(enemy, player):
        enemies_down.add(enemy)
        enemies1.remove(enemy)
        player.is_hit = True
        break
    #4. 移动出屏幕后删除飞机    
    if enemy.rect.top < 0:
        enemies1.remove(enemy)

#5. 敌机被子弹击中效果处理

# 将被击中的敌机对象添加到击毁敌机 Group 中，用来渲染击毁动画
enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
for enemy_down in enemies1_down:
    enemies_down.add(enemy_down)

# 敌机被子弹击中效果显示
for enemy_down in enemies_down:
    if enemy_down.down_index == 0:
        pass
    if enemy_down.down_index > 7:
        enemies_down.remove(enemy_down)
        score += 1000
        continue
    screen.blit(enemy_down.down_imgs[enemy_down.down_index / 2], enemy_down.rect)
    enemy_down.down_index += 1

# 显示敌机
enemies1.draw(screen)

# 绘制得分
score_font = pygame.font.Font(None, 36)
score_text = score_font.render(str(score), True, (128, 128, 128))
text_rect = score_text.get_rect()
text_rect.topleft = [10, 10]
screen.blit(score_text, text_rect)