
from graphics import *
def main():
    win = GraphWin("Tic Tac Toe",400,300)
    win.setCoords(0.0,0.0,3.0,3.0)

    # draw grid  interface
    #  Draw vertical lines
    Line(Point(1, 0), Point(1, 3)).draw(win)
    Line(Point(2, 0), Point(2, 3)).draw(win)

    #  Draw horizontal lines
    Line(Point(0, 1), Point(3, 1)).draw(win)
    Line(Point(0, 2), Point(3, 2)).draw(win)

    #define counter and list
    list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    count = 0

    while count <9:
        count = count + 1
        if count%2 == 0:
            flag = True
        else:
            flag = False
        click = win.getMouse()
        if click:
            FunctionClick(click, win, flag)

    win.getMouse()

    win.close()


def FunctionClick(pt, win,flag):

    if pt.getX() > 0 and pt.getX() < 1:
        if pt.getY() > 0 and pt.getY() < 1:
            point = Point(0.5, 0.5)
            DrawFunction(point, win, flag)
    if pt.getX() > 0 and pt.getX() < 1:
        if pt.getY() > 1 and pt.getY() < 2:
            point = Point(0.5, 1.5)
            DrawFunction(point, win, flag)
    if pt.getX() > 0 and pt.getX() < 1:
        if pt.getY() > 2 and pt.getY() < 3:
            point = Point(0.5, 2.5)
            DrawFunction(point, win, flag)

    if pt.getX() > 1 and pt.getX() < 2:
        if pt.getY() > 0 and pt.getY() < 1:
            point = Point(1.5, 0.5)
            DrawFunction(point, win, flag)
    if pt.getX() > 1 and pt.getX() < 2:
        if pt.getY() > 1 and pt.getY() < 2:
            point = Point(1.5, 1.5)
            DrawFunction(point, win, flag)
    if pt.getX() > 1 and pt.getX() < 2:
        if pt.getY() > 2 and pt.getY() < 3:
            point = Point(1.5, 2.5)
            DrawFunction(point, win, flag)

    if pt.getX() > 2 and pt.getX() < 3:
        if pt.getY() > 0 and pt.getY() < 1:
            point = Point(2.5, 0.5)
            DrawFunction(point, win, flag)
    if pt.getX() > 2 and pt.getX() < 3:
        if pt.getY() > 1 and pt.getY() < 2:
            point = Point(2.5, 1.5)
            DrawFunction(point, win, flag)
    if pt.getX() > 2 and pt.getX() < 3:
        if pt.getY() > 2 and pt.getY() < 3:
            point = Point(2.5, 2.5)
            DrawFunction(point, win, flag)

def DrawFunction(point, win, flag):
    if flag == True:
        circle = Circle(point, 0.3)
        circle.setFill('lightblue')
        circle.draw(win)
    else:
        line1 = Line(Point(point.getX()+0.3, point.getY()+ 0.3),Point(point.getX()-0.3, point.getY()-0.3))
        line1.setFill('green')
        line1.draw(win)
        line2 = Line(Point(point.getX() - 0.3, point.getY() + 0.3), Point(point.getX() + 0.3, point.getY() - 0.3))
        line2.setFill('green')
        line2.draw(win)





main()