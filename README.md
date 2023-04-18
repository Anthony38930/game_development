# game_development

I got this idea when researching games created in Python. I was watching a tutorial on how to build the classic Snake game in Python. I decided to follow along with the video tutorial, writing my own code alongside this one, while making some subtle changes along the way.

Instead of having a snake eating food to grow, I’ve adapted the concept to be an alien eating planets and growing larger as it devours more planets. I may implement certain points scoring system, challenges and special abilities to assist the player, depending on the challenges I find along the way.

I start by drawing the game window, I’l be using pygame in this assignment, this is a tool which has been developed by the Python community, which allows the programmer to easily write codes by calling on functions created previously by the community and compiled into this library for a wider use.

After spending a couple of hours working through this tutorial, I encountered my first error whilst trying to run the game. I was encountering an ‘unbound local error’. This was frustrating and the code at first glance appeared to be all correct. After further debugging, I noticed I had forgotten the ending brackets when calling the block move class. After this was rectified, I was able to get my block moving across the screen when pressing directional buttons. 

During my time following this walkthrough, it has become apparent that I keep missing the Parenthesis. This I’ll need to be sure to double check going forward.

27/01/23 
Working through the tutorial, I came across an error which I must of made a while ago regarding the collision. I mistyped whilst following the code and I was getting an error until I combed through the source code to see what the mistake was.  

28/01/23
Created the game assets myself by utiling pixelart (https://www.pixilart.com/draw)
At this stage I'm now looking at how to impliment collision detection around the borders of the window. Currently i'm finding it difficult to impliment this. I've tried several iterations of code and the game hits game over immediately.

18/04/23
This project has been quiet a few months as other assignments had to take some precident, an update to the project:

Scott Morgan commit:
This commit adds the ability to catch particles exiting the y-value bounding box. In particular (aside from adding a .gitignore to exclude my virtual environment files). this PR adds the following to main.py (line 215-219):

if (self.alien.y[0] <= 0) or (self.alien.y[0] >= 800):
                print(f"x = {self.alien.x[0]}, y = {self.alien.y[0]}")
                self.show_game_over()
                pause = True
                self.reset()
This catches the exiting of the vertical domain. Horizontal is left to you!

Scott Morgan helped understand the collision issue I was having. After giving me an example I was able to successfully impliment collision for the walls of the game.


Going forward the project will have more time committed to it. I'm working through the assesment document and compiling all the required assets. This document should see more updates.
