import random
import time
from graphics import *
import openpyxl

def main():
    win = GraphWin("Moving Circle", 500, 500)
    win.setCoords(0.0, 0.0, 4.0, 4.0)
    win.setBackground('lightgreen')
    score = 0

    start = Rectangle(Point(3,1), Point(1,3))
    start.setFill("lightgrey")
    start.draw(win)

    startText= Text(Point(2,2), "START")
    startText.setSize(30)
    startText.draw(win)

    while True:
        pt = win.getMouse()
        if pt:
            if pt.getX() > 1 and pt.getX() < 3:
                if pt.getY() > 1 and pt.getY() < 3:
                    start.undraw()
                    startText.undraw()
                    score = FunctionStart(win, score)

                    finish(win)
                    pt = win.getMouse()
                    if pt:
                        if pt.getX() > 1 and pt.getX() < 3:
                            if pt.getY() > 1 and pt.getY() < 3:
                                break

def create_button(win, label, p1, p2):
    button = Rectangle(p1, p2)
    button.setFill("lightgray")
    button.draw(win)

    text_point = Point((p1.getX() + p2.getX()) / 2, (p1.getY() + p2.getY()) / 2)
    text = Text(text_point, label)
    text.setSize(10)
    text.draw(win)

    return button



def FunctionStart(win,score):
    scorebox = Rectangle(Point(0, 3.5), Point(1, 4))
    scorebox.setFill("lightgrey")
    scorebox.draw(win)

    scoreText = Text(Point(0.5, 3.75), score)
    scoreText.setSize(20)
    scoreText.draw(win)

    Circles= []
    BlueCircles = []
    RedCircles= []

    while score < 5:
        for i in [1,2,3,4]:
            if i <4:
                time.sleep(0.2)
                circle = DrawBlue(win, Circles)
                Circles.append(circle)
                BlueCircles.append(circle)
                MoveCircles(Circles)

            else:
                time.sleep(0.2)
                circle = DrawRed(win, Circles)
                Circles.append(circle)
                RedCircles.append(circle)
                MoveCircles(Circles)

            click = win.checkMouse()
            if click:
                x = click.getX()
                y = click.getY()
                scoreText = changescore(win, RedCircles, BlueCircles, score, scorebox, scoreText, x, y)
                score = scoreText.getText()
                scoreText.draw(win)




def DrawBlue(win, Circles):
    circle = Circle(Point(random.randint(1,4), 3.5), 0.5)
    circle.setFill("blue")
    circle.draw(win)
    return circle

def DrawRed(win, Circles):
    circle = Circle(Point(random.randint(1, 4), 4), 0.5)
    circle.setFill("red")
    circle.draw(win)
    return circle

def MoveCircles(Circles):
    for circle in Circles:
        circle.move(0,-0.5)

def changescore(win, RedCircles, BlueCircles, score, scorebox, scoreText, x, y):
    score = calcscore(win, RedCircles, BlueCircles, score, scorebox, scoreText, x, y)
    scoreText.undraw()
    scoreText = Text(Point(0.5, 3.75), score)
    scoreText.setSize(20)
    return scoreText

def calcscore(win, RedCircles, BlueCircles, score, scorebox, scoreText, x, y):
        for circle in RedCircles:
            #gets x and y of center of the circle
            circle_x =circle.getCenter().getX()
            circle_y = circle.getCenter().getY()
            radius = circle.getRadius()
            # Check if the click is inside the circle
            distance = ((x - circle_x) ** 2 + (y - circle_y) ** 2) ** 0.5
            if distance <= radius:
                score = score-1
                circle.undraw()

        for circle in BlueCircles:
            #gets x and y of center of the circle
            circle_x = circle.getCenter().getX()
            circle_y = circle.getCenter().getY()
            radius = circle.getRadius()
            # Check if the click is inside the circle
            distance = ((x - circle_x) ** 2 + (y - circle_y) ** 2) ** 0.5
            if distance <= radius:
                score = score+1
                circle.undraw()

        return score



def finish(win):
    finish = Rectangle(Point(3, 1), Point(1, 3))
    finish.setFill("lightgrey")
    finish.draw(win)

    YouFinishText = Text(Point(2, 2), "You Won! \n Quit")
    YouFinishText.setSize(30)
    YouFinishText.draw(win)


main()