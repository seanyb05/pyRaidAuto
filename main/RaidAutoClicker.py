import time
from main.clickAutomationHelper import *


if __name__ == '__main__':
    # click_all_heart_shields()

    while True:
        if this_is_on_screen("screenshots/note_full_energy.JPG"):
            print("WARNING: Waiting 8 Minutes because out of energy.")
            time.sleep(600)
        if this_is_on_screen("screenshots/alert_maintenence.png"):
            print("WARNING: Waiting 15 Minutes because of maintenence")
            time.sleep(900)
            click_button("screenshots/button_maintenence_ok.png")
        # run_max_level_routine()
        time.sleep(1)
        click_button("screenshots/button_replay.png")
        time.sleep(2)
