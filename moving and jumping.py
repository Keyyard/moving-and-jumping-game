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
obstacle_x = 700
obstacle_y = 700
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

#cloud x and y
cloud_x = 480
cloud2_x = 200
cloud_y = 20
cloud2_y = 40
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
    if keys[pygame.K_SPACE] and y == 400:
        isJump = True
    
    #move right every 100ms
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
        if keys[pygame.K_SPACE] and game_over == 0:
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
    # with sky colour  
    keyyard.fill((90,188,216)) # this will also remove the previous rectangle
    #fill the bottom part 450-500 with light green
    #ground 
    ground = pygame.image.load('ground.png')
    ground_rect = ground.get_rect()
    #scale up the ground
    ground = pygame.transform.scale(ground, (80, 80))
    ground_rect.bottom = 440
    #fill the bottom with ground
    #ground cover screen
    for i in range(0, 500, 80):
        keyyard.blit(ground, (i, 420))

    #pygame.draw.rect(keyyard, (160, 231, 125), (0, 420, 500, 500))
    # drawing player on screen which is rectangle here 
    player = pygame.image.load('char.png')
    player_rect = player.get_rect()
    #scale up the player
    player = pygame.transform.scale(player, (40, 40))
    # obstacle 1
    if x < 5:
        #randomize the obstacle position number that % 50 = 0
        obstacle_x = random.randint(100, 460)
        if obstacle_x % 50 != 0:
            obstacle_x = random.randint(100, 460)
        obstacle_y = 400
        obstacle_width = 40
        obstacle_height = 40

    # if the player hits the obstacle
    if x > obstacle_x and x < obstacle_x + obstacle_width or x + width > obstacle_x and x + width < obstacle_x + obstacle_width:
        if y > obstacle_y and y < obstacle_y + obstacle_height or y + height > obstacle_y and y + height < obstacle_y + obstacle_height:
            x = 500
            y = 500
            #game over text
            game_over = 1
    obstacle = pygame.image.load('spike.png')
    obstacle_rect = obstacle.get_rect()
    #scale up the obstacle 1 
    obstacle = pygame.transform.scale(obstacle, (40, 40))
    obstacle_rect.bottom = 400
    keyyard.blit(obstacle, (obstacle_x, obstacle_y))

    # clouds
    cloud = pygame.image.load('cloud.png')
    cloud_rect = cloud.get_rect()
    #scale up the cloud
    cloud = pygame.transform.scale(cloud, (180, 180))
    cloud2 = pygame.transform.scale(cloud, (180, 180))
    if cloud_x <= -180:
        cloud_x = 480
        cloud_y = random.randint(10, 40)
    cloud_x = cloud_x - 1
    cloud2_x = cloud2_x - 1
    if cloud2_x <= -180:
        cloud2_x = 480
        cloud2_y = random.randint(10, 40)
    keyyard.blit(cloud, (cloud_x, cloud_y))
    keyyard.blit(cloud2, (cloud2_x, cloud2_y))
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
        obstacle_x = 700
        obstacle_y = 700
        obstacle_width = 0
        obstacle_height = 0
        vel = 0

    # if key press = enter, reset the game
    if keys[pygame.K_RETURN] and game_over == 1:
        x = 4
        y = 400
        game_over = 0
        vel = 3
        point = 0
    # render player
    keyyard.blit(player, (x, y))
    # it refreshes the window
    pygame.display.update() 
# closes the pygame window 
pygame.quit()