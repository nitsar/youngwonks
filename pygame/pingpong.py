import pygame
from pygame import *
import pygame.time
import random
import time

class helper():
    def __init__(self):
        #Width and Height of pygame window 
        self.screenwidth = 640
        self.screenlength = 640
        #Width and Heigth of paddle
        self.paddlewidth = 10
        self.paddleheight = 100
        #Left paddle initial position co-ordinates
        self.startpaddleleftx= 0
        self.startpaddlelefty= 400
        #Right paddle initial position co-ordinates
        self.startpaddlerightx= 640 - self.paddlewidth
        self.startpaddlerighty= 400
        #Ball initial co-ordinates
        self.ballx = 320
        self.bally = 320
        self.radius = 20
        self.thickness = 0
        #Colors
        self.red = (255,0,0)
        self.blue = (0,0,255)
        self.green = (0,255,0)
        self.clock = pygame.time.Clock()
        self.left_player_score_coord = (0,0)
        self.right_player_score_coord = (480,0)
        self.start_time = time.time()
        self.time_coord = (320,0)
        self.game_over_coord = (320,240)
        self.game_over_time = 60
        
    def show_text(self,screen,x,y,color,text):
        fontobj = pygame.font.SysFont("freesans",16)
        msgobj = fontobj.render(str(text),False,color)
        screen.blit(msgobj,(x,y))
        
objhelper = helper()

class paddle:
    def __init__(self, screen, paddlex, paddley, paddlewidth, paddleheight, color):
        self.paddlex = paddlex
        self.paddley = paddley
        self.paddlewidth = paddlewidth
        self.paddleheight = paddleheight
        self.color = color
        self.paddle_up = 0
        self.paddle_down = 0
        self.score = 0
        pygame.draw.rect(screen,color,(self.paddlex,self.paddley,self.paddlewidth,self.paddleheight))

    def move(self, screen):
        #self.paddlex = dest_x
        #self.paddley = dest_y
        if paddleleft.paddle_up == 1 and paddleleft.paddley >= 0:
            paddleleft.paddley = paddleleft.paddley - 1
        if paddleleft.paddle_down == 1 and paddleleft.paddley + paddleleft.paddleheight <= objhelper.screenwidth:
            paddleleft.paddley = paddleleft.paddley + 1
        if paddleright.paddle_up == 1 and paddleright.paddley >= 0:
            paddleright.paddley = paddleright.paddley - 1
        if paddleright.paddle_down == 1 and paddleright.paddley + paddleleft.paddleheight <= objhelper.screenwidth:
            paddleright.paddley = paddleright.paddley + 1

        pygame.draw.rect(screen,self.color,(self.paddlex,self.paddley,self.paddlewidth,self.paddleheight))

    def detectpaddlecollision(self,screen, ballobj, paddle):
        #print(ballobj.ballx + ballobj.radius,self.paddlex, self.paddley, ballobj.bally, self.paddleheight)
        if ballobj.ballx + ballobj.radius == self.paddlex and self.paddley <= ballobj.bally <= self.paddley + self.paddleheight \
        and paddle == "right":
            print("right collision")
            ballobj.ballxmovement = -1
            self.score += 1
        if ballobj.ballx - ballobj.radius == self.paddlex + self.paddlewidth and self.paddley <= ballobj.bally <= self.paddley + self.paddleheight \
        and paddle == "left":
            print("left collision")
            ballobj.ballxmovement = 1
            self.score += 1
        
class ball:
    def __init__(self, screen, ballx, bally, radius, thickness, color):
        self.ballx = ballx
        self.bally = bally
        self.radius = radius
        self.thickness = thickness
        self.color = color
        self.movement = 1
        self.ballxmovement  = random.randint(-1,1)
        self.ballymovement = random.randint(-1,1)
        while self.ballymovement == 0:
            self.ballymovement = random.randint(-1,1)
        while self.ballxmovement == 0:
            self.ballxmovement = random.randint(-1,1)
        pygame.draw.circle(screen,self.color,(self.ballx,self.bally),self.radius, self.thickness)

    def move(self, screen):
        #self.ballx = ballx
        #self.bally = bally
        pygame.draw.circle(screen,self.color,(self.ballx,self.bally),self.radius, self.thickness)

    def checkboundaries(self,screen):
        if self.bally + self.radius == objhelper.screenlength and self.movement == 1:
            self.movement = -1 
        if self.bally - self.radius == 0 and self.movement == -1:
            self.movement = 1
        if self.movement == 1:
            self.bally = self.bally + self.movement
        else:
            self.bally = self.bally + self.movement
        self.ballx += self.ballxmovement
        # Make the ball go to the center after its out of the screen
        if self.ballx < 0 or self.ballx > objhelper.screenwidth:
            self.ballx = objhelper.ballx
            self.bally = objhelper.bally

pygame.init()
screen = pygame.display.set_mode((objhelper.screenwidth,objhelper.screenlength))

#Creating left paddle object    
paddleleft = paddle(screen, objhelper.startpaddleleftx, objhelper.startpaddlelefty, objhelper.paddlewidth,
                    objhelper.paddleheight,objhelper.red)

#Creating right paddle object
paddleright = paddle(screen, objhelper.startpaddlerightx, objhelper.startpaddlerighty, objhelper.paddlewidth,
                     objhelper.paddleheight,objhelper.blue)

#Creating a ball
ball_1 = ball(screen,objhelper.ballx, objhelper.bally,objhelper.radius, objhelper.thickness, objhelper.green)

while True:
    #Tell how many frames per second
    objhelper.clock.tick(200)
    time_end = time.time()
    #Refreshes the screen
    pygame.display.update()
    #Fills screen with black each time in while True
    screen.fill((0,0,0))
    #Movement of left paddle
    paddleleft.move(screen)
    #Movement of right paddle
    paddleright.move(screen)
    #Movement of ball
    ball_1.move(screen)
    #Check boundary
    ball_1.checkboundaries(screen)
    #Check right paddle collision 
    paddleright.detectpaddlecollision(screen,ball_1,"right")
    #Check left paddle collision 
    paddleleft.detectpaddlecollision(screen,ball_1,"left")
    objhelper.show_text(screen, objhelper.left_player_score_coord[0], objhelper.left_player_score_coord[1], objhelper.blue, "Left Player Score:" + str(paddleleft.score))
    objhelper.show_text(screen, objhelper.right_player_score_coord[0], objhelper.right_player_score_coord[1], objhelper.red, "Right Player Score:" + str(paddleright.score))
    time_elapsed = int(time_end - objhelper.start_time)
    objhelper.show_text(screen, objhelper.time_coord[0], objhelper.time_coord[1], objhelper.red, "Time:" + str(time_elapsed))

    if time_elapsed > objhelper.game_over_time:
        objhelper.show_text(screen, objhelper.game_over_coord[0], objhelper.game_over_coord[1], objhelper.red, "GAME OVER!!!")
        
        if paddleleft.score > paddleright.score:
            objhelper.show_text(screen, objhelper.game_over_coord[0], objhelper.game_over_coord[1]+50, objhelper.red, "Player 1 won")
        if paddleleft.score < paddleright.score:
            objhelper.show_text(screen, objhelper.game_over_coord[0], objhelper.game_over_coord[1]+50, objhelper.red, "Player 2 won")
        if paddleleft.score == paddleright.score:
            objhelper.show_text(screen, objhelper.game_over_coord[0], objhelper.game_over_coord[1]+50, objhelper.red, "DRAW!!")
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        exit()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_w:
                paddleleft.paddle_up = 1
            elif event.key == K_s:
                paddleleft.paddle_down = 1
            if event.key == K_UP:
                paddleright.paddle_up = 1
            elif event.key == K_DOWN:
                paddleright.paddle_down = 1
        elif event.type == KEYUP:
            if event.key == K_w:
                paddleleft.paddle_up = 0
            elif event.key == K_s:
                paddleleft.paddle_down = 0
            if event.key == K_UP:
                paddleright.paddle_up = 0
            elif event.key == K_DOWN:
                paddleright.paddle_down = 0
            
    
