import pygame
import random

pygame.init()
#initialises the pygame module

black=(0,0,0)
white= (255,255,255)
red= (255,0,0)

screenwidth= 900
screenheight= 600
gamewindow= pygame.display.set_mode((screenwidth, screenheight))
#sets height and width of the screen
pygame.display.set_caption("Arush's Snake Game")
#captions the screen
pygame.display.update()
#refreshes to show update

clock= pygame.time.Clock()
#clock stores the number of milliseconds (default= 0)
font= pygame.font.SysFont("Helvetica",20)
#font for the entire game

def textscreen(text, color, x, y):
    #defines the  function with text + color + coordinates
    screentext= font.render(text, False,color)
    gamewindow.blit(screentext, [x,y])
    #will add text on given coordinates

def plotsnake(gamewindow, color, snklist, snakesize):
#for drawking snake
    for x,y in snklist:
    #for each coordinate on topleft
        pygame.draw.rect(gamewindow, color, [x,y,snakesize, snakesize])
        #draws snake (snakesize variable is the same because it needs to be a square at the start)

def gameloop():
    exitgame= False
    gameover= False
    snakex=45
    snakey=55
    velocityx= 0
    velocityy=0
    snklist=[]
    snklength=1

    foodx=random.randint(20, screenwidth-20)
    #random.randint chooses random integers in between range...
    foody=random.randint(60, screenheight-20)
    score=0
    initvelocity=4
    snakesize=30
    fps=300
    #frames per second

    while not exitgame:
    #while exitgame not equal to True
        if gameover:
        #if gameover equals True
            gamewindow.fill(white)
            textscreen("Game Over! Press ENTER key to continue", red, 100,300)

            for event in pygame.event.get():
            #takes into account every event on the screen e.g clicks ect.
                if event.type== pygame.QUIT:
                #quit for cross button or Alt F4 ect.
                    exitgame= True
                if event.type== pygame.KEYDOWN:
                #takes into account every key press
                    if event.key==pygame.K_RETURN:
                    #if the enter key is pressed..
                        gameloop()
        else:
            for event in pygame.event.get():
            #for loop while the game is being played
                if event.type== pygame.QUIT:
                    exitgame= True

                if event.type== pygame.KEYDOWN:
                #takes into account every key press
                    if event.key==pygame.K_RIGHT:
                    #if right arrow key is pressed
                        velocityx=initvelocity
                        velocityy=0
                        #velocity y doesn't need to change
                        
                    if event.key== pygame.K_LEFT:
                        velocityx=-initvelocity
                        #velocity x changes in the other direction
                        velocityy=0

                    if event.key== pygame.K_UP:
                        velocityx=0
                        velocityy=-initvelocity
                        #snake goes upwards because in coding graph y decreases as you go up

                    if event.key==pygame.K_DOWN:
                        velocityx=0
                        velocityy=initvelocity
                snakex=snakex+velocityx
                snakey=snakey+velocityy

                if abs(snakex-foodx)<10 and abs(snakey-foody)<10:
                #checks if the snake is roughly eaten the food by checking the positive values of the coordinates
                    score+=1
                    foodx=random.randint(20, screenwidth-20)
                    foody=random.randint(60, screenheight-20)
                    snklength=snklength+5
                    #snake length is increases because food was eaten
                gamewindow.fill(white)
                #fills game window with white
                textscreen("Score:"+str(score),red,5,5)
                #displays score with red colour on top left
                pygame.draw.rect(gamewindow,red,[foodx,foody,snakesize,snakesize])
                #draws rectange for food by giving coordinates and size
                pygame.draw.line(gamewindow,red,(0,40),(900,40),5)
                #draws line underneath the score
                
                head=[]
                head.append(snakex) #head = [45]
                #adds x coordinates to the list
                head.append(snakey) #head= [45,55]
                #adds y coordinates to the list
                snklist.append(head) #snklist= [(45,55), ....]
                #adds both coordinates as tuples into a new lsit

                if len(snklist)>snklength:
                #if the length of the list is not equal to the food eaten...
                    del snklist[0]
                    #deletes the first value of the list

                if head in snklist[:-1]:
                #if snake head isn't the last element to show that the snake touched itself...
                    gameover= True

                if snakex<0 or snakex>screenwidth-20 or snakey>screenheight-20 or snakey<50:
                #checks if the snake has crossed the boundaries
                    gameover= True

                

                plotsnake(gamewindow,black,snklist, snakesize)

                
            pygame.display.update()
            #refreshes the screen
            clock.tick(fps)
            #defines speed of animations
gameloop()
            
                    
                        
            
