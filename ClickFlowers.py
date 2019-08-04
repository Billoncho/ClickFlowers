# ClickFlowers.py
# Billy Ridgeway
# Creates flowers on the screen where clicked.

import turtle           # Imports the turtle library.
import random           # Imports the random library.
turtle.bgcolor('black') # Sets the background color to black.
t = turtle.Pen()        # Creates a new pen called t.      
t.speed(0)              # Sets the pen's speed to fast.
t.hideturtle()          # Hides the pen.

# Creates a list of colors.
colors = ["red", "orange", "yellow", "blue", "green", 
        "purple", "white", "gray", "indigo"]

def drawAFlower(x,y):               # Defines the function drawAFlower.         
    t.penup()                       # Stops the pen from drawing.
    t.setpos(x,y)                   # Sets the pen's position on screen.
    t.pendown()                     # Sets the pen to draw.
    sFlower = random.choice(colors) # Randomly chooses the small flower's color.
    bFlower = random.choice(colors) # Randomly chooses the big flower's color.
    t.width(random.randint(1,5))    # Randomly choosed the pen's width.
    radius = random.randint(6,26)   # Randomly selects the flowers radius.
    t.pencolor(bFlower)             # Sets the big flower's color.
    for m in range(radius//2):      # Sets the range of m to the quotient of radius divided by 2.
        t.circle(radius)            # Draws a circle the size of radius.
        t.left(360/radius*2)        # Moves the pen left 360 degrees divided by twice the radius.
    t.pencolor(sFlower)             # Sets the small flower's color.
    for m in range(radius//2):      # Sets the range of m to the quotient of radius divided by 2.
        t.circle(radius/3)          # Draws a circle the size of radius divided by 3.
        t.left(360/radius*2)        # Moves the pen left 360 degrees divided by twice the radius.
turtle.onscreenclick(drawAFlower)   # Calls the function drawAFlower when the screen is clicked.
