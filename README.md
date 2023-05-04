# game_development

I got this idea when researching games created in Python. I was watching a tutorial on how to build the classic Snake game in Python. I decided to follow along with the video tutorial, writing my own code alongside this one, while making some subtle changes along the way.

Instead of having a snake eating food to grow, I’ve adapted the concept to be an alien eating planets and growing larger as it devours more planets. I may implement certain points scoring system, challenges and special abilities to assist the player, depending on the challenges I find along the way.

I start by drawing the game window. I'll be using pygame in this assignment, this is a tool which has been developed by the Python community, which allows the programmer to easily write codes by calling on functions created previously by the community and compiled into this library for a wider use.

After spending a couple of hours working through this tutorial, I encountered my first error whilst trying to run the game. I was encountering an ‘unbound local error’. This was frustrating and the code at first glance appeared to be all correct. After further debugging, I noticed I had forgotten the ending brackets when calling the block move class. After this was rectified, I was able to get my block moving across the screen when pressing directional buttons. 

During my time following this walkthrough, it has become apparent that I keep missing the Parenthesis. This I’ll need to be sure to double check going forward.

27/01/23 
Working through the tutorial, I came across an error which I must have made a while ago regarding the collision. I mistyped whilst following the code and I was getting an error until I combed through the source code to see what the mistake was.  

28/01/23
Created the game assets myself by utilising pixelart (https://www.pixilart.com/draw)
At this stage I'm now looking at how to implement collision detection around the borders of the window. Currently I'm finding it difficult to implement this. I've tried several iterations of code and the game hits game over immediately.

18/04/23
This project has been quite a few months as other assignments had to take some precedent, an update to the project:

Scott Morgan commit:
This commit adds the ability to catch particles exiting the y-value bounding box. In particular (aside from adding a .gitignore to exclude my virtual environment files). this PR adds the following to main.py (line 215-219):

if (self.alien.y[0] <= 0) or (self.alien.y[0] >= 800):
                print(f"x = {self.alien.x[0]}, y = {self.alien.y[0]}")
                self.show_game_over()
                pause = True
                self.reset()
This catches the exiting of the vertical domain. Horizontal is left to you!

Scott Morgan helped understand the collision issue I was having. After giving me an example I was able to successfully implement collision for the walls of the game.


Going forward the project will have more time committed to it. I'm working through the assessment document and compiling all the required assets. This document should see more updates.

#### Criteria ####

appeal to children aged around 8-12.

The game involves navigating a character around an area collecting items and avoiding hazards.

Collecting items adds to your score, colliding with hazards uses up lives, of which each game character only has a limited number.

For example the player could direct a mouse around a house collecting pieces of cheese, but the mouse needs to avoid cats (hazards) which occupy the house. 

The game should be timed, with player performance based on the score achieved over a certain time. 

It should also have levels of difficulty with more difficult levels having more hazards, fewer lives or a shorter time. 

The game should be exciting and fun to play, as well as visually appealing.

*** This criteria has been met, it's appealing to children, it involves moving an alien around space collecting planets and avoiding its growth and borders. The input is keyboard, --need to add timer to countdown-- it gets harder the longer they play. One life only!

Tuesday 2nd May:

I define a new font and size for the timer display using pygame.font.SysFont, using the same settings as the other text.

I am able to get the current time when the game starts using pygame.time.get_ticks() and save it in the start_time variable.

Setting the timer to 2 minutes in milliseconds is done by multiplying 2 minutes by 60 seconds per minute and 1000 milliseconds per second and saving it in the time_limit variable.

I'm then defining a new method called display_time that calculates the elapsed time since the game started by subtracting the start_time from the current time using pygame.time.get_ticks(). Then calculate the time left in seconds by subtracting the elapsed time from the time_limit and using the max function to ensure that the time left never goes below 0. Finally divide the time left by 1000 to convert it from milliseconds to seconds.

Render the time left as text using the timer font and size defined earlier, and blit it onto the surface at position (800, 100) using self.surface.blit. 

I also have the code check if the time left is 0, and if so, we call the show_game_over method.


Tuesday 2nd May #2:

I'm creating a feedback form in Google Forms which I'm going to distribute to the class for some feedback. I'm aware of some small generic bugs and tweaks which could make the game run better, these will be addressed providing time isn't to tight. Depending of the feedback recieved, I'll be prioritising any issues found as a result of the testing document. 


Thursday 4th May:

Feedback information recieved: 

** If I click in the againt the direction of the snake it causes the game to stop completely. Caused the game to stop completely having to make me close the program to restart.

Sprites have black boxes around them and it only sometimes will end the game if you move back into the trail of aliens.

Make the snake move slower at the start but speed up as it grows.

It was fun to play. I suggest adding a bit where it tells you your high score to play. This can incentivise people to play more.**


Within the timeframe I have available, making the sprite have a transparent background would be possible, it would also be worth looking at why the game occasionally bugs out when pressing the key that moves back on itself. 
When looking at the PNG file, the white space is actually already transparent, however that is not being projected onto the game background. i'll have to spend some time looking into what is causing this issue.

![image](https://user-images.githubusercontent.com/92015993/236187737-15bd45f8-aa62-4c69-80c5-c0fc7fdb5091.png)

This was caused by the Alpha channel of the PNG file to not be used. By loading the image with convert_alpha() we see that the alien no longer has the white parameters. I did the same to the planet asset too which makes the game look cleaner. 
