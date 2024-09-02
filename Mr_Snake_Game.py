"""
Main file the game runs off of
By Ibrahim Sydock
"""

import sys, random, pygame, time, math

#initialize
pygame.init()

#screen width and height in pixels
WIN_X = 800
WIN_Y = 600

GAME_NAME = 'Mr.Snake\'s Insatiable Appetite'
fps = 30

font = pygame.font.SysFont('subscribe',40)

MAX_FRUIT = 10

#Colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)

GREEN = (0,255,0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PINK = (235, 28, 228)
ORANGE = (255, 128, 0)
VIOLET = (128, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

RAINBOW = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, VIOLET]

#game window initialize
WIN = pygame.display.set_mode((WIN_X,WIN_Y))

#Game caption
pygame.display.set_caption(GAME_NAME)

UNIQUE_FRUIT_TYPES = 6

class Fruit():
    def __init__(self, pos, fType):
        self.pos = pos
        self.fType = fType
        self.color = VIOLET
        self.rainIterator = 0.0
        
        if self.fType == 1:
            self.color = BLUE
        if self.fType == 2:
            self.color = CYAN
        if self.fType == 3:
            self.color = ORANGE
        if self.fType == 4:
            self.color = PINK
        if self.fType == 5:
            self.color = RED
        if self.fType == 6:
            self.color = "cycle"
      
    def getType(self):
        return self.fType
      
    #Collision
    def collid(self, snake_pos):
        if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(self.pos[0],self.pos[1],10,10)):
            return True
        return False
    
    #Drawing
    def draw(self):
        # Rainbow cycle
        if self.color == "cycle":
            
            pygame.draw.rect(WIN , RAINBOW[math.floor(self.rainIterator)], (self.pos[0],self.pos[1],10,10))
            
            self.rainIterator += 0.26
            if math.floor(self.rainIterator) >= len(RAINBOW):
                self.rainIterator = 0
                
        else:
            pygame.draw.rect(WIN ,self.color,(self.pos[0],self.pos[1],10,10))

#MENU
def main_menu():
    #Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Click to game
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        
        WIN.fill((0,0,0)) #BG
        main_menu_message = font.render('Press anywhere to start the game' , True , WHITE)
        font_pos = main_menu_message.get_rect(center=(WIN_X//2, WIN_Y//2))
        WIN.blit(main_menu_message , font_pos)
        pygame.display.update()
        
#GAME OVER
def game_over(score):
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        WIN.fill((0,0,0)) #BG
        
        #showing 'You lost' in red color
        game_over_message = font.render('You Lost' , True , RED)
        #showing 'You score was SCORE'
        game_over_score = font.render(f'Your Score was {score}' , True , WHITE)

        font_pos_message = game_over_message.get_rect(center=(WIN_X//2, WIN_Y//2))
        font_pos_score = game_over_score.get_rect(center=(WIN_X//2, WIN_Y//2+40))
        WIN.blit(game_over_message , font_pos_message)
        WIN.blit(game_over_score , font_pos_score)
        pygame.display.update()

        #Click to continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()
        
        
#MAIN
def main():
    #Game time
    clock = pygame.time.Clock()
    
    snake_pos = [250,70] 
    snake_body = [[200,70], [190,70], [180,70]] #Starting body pieces
    
    direction = 'right' 
    score = 0
    rainbow_mode = False

    #Fruit info
    fruit_ate = False
    fruits = []
    fruit_limit = 1
    
    #Snake Stats
    speed_multiplier = 1
    
    def aRainbowFruitExists(onScreenFruits):
        for f in onScreenFruits:
            if f.getType() == 6:
                return True
            
        return False

    #game loop
    while True:
        #Events
        for event in pygame.event.get():
            #Quiting
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #Control input
        keys = pygame.key.get_pressed()
        #Checking same direciton to prevent instant switch movement
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and direction != 'down':
                direction = 'up'
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and direction != 'up':
                direction = 'down'
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and direction != 'left':
                direction = 'right'
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and direction != 'right':
                direction = 'left'        
        
        WIN.fill(BLACK) #background
        
        #Drawing Snake
        for square in snake_body:
            pygame.draw.rect(WIN ,GREEN, (square[0],square[1],10,10))
        
        
        #Directions
        if direction == 'right':
            snake_pos[0] += 10 * speed_multiplier
        elif direction == 'left':
            snake_pos[0] -= 10 * speed_multiplier
        elif direction == 'up':
            snake_pos[1] -= 10 * speed_multiplier
        elif direction == 'down':
            snake_pos[1] += 10 * speed_multiplier
        
        #Body adding
        snake_body.append(list(snake_pos))
        
        #Fruit generator
        i = 0
        while i < fruit_limit and len(fruits) < fruit_limit:
            doChooseRandNum = True
            while doChooseRandNum:
                randNum = random.randint(5,UNIQUE_FRUIT_TYPES)
                doChooseRandNum = False
                
                #Stopping snake from being able to shrink below 3 squares
                snakeTooSmall = len(snake_body) <= 3 and randNum == 4
                #Stopping multiple rainbow fruit spawning or spawning when in rainbow mode
                tooMuchRainbow = (rainbow_mode or aRainbowFruitExists(fruits)) and randNum == 6
                
                if snakeTooSmall or tooMuchRainbow: 
                    doChooseRandNum = True
            #end loop
            
            nFruit = Fruit([random.randrange(40,WIN_X-40),random.randrange(40,WIN_Y-40)], randNum)
            
            fruits.append(nFruit)
        
        #Fruit draw AND effect
        fruit_ate = False
        for f in fruits:
            f.draw()
            if pygame.Rect(snake_pos[0],snake_pos[1],10,10).colliderect(pygame.Rect(f.pos[0],f.pos[1],10,10)):
                #print("before: ", len(snake_body))
                score += 5
                fruits.remove(f)
                fruit_ate = True
                if f.fType == 1: #Double Score                  
                    score += 5
                elif f.fType == 2: #Speed Up
                    speed_multiplier += 0.05
                elif f.fType == 3: #Speed Down
                    speed_multiplier -= 0.025
                elif f.fType == 4: #Shrink
                    snake_body.pop(0)
                    snake_body.pop(0)
                elif f.fType == 5: #Grow Extra   
                    snake_body.append(list(snake_pos))
                elif f.fType == 6: #RAINBOW 
                    #rainbow_mode = True
                    # temp functionality
                    score += 50
                #print("after: ", len(snake_body))
            
        if fruit_ate == False:
            snake_body.pop(0) #Body shrink for movement        
        
        #Increasing fruit limit based on score
        if fruit_limit < MAX_FRUIT:
            fruit_limit = int(score / 50) + 10
        
        #Score rendering
        score_font = font.render(f'{score}' , True , WHITE)
        font_pos = score_font.get_rect(center=(WIN_X//2-40 , 30))
        WIN.blit(score_font , font_pos)
        
        #Update
        pygame.display.update()
        clock.tick(fps)
        print(pygame.time)
        
        #Body Hit, ignoring starting body elements (Game Over)
        for square in snake_body[:-3]: 
            if pygame.Rect(square[0],square[1],10,10).colliderect(pygame.Rect(snake_pos[0],snake_pos[1],10,10)):
                game_over(score)

        #Boundary hit (Game Over)
        pixel_nudge = 10
        if snake_pos[0]+pixel_nudge <= 0 or snake_pos[0] >= WIN_X or snake_pos[1] + pixel_nudge <= 0 or snake_pos[1] >= WIN_Y:
            game_over(score)

#Game call
main_menu()