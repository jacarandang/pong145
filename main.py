import os, sys, time

import pygame
from pygame.locals import *

from classes.board import boardSprite
from classes.pong import pongSprite
from classes.ball import ballSprite
from classes.stuff import splitterSprite
from classes.stuff import boosterSprite
from classes.connections import Client
from classes.utilities import loadImage
from classes.utilities import Button

pygame.font.init()

class Main:

    def __init__(self, screen, client, player):
        self.screen = screen
        self.bg = pygame.Surface(screen.get_size()).convert()
        self.bg.fill((0, 0, 0))

        self.clock = pygame.time.Clock();
        self.running = False

        self.board = boardSprite.boardSprite()

        self.player1 = pongSprite.pongSprite((10, 300))
        self.player2 = pongSprite.pongSprite((790, 300))

        self.ball = ballSprite.ballSprite(400, 300)
        self.ball.setLeftPong(self.player1)
        self.ball.setRightPong(self.player2)

        self.balls = [self.ball]

        self.splitter = splitterSprite.splitterSprite(400, 300, self)
        self.splitter.addBall(self.ball)

        self.spriteGroup = pygame.sprite.Group()
        self.spriteGroup.add(self.player1)
        self.spriteGroup.add(self.player2)
        self.spriteGroup.add(self.ball)

        self.stageGroup = pygame.sprite.Group()
        self.stageGroup.add(self.board)

        self.stuffGroup = pygame.sprite.Group()

        self.font = pygame.font.Font("resource/font.ttf", 350)
        self.font2 = pygame.font.Font("resource/font.ttf", 32)

        self.client = client
        self.player = player

        self.selected = None

    def add_ball(self, x, y, dx, dy):
        ball = ballSprite.ballSprite(x, y, dx, dy)
        ball.setLeftPong(self.player1)
        ball.setRightPong(self.player2)
        for stuff in self.stuffGroup:
            stuff.addBall(ball)
        self.spriteGroup.add(ball)
        self.balls.append(ball)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    if self.player == 1:
                        self.player1.startMovingUp()
                    else:
                        self.player2.startMovingUp()
                    self.client.send("up")
                elif event.key == K_DOWN:
                    if self.player == 1:
                        self.player1.startMovingDown()
                    else:
                        self.player2.startMovingDown()
                    self.client.send("down")
            elif event.type == KEYUP:
                if event.key in [K_UP, K_DOWN]:
                    if self.player == 1:
                        self.player1.stopMoving()
                    else:
                        self.player2.stopMoving()
                    self.client.send("stop")

    def process_message(self):
        for msg in self.client.get_all():
            print msg
            msgs = msg.split()
            if msgs[0] == "player":
                if msgs[1] == "1":
                    if msgs[2] == "up":
                        self.player1.startMovingUp()
                    elif msgs[2] == "down":
                        self.player1.startMovingDown()
                    elif msgs[2] == "stop":
                        self.player1.stopMoving()
                    elif msgs[2] == "pos":
                        x = float(msgs[3])
                        y = float(msgs[4])
                        self.player1.x = x
                        self.player1.y = y
                if msgs[1] == "2":
                    if msgs[2] == "up":
                        self.player2.startMovingUp()
                    elif msgs[2] == "down":
                        self.player2.startMovingDown()
                    elif msgs[2] == "stop":
                        self.player2.stopMoving()
                    elif msgs[2] == "pos":
                        x = float(msgs[3])
                        y = float(msgs[4])
                        self.player2.x = x
                        self.player2.y = y

            if msgs[0] == "ball":
                bx = float(msgs[1])
                by = float(msgs[2])
                bdx = float(msgs[3])
                bdy = float(msgs[4])
                self.ball.x = bx
                self.ball.y = by
                self.ball.dx = bdx
                self.ball.dy = bdy

    #SETTER OF SELECTED
    def set_boosterr(self):
        self.selected = boosterSprite.boosterSprite(3, 0, 0, 0, loadImage("boosterr.png", None), True)
    def set_boosterl(self):
        self.selected = boosterSprite.boosterSprite(-3, 0, 0, 0, loadImage("boosterl.png", None), True)
    def set_boosteru(self):
        self.selected = boosterSprite.boosterSprite(0, -3, 0, 0, loadImage("boosteru.png", None), True)
    def set_boosterd(self):
        self.selected = boosterSprite.boosterSprite(0, 3, 0, 0, loadImage("boosterd.png", None), True)
    def set_splitter(self):
        self.selected = splitterSprite.splitterSprite(0, 0, self, loadImage("splitter.png", None), True)

    def placement(self):

        self.running = True
        def ready():
            self.running = False

        base_time = time.time()

        panel_img = pygame.Surface((150, 600)).convert()
        panel_img.fill((200, 200, 200))
        panel_rect = panel_img.get_rect()
        panel_rect.center = 400, 300

        valid_area = overlay = None
        if self.player == 1:
            valid_area = pygame.Rect(0, 0, 325, 600)
            overlay = pygame.Rect(475, 0, 325, 600)
        else:
            valid_area = pygame.Rect(475, 0, 325, 600)
            overlay = pygame.Rect(0, 0, 325, 600)

        overlay_img = pygame.Surface((325, 600)).convert()
        overlay_img.fill((0, 0, 0))
        overlay_img.set_alpha(200)

        buttongroup = pygame.sprite.Group()

        bboosterr = Button(loadImage("boosterr.png", None), (400, 50), self.set_boosterr)
        buttongroup.add(bboosterr)

        bboosterl = Button(loadImage("boosterl.png", None), (400, 125), self.set_boosterl)
        buttongroup.add(bboosterl)

        bboosteru = Button(loadImage("boosteru.png", None), (400, 225), self.set_boosteru)
        buttongroup.add(bboosteru)

        bboosterd = Button(loadImage("boosterd.png", None), (400, 350), self.set_boosterd)
        buttongroup.add(bboosterd)

        bsplitter = Button(loadImage("splitter.png"), (400, 450), self.set_splitter)
        buttongroup.add(bsplitter)

        bready = Button(self.font2.render("READY", True, (0, 0, 0), None), (400, 550), ready)
        buttongroup.add(bready)

        buttonlist = [bboosterr, bboosterl, bboosteru, bboosterd, bsplitter, bready]

        while(self.running):
            self.clock.tick(60)

            self.screen.blit(self.bg, (0, 0))

            self.stageGroup.update()
            self.stuffGroup.update()
            self.spriteGroup.update()
            buttongroup.update()

            self.stageGroup.draw(self.screen)
            self.stuffGroup.draw(self.screen)
            self.spriteGroup.draw(self.screen)

            self.screen.blit(panel_img, panel_rect)
            buttongroup.draw(self.screen)
            self.screen.blit(overlay_img, overlay)

            if self.selected:
                self.selected.update()
                self.screen.blit(self.selected.image, self.selected.rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    self.quit = True
                elif event.type == MOUSEBUTTONDOWN:
                    if not self.selected:
                        for b in buttonlist:
                            b.click()
                    elif self.selected:
                        (self.selected.x, self.selected.y) = pygame.mouse.get_pos()
                        self.selected.onMouse = False
                        self.stuffGroup.add(self.selected)
                        self.selected.addBall(self.ball)
                        self.selected = None

    def count_down(self):
        rem = 3

        base_time = time.time()
        time_image = self.font.render(str(rem), True, (255, 255, 255), (0, 0, 0))
        time_rect = time_image.get_rect()
        time_rect.center = 400, 300

        self.running = True
        self.quit = False

        overlay = pygame.Surface((800, 600)).convert()
        overlay.fill((0, 0, 0))
        overlay.set_alpha(200)

        while(self.running):
            nrem = int(4 - (time.time() - base_time))
            if(nrem < rem):
                rem = nrem
                time_image = self.font.render(str(rem), True, (255, 255, 255), (0, 0, 0))
                time_rect = time_image.get_rect()
                time_rect.center = 400, 300

            self.clock.tick(60)

            self.screen.blit(self.bg, (0, 0))

            self.stageGroup.update()
            self.stuffGroup.update()
            self.spriteGroup.update()

            self.stageGroup.draw(self.screen)
            self.stuffGroup.draw(self.screen)
            self.spriteGroup.draw(self.screen)

            self.screen.blit(overlay, (0, 0))
            self.screen.blit(time_image, time_rect)

            pygame.display.flip()
            if(time.time() - base_time >= 3):
                break

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    self.quit = True

        if self.quit:
            return

        self.client.send("READY")
        self.start()

    def start(self):
        self.running = True
        init = self.client.wait_message().split()
        self.ball.initiate(int(init[0]), int(init[1]))

        booster = boosterSprite.boosterSprite(3, 0, 400, 300, loadImage("boosterr.png", None), False)
        booster.addBall(self.ball)
        splitter = splitterSprite.splitterSprite(400, 400, self, loadImage("splitter.png", None), False)
        splitter.addBall(self.ball)
        self.stuffGroup.add(booster, splitter)

        while(self.running):
            self.check_events()
            self.process_message()
            self.clock.tick(60) #resource intensive but fixes bugged pong and slider

            self.screen.blit(self.bg, (0, 0))

            self.stageGroup.update()
            self.stuffGroup.update()
            self.spriteGroup.update()

            self.stageGroup.draw(self.screen)
            self.stuffGroup.draw(self.screen)
            self.spriteGroup.draw(self.screen)
            pygame.display.flip()

            if self.ball.outOfBounds():
                msg = self.client.wait_message()
                if msg == "GAMEOVER":
                    break

        if self.ball.out: self.gameover()

    def gameover(self):
        pygame.display.flip()
        go_image = loadImage("gameover.jpg", None)
        go_rect = go_image.get_rect()
        go_rect.center = 400, 300
        self.screen.blit(go_image, go_rect)
        pygame.display.flip()
        t = time.time()
        while time.time() - t < 1:
            continue


if __name__ == '__main__':

    print "Enter address"
    add = raw_input()
    print "Enter port"
    port = raw_input()

    pygame.init()
    pygame.display.set_caption("Pong")
    # pygame.key.set_repeat(1, 10)
    screen = pygame.display.set_mode((800, 600))

    client = Client.Client(add, port)
    client.begin_listening()

    pl = int(client.wait_message())
    game = Main(screen, client, pl)
    game.placement()
    msg = client.wait_message()
    if msg == "COUNTDOWN":
        game.count_down()
    print "End Game"
    pygame.quit()
