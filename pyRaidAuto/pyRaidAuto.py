import clickAutomationHelper as cah
import navigation as nav
import auto_utils as auto
from pathlib import Path
import pyautogui as ptg
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import imagesearch
from imagesearch import imagesearch, click_image, imagesearcharea, region_grabber

# delay = 1.0
# button = Button.left
# start_stop_key = KeyCode(char='1')
# exit_key = KeyCode(char='e')
#
# class ClickMouse(threading.Thread):
#     def __init__(self, delay, button):
#         super(ClickMouse, self).__init__()
#         self.delay = delay
#         self.button = button
#         self.running = False
#         self.program_running = True
#
#     def start_clicking(self):
#         self.running = True
#
#     def stop_clicking(self):
#         self.running = False
#
#     def exit(self):
#         self.stop_clicking()
#         self.program_running = False
#
#     def run(self):
#         while self.program_running:
#             while self.running:
#                 count = 0
#                 count += 1
#                 print("count:" + str(count))
#                 # location = str(ptg.position())
#                 # print(location)
#                 # time.sleep(self.delay)
#                 auto_replay()
#                 # auto_classicArena_routine()
#                 # auto_teamArena_routine()
#                 # auto_dungeon_routine("spiders")
#                 # auto_all_tasks()
#                 # auto_dungeon_routine()
#                 auto_campaign_routine()
#                 # auto_classicArena_routine()
#                 time.sleep(1)
#
# mouse = Controller()
# click_thread = ClickMouse(delay, button)
# click_thread.start()
#
#
# def on_press(key):
#     if key == start_stop_key:
#         if click_thread.running:
#             click_thread.stop_clicking()
#         else:
#             click_thread.start_clicking()
#     elif key == exit_key:
#         click_thread.exit()
#         listener.stop()
#
#
# with Listener(on_press=on_press) as listener:
#     listener.join()

project_dir = str(Path(__file__).parents[1])
screenshots_dir = project_dir + '\\pyRaidAuto\\screenshots\\'

if __name__ == '__main__':
    # cah.auto_replay()
    time.sleep(3)
    # auto.auto_classicArena_routine()

    # if cah.this_is_on_screen("notification_classicArena_refillTokens"):
    #     print("Ran routine")
    #     cah.click_button("button_exit")
    #     nav.navigate_to_bastion_from_arena()
        

    # input = ("arena_button_auto_silver","arena_button_auto_gold")
    # cah.auto_classicArena_routine()
