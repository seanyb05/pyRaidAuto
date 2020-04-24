import pyautogui as ptg
import time
import win32gui
from imagesearch import *
from PIL import Image

from main.imagesearch import imagesearch, click_image


def this_is_on_screen(imageName, x1=None, y1=None, x2=None, y2=None):
    if x1 and y1 and x2 and y2:
        pos = imagesearcharea(imageName, x1, y1, x2, y2)
    else:
        pos = imagesearch(imageName, precision=.85)

    if pos[0] != -1:
        ptg.moveTo(pos[0], pos[1])
        return True
    else:
        return False


def click_button(buttonLocation):
    pos = imagesearch(buttonLocation)
    img = Image.open(buttonLocation)
    width, height = img.size
    if pos[0] != -1:
        click_image(buttonLocation, pos, "left", 0.001, offset=5)
        ptg.click(clicks=1, button='left')
        print(buttonLocation + " button clicked!")
    else:
        print(buttonLocation + " button not found!")


def drag_right_to_left(x=None, y=None):  # Drag from bottom of screen to top
    if x and y:
        ptg.moveTo(x, y)
        ptg.dragTo(1, y, .5, button='left')
    else:
        ptg.moveTo(1300, 300)
        ptg.dragTo(1, 300, .3, button='left')


def drag_bottom_to_top(x=None):  # Drag from bottom of screen to top
    if x:
        ptg.moveTo(x, 996)
        ptg.dragTo(x, 255, 1, button='left')
    else:
        ptg.moveTo(930, 996)
        ptg.dragTo(928, 255, 1, button='left')


def clickstage(stageNumber):
    pos = imagesearch(stageNumber, precision=.9)
    posList = list(pos)
    posList[0] = posList[0] + 859
    posList[1] = posList[1] + 50
    pos = tuple(posList)
    if pos[0] != -1:
        ptg.moveTo(pos[0], pos[1])
        ptg.click(clicks=1, button='left')
    else:
        print("Stage Number Not There")


def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


def move_to_end_of_chamption_list():
    drag_right_to_left(1342, 925)
    time.sleep(1)
    drag_right_to_left(1342, 925)
    time.sleep(1)
    drag_right_to_left(1342, 925)
    time.sleep(1)


def remove_old_food_champs(champ_position):

    if champ_position[0] == 1:
        ptg.moveTo(465, 291)
        ptg.click(clicks=1, button='left')
    if champ_position[1] == 1:
        ptg.moveTo(461, 484)
        ptg.click(clicks=1, button='left')
    if champ_position[2] == 1:
        ptg.moveTo(298, 394)
        ptg.click(clicks=1, button='left')


def click_last_four_champs_in_champ_list():

    ptg.moveTo(1360, 943)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)

    ptg.moveTo(1351, 764)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)

    ptg.moveTo(1226, 759)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)

    ptg.moveTo(1230, 940)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)



def sort_champ_list_by_level():
    ptg.moveTo(138, 607)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)
    ptg.moveTo(392, 492)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)

def run_max_level_routine():
    champ_position_array = []
    if this_is_on_screen("screenshots/word_max_level.png", 447, 403, 668, 732):
        print("max level 0")

    if this_is_on_screen("screenshots/word_max_level.png", 700, 391, 921, 863):
        print("max level 1")
        champ_position_array.append(1)
    else:
        champ_position_array.append(0)

    if this_is_on_screen("screenshots/word_max_level.png", 986, 409, 1200, 864):
        print("max level 2")
        champ_position_array.append(1)
    else:
        champ_position_array.append(0)

    if this_is_on_screen("screenshots/word_max_level.png", 1254, 399, 1467, 858):
        print("max level 3")
        champ_position_array.append(1)
    else:
        champ_position_array.append(0)

    if champ_position_array != [0, 0, 0]:
        click_button("screenshots/button_edit_team.png")
        time.sleep(1)
        if this_is_on_screen("screenshots/note_full_energy.JPG"):
            print("WARNING: Waiting 8 Minutes because out of energy.")
            time.sleep(600)
            click_button("screenshots/button_edit_team.png")
        time.sleep(1)
        remove_old_food_champs(champ_position_array)
        sort_champ_list_by_level()
        move_to_end_of_chamption_list()
        click_last_four_champs_in_champ_list()
        click_button("screenshots/button_start.png")
    else:
        print("No new max levels found")

def minimize_window():
    ptg.hotkey('win', 'down')


def from_home_navigate_to_campaign_12_3_start():
    if this_is_on_screen("screenshots/button_home_battle.png"):
        click_button("screenshots/button_home_battle.png")
        time.sleep(1)
        click_button("screenshots/button_campaign.png")
        time.sleep(1)
        drag_right_to_left()
        drag_right_to_left()
        drag_right_to_left()
        click_button("screenshots/campaign_12.png")
        time.sleep(1)
        drag_bottom_to_top()
        time.sleep(1)
        clickstage("screenshots/campaign_12_3.png")
        time.sleep(1)
        click_button("screenshots/button_start.png")

def click_all_heart_shields():

    while this_is_on_screen("screenshots/button_heart_shield.png"):
        click_x = 650
        click_y = 307
        click_y_shield_col(click_x, click_y)
        drag_bottom_to_top(x=650)

def click_y_shield_col(click_x, click_y):
    for x in range(0, 6):
        click_x_shield_row(click_x, click_y)
        click_y += 140


def click_x_shield_row(click_x, click_y):
    for x in range(0, 6):
        ptg.click(x=click_x, y=click_y, clicks=1, button='left', interval=0.02)
        click_x += 133



# class get_argument:
#     argument_list = argparse.ArgumentParser()
#     argument_list.add_argument("--database", "-db", help="Set the database you want to run this utility on.")
#     argument_list.add_argument("--execute", "-e", help="This will execute hive commands, if not added, logs will contain"
#                                                        " commands needed to be ran.")
#     args = argument_list.parse_args()
#
#     def database_name(self):
#         if self.args.database:
#             database_name = self.args.database
#             return database_name
#         # for x in range(3):
#         #     input("While executing, project did not find database variable, please enter database name now.")
#         #     if x == 3:
#         #         sys.exit("[ERROR] please enter database name.")
#
#     def execute_on(self):
#         if self.args.execute.upper() == "ON":
#             return True
#         return False

# class home_screen:
#
#     def navigate_to_campaign(self):
#         click_button("screenshots/button_home_battle.png")
#         return ""
#
#
#     def execute_on(self):
#         if self.args.execute.upper() == "ON":
#             return True
#         return False
#
# if __name__ == '__main__':
#     print("nothing")
