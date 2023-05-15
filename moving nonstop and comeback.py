# import pygame module in this program 
import pygame
  
# activate the pygame library
pygame.init()
  
# create the display surface dimension
keyyard = pygame.display.set_mode((500, 500))
  
# set the pygame window name 
pygame.display.set_caption("Moving nonstop and comeback")
  
# object current coordinates 
x = 0
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
    
         # if not jumping
    if not(isJump): 
        # if space bar is pressed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        # if space bar is pressed
        if jumpCount >= -15: #count down the jump count until it reaches -20 (to get back the original position)
                y -= (jumpCount * 2) * 0.5 # this is the formula for smooth jump: y = (x * abs(x)) * 0.5, x is the time of the jump
                jumpCount -= 1 
        else: 
                # making isJump equal to False when done, reseting the jumpCount
                jumpCount = 15
                isJump = False
         
              
    # completely fill the surface object  
    # with black colour  
    keyyard.fill((0, 0, 0)) # this will also remove the previous rectangle
      
    # drawing object on screen which is rectangle here 
    pygame.draw.rect(keyyard, (255, 0, 0), (x, y, width, height))
      
    # it refreshes the window
    pygame.display.update() 
  
# closes the pygame window 
pygame.quit()