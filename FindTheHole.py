# Find the Hole Graphics Game
# By: Areesh, Danna, Shreya
# Python Project for Loyola University Chicago

from graphics import *
import random
import math

#Sets graphical window up. 
win = GraphWin('FindTheHole', 500, 500)
win.setBackground('green')
win.yUp()

MessageSquare = Rectangle(Point(50, 480), Point(450, 460))
MessageSquare.setFill('white')
MessageSquare.setOutline('black')
MessageSquare.draw(win)

message = Text(Point(250, 470), 'Click around to find the hole! You have 12 tries!')
message.draw(win)

def DrawHole():
# Draws the target hole at a random location, hole must stay hidden at first. 

    randomPoint = Point(random.randint(40,460), random.randint(40,460))
    hole = Circle(randomPoint, 40)
    return hole

def getClick():
# Points out where the user has guessed and marks that place with a small red circle. 

    click = win.getMouse()
    clickLoc = Circle(click, 3)
    clickLoc.setFill('red')
    clickLoc.draw(win)
    return click

def partyHat():
# Displays a party hat when hole is found. Iterates through a for-loop to draw circles in the hat. 
    partyHat = Polygon(Point(430, 30), Point(460, 80), Point(490, 30))
    partyHat.setFill('cyan')
    partyHat.draw(win)
    
    hat1 = Circle(Point(460, 80), 10)
    hat2 = Circle(Point(463, 60), 5)
    hat3 = Circle(Point(450, 45), 5)
    hat4 = Circle(Point(470, 37), 5)
    circles = [hat1, hat2, hat3, hat4]
    colors = ['red', 'yellow', 'purple', 'pink']
    for item in circles:
      item.setFill(random.choice(colors))
      item.draw(win)

def holeFound(hole, click):
    '''Checks to see if the hole is found using distance formula.
    If the distance is less than the radius of the circle,
    it means the hole is found.''' 

    dx = click.getX() - hole.getCenter().getX() #difference in X coordinates
    dy = click.getY() - hole.getCenter().getY() # difference in Y coordinates
    distance = math.sqrt(dx**2 + dy**2) #distance formula
    
    if distance <= 40:
        hole.setOutline('black')
        hole.setFill('black')
        hole.draw(win)
        message.setText('Congratulations you found the hole! Click anywhere to quit.')
        partyHat()
        win.getMouse()
        win.close()

def main():
    '''Runs the main program. The player has 12 tries to find the hole.
    Program also tracks how many tries the user has taken and displays it.
    Program will stay running until the hole is found or the number of tries
    is less than 12. '''

    tries = 0
    hole = DrawHole()

    CounterSquare = Rectangle(Point(420, 30), Point(500, 10))
    CounterSquare.setFill('white')
    CounterSquare.setOutline('black')
    CounterSquare.draw(win)
    Counter = Text(Point(460, 20), 'Tries: ' + str(tries))
    Counter.draw(win)

    while tries < 12:
        click = getClick()
        holeFound(hole, click)
        tries = tries + 1
        Counter.setText('Tries: ' + str(tries))

    if tries >= 12:
        message.setText('You lost, click anywhere to exit the program.')
        hole.setOutline('black')
        hole.setFill('black')
        hole.draw(win)

    win.getMouse()
    win.close()

main()
