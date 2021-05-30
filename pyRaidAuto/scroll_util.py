import pyautogui as ptg

def scroll_right_to_left(x=None, y=None):  # Drag from bottom of screen to top
    if x and y:
        ptg.moveTo(x, y)
        ptg.dragTo(1, y, .5, button='left')
    else:
        ptg.moveTo(1300, 300)
        ptg.dragTo(1, 300, .3, button='left')

def scroll_bottom_to_top(x=None, y=None):  # Drag from bottom of screen to top
    if x and y:
        ptg.leftClick(x, y)
        ptg.dragTo(x, 255, .6, button='left')
    if x and not y:
        ptg.moveTo(x, 996)
        ptg.dragTo(x, 255, .6, button='left')
    if not x and not y:
        ptg.moveTo(930, 996)
        ptg.dragTo(928, 255, 1, button='left')