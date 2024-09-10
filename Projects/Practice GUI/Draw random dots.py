from graphics import *

def create_window():
    """Create and return a graphics window."""
    win = GraphWin("Simple Drawing Program", 800, 600)
    return win

def draw_point(win, x, y):
    """Draw a point on the window at the specified coordinates."""
    point = Point(x, y)
    point.draw(win)
    return point

def clear_screen(win, points):
    """Clear the screen by undrawing all points."""
    for p in points:
        p.undraw()
    points.clear()

def main():
    win = create_window()
    points = []

    while True:
        click_point = win.checkMouse()
        key = win.checkKey()

        if click_point:
            point = draw_point(win, click_point.getX(), click_point.getY())
            points.append(point)

        if key == "q":
            break
        elif key == "c":
            clear_screen(win, points)

    win.close()

if __name__ == "__main__":
    main()