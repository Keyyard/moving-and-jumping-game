# import pygame module in this program 
import pygame
import random
# activate the pygame library
pygame.init()
  
# create the display surface dimension
keyyard = pygame.display.set_mode((500, 500))
  
# set the pygame window name 
pygame.display.set_caption("Moving nonstop and comeback")

# obstacle position
obstacle_x = 0
obstacle_y = 0
obstacle_width = 0
obstacle_height = 0
# object current coordinates 
x = 5
y = 400

# object width and height  
width = 20
height = 20
  
# velocity / speed of movement
vel = 3
  
# Indicates pygame is running
run = True
  
# Detects jump
isJump = False
jumpCount = 15

point = 0
# Game over test
game_over = 0
# infinite loop so it checks every change made to run
while run:
    # creates time delay of 10ms 
    pygame.time.delay(10)
      

    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False
    # stores keys pressed 
    keys = pygame.key.get_pressed()

    # if space bar is pressed  
    if keys[pygame.K_SPACE]:
        isJump = True
    
    #move right every second
    for i in range(100):
        if i%100 == 0:
            x += vel
        if i == 100:
            i = 0
    #if it comes to border of the screen, it will go back to the other side
    if x > 500:
        x = 0
        point = point + 1 #add point
    
         # if not jumping
    if not(isJump): 
        # if space bar is pressed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        # if space bar is pressed
        if jumpCount >= -15: #count down the jump count until it reaches -20 (to get back the original position)
                y -= (jumpCount * 2) * 0.5 # this is the formula for smooth jump: y = (x * abs(x)) * 0.5, x is the time of the jump
                vel = 6 #increase speed for the jump
                jumpCount -= 1 
        else: 
                # making isJump equal to False when done, reseting the jumpCount
                jumpCount = 15
                isJump = False
                vel = 3
         
              
    # completely fill the surface object  
    # with black colour  
    keyyard.fill((0, 0, 0)) # this will also remove the previous rectangle
    #fill the bottom part 450-500 with light green
    pygame.draw.rect(keyyard, (160, 231, 125), (0, 420, 500, 500))
    # drawing player on screen which is rectangle here 
    pygame.draw.rect(keyyard, (130, 182, 217), (x, y, width, height))
    # obstacle
    if x < 5:
        #randomize the obstacle position number that % 50 = 0
        obstacle_x = random.randint(100, 460)
        if obstacle_x % 50 != 0:
            obstacle_x = random.randint(100, 460)
        obstacle_y = 380
        obstacle_width = 40
        obstacle_height = 40

    # if the player hits the obstacle
    if x > obstacle_x and x < obstacle_x + obstacle_width or x + width > obstacle_x and x + width < obstacle_x + obstacle_width:
        if y > obstacle_y and y < obstacle_y + obstacle_height or y + height > obstacle_y and y + height < obstacle_y + obstacle_height:
            x = 500
            y = 500
            #game over text
            game_over = 1
    # draw obstacle
    pygame.draw.rect(keyyard, (239, 134, 119), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    #points
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render("Point: " + str(point), True, (255, 255, 255))
    keyyard.blit(text, (10, 10))
    # game over
    if game_over == 1:
        font_title = pygame.font.SysFont("comicsansms", 40)
        font_subtitle = pygame.font.SysFont("comicsansms", 20)
        text_title = font_title.render("Game Over", True, (255, 255, 255))
        text_subtitle = font_subtitle.render("Press Enter to restart", True, (255, 255, 255))
        text_title_rect = text_title.get_rect(center=(500/2, 500/2))
        text_subtitle_rect = text_subtitle.get_rect(center=(500/2, 500/2+50))
        keyyard.blit(text_title, (150, 200))
        keyyard.blit(text_subtitle, (150, 250))
        obstacle_x = 0
        obstacle_y = 0
        obstacle_width = 0
        obstacle_height = 0
        vel = 0

    # if key press = enter, reset the game
    if keys[pygame.K_RETURN]:
        x = 4
        y = 400
        game_over = 0
        vel = 3
        point = 0

    # it refreshes the window
    pygame.display.update() 
# closes the pygame window 
pygame.quit()