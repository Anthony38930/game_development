#time into video 1:11:30 https://www.youtube.com/watch?v=8dfePlONtls

import pygame # This is importing the pygame lbrary which allows us to call on predefined functions
import time # This will import the time module allowing our program to gain access the system time
from pygame.locals import * # Will import global variables of importance
import random # This will import the random module where we can randomise functions.

# Defining the global size variable for our assets. These assets are 40 x 40 pixels so by defining this, it allows us to call upon it when required for calculating positions.
SIZE = 40 

# By creating a class such as planet, we are creating an object in which we are able to create a set of methods which we can use throughout our game. 
class Planet:

    # Initialising the pygame module so we can use its functions and passing through attributes we want to use in the class
     def __init__(self, parent_screen): 

        # We need to pass through a parent surface as a class member called parent_screen
        self.parent_screen = parent_screen 

        # We have a resources folder containing important game assets. Here we pass through our planets image.
        self.image = pygame.image.load("resources/planet.png").convert() 
        
        # Defing the X and Y coordinates for where our planet will originally spawn in.
        self.x = 120 
        self.y = 120

     # This is where we define the function for how the planets get drawn onto our screen   
     def draw(self):

        # Blit (draw) at the pixels coordinates X, Y using the parent screen. This will pass through the X and Y coordinates 
        self.parent_screen.blit(self.image, (self.x, self.y)) 

        #This refreshes the screen so we can show the results of our code.
        pygame.display.flip() 

      # This function relatiosn to how we get the planets to move  
     def move(self):
        
        #We use the random module and one of its functions, randint. We supply it arguments that gives allows it to calculate a random spot to spawn the new planet
        #this calculation takes into account the size of the asset and the size of the window draw. This prevents the apple spawning outside the viewing window.
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE


# Our alien class which is where we define everything to do with our alien object. I've previously covered what most of these stages do, this applies to all new classes created
class Alien: 
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.alien = pygame.image.load("resources/alien.png").convert()

        # This is the direction in which our alien will start his direction.
        self.direction = 'down' 

        # Starting with one block in size and from coordinates 40, 40 (as we used the size variable to define where they spawn)
        self.length = 1 
        self.x = [SIZE]
        self.y = [SIZE]


    # We need to define our functions to enable us to navigate around our game screen. We are able to use the direction functions built into pygames library
    def move_left(self):
        self.direction = 'left'
                
    def move_right(self):
        self.direction = 'right'
    
    def move_up(self):
        self.direction = 'up'
        
    def move_down(self):
        self.direction = 'down'


    # I need further understanding behind the logic here - this was a lot to take in initially - Will be revisiting this stage
    def walk(self):
        
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
            
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        self.draw()

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.alien, (self.x[i], self.y[i]))
        pygame.display.flip()    


    # This function increases the size of our alien train.    
    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)    
    
    
# This is the class where we define all the objects relating to the running and functionality of our game    
class Game:
    def __init__(self):
        pygame.init()

        # Using the set_caption function built into pygame, we can give our game a window title.    
        pygame.display.set_caption("Hungry Aliens")

        # Initialising our game window (xxx,xxx pixels)
        self.surface = pygame.display.set_mode((1000,800))

        # Calling our alien and planet classes and drawing them onto our surface. 
        self.alien = Alien(self.surface)
        self.alien.draw()
        self.planet = Planet(self.surface)
        self.planet.draw()
    
    # Should the reset function be called we need to tell the game what to do, in this case, reset all the assets to their original position on the surface.
    def reset(self):
        self.alien = Alien(self.surface)
        self.planet = Planet(self.surface)   

    # Here is where we define our collision detection, complex code, need more time analysing before writing a description
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False
    
    # Defining where our background image comes from for our game and where to display it from, 0, 0 being top left corner.
    def render_background(self):
        bg = pygame.image.load("resources/background.jpg").convert()
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_background()
        self.alien.walk()
        self.planet.draw()
        self.display_score()
        pygame.display.flip()
        
        #aliens colliding with planet
        if self.is_collision(self.alien.x[0], self.alien.y[0], self.planet.x, self.planet.y):
            self.alien.increase_length()
            self.planet.move()
            
        #aliens colliding with themselves
        for i in range(2, self.alien.length):
            if self.is_collision(self.alien.x[0], self.alien.y[0], self.alien.x[i], self.alien.y[i]):
                raise ("Collision Occured")

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.alien.length}", True, (200, 200, 200))
        self.surface.blit(score, (850,10))            

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! You uncontrollably ate to much, final score is:  {self.alien.length}", True, (255, 255, 255))
        self.surface.blit(line1, (100, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()

    def run(self):
        
#Here we will create our even loop while it waits for our keyboard input

        running = True #Setting a variable to define if our game is running
        pause = False

        while running:
            for event in pygame.event.get(): # This will allow us to use events from the pygame library which will allow us to use keystrokes and user inputs
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False


                    if event.key == K_RETURN:
                        pause = False

                    if not pause:    
                        if event.key == K_UP:   # When the appropriate arrow key, the block will move +/- 10 pixels along the appropriate axis
                            self.alien.move_up()
                                                
                        
                        if event.key == K_DOWN:
                            self.alien.move_down()
                        
                        
                        if event.key == K_LEFT:
                            self.alien.move_left()
                                                
                        
                        if event.key == K_RIGHT:
                            self.alien.move_right()
                                                
            
                       
                elif event.type == QUIT:
                    running = False
                    
            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()


        
            time.sleep(.1)
   
    
if __name__ == "__main__":   #This is where we initialise the module
    game = Game()
    game.run()
