import pyautogui as ptg
import time
import scroll_util as su
# import win32gui
from pathlib import Path
import imagesearch
from PIL import Image
import navigation

from imagesearch import imagesearch, click_image, imagesearcharea, region_grabber

project_dir = str(Path(__file__).parents[1])
screenshots_dir = project_dir + '\\pyRaidAuto\\screenshots\\'


def open_game():
    ptg.hotkey('win')
    ptg.typewrite('raid', interval=0.25)
    ptg.typewrite(['enter'], interval=0.25)
    time.sleep(2)
    ptg.hotkey('win', 'up')
    time.sleep(10)
    ptg.hotkey('win', 'down')
    time.sleep(1)
    ptg.hotkey('win', 'down')
    time.sleep(1)
    ptg.hotkey('win', 'up')

    exit_all_ads()


def close_game():
    ptg.hotkey('Alt', 'F4')
    time.sleep(2)
    click_button("button_exit_ok")


def this_is_on_screen(*given_images, x1=None, y1=None, x2=None, y2=None):

    image_found = None

    for images in given_images:
        image_path = screenshots_dir + images + '.png'
        if x1 and y1 and x2 and y2:
            pos = imagesearcharea(image_path, x1, y1, x2, y2)
        else:
            pos = imagesearch(image_path, precision=.85)

        pos = imagesearch(image_path, precision=.85)
        if pos[0] != -1:
            print("Found: " + images)
            image_found = str(images)

        else:
            print("Not Found: " + images)
            
    return image_found


def click_button(button_name):
    button_path = screenshots_dir + button_name + '.png'
    pos = imagesearch(button_path)
    img = Image.open(button_path)

    if pos[0] != -1:
        click_image(button_path, pos, "left", 0.001, offset=5)
        img.close()
        print("Clicked: " + button_name)
        return True
    else:
        img.close()
        print("NOT Clicke: " + button_name)
        return False


def wait_until_on_screen_then_click(*button_names):
    while True:
        for buttons in button_names:
            if not this_is_on_screen(buttons):
                print("Waiting for: ")
                time.sleep(1)
                continue
            else:
                click_button(buttons)
            return True


def wait_until_on_screen_dont_click(button_name):
    while not this_is_on_screen(button_name):
        print("Waiting for: " + button_name)
        time.sleep(1)
    return True


def click_button_area(button_name, x1, y1, x2, y2):
    button_path = screenshots_dir + button_name + '.png'
    pos = imagesearch(button_path)
    img = Image.open(button_path)

    im = region_grabber(region=(x1, y1, x2, y2))

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    # res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if pos[0] != -1:
        click_image(button_path, pos, "left", 0.001, offset=5)
        img.close()
        return True
    else:
        img.close()
        return False


def exit_all_ads():
    time.sleep(1)
    if this_is_on_screen("button_exit"):
        for x in range(10):
            time.sleep(1)
            click_button("button_exit")


def on_home_screen():
    return this_is_on_screen("note_playerName")


def drag_right_to_left(x=None, y=None):  # Drag from bottom of screen to top
    if x and y:
        ptg.moveTo(x, y)
        ptg.dragTo(1, y, .5, button='left')
    else:
        ptg.moveTo(1300, 300)
        ptg.dragTo(1, 300, .3, button='left')


def drag_bottom_to_top(x=None, y=None):  # Drag from bottom of screen to top
    if x and y:
        ptg.leftClick(x, y)
        ptg.dragTo(x, 255, .6, button='left')
    if x and not y:
        ptg.moveTo(x, 996)
        ptg.dragTo(x, 255, .6, button='left')
    if not x and not y:
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
    for x in range(0, 7):
        drag_right_to_left(1342, 925)
        time.sleep(.5)


def remove_old_food_champs(champ_position):
    while not this_is_on_screen("campaign_empty_championg_slot"):
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


def open_filter():
    ptg.moveTo(138, 607)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)


def if_vault_included_on_change_to_off():
    open_filter()
    if this_is_on_screen("button_includeVault"):
        click_button("button_includeVault")
        print("Found vault button")
    time.sleep(.25)


def sort_champ_list_by_level():
    ptg.moveTo(392, 492)
    ptg.click(clicks=1, button='left')
    time.sleep(.25)


def champion_is_max_level():
    time.sleep(1)
    champ_position_array = []
    if this_is_on_screen("word_max_level", 447, 403, 668, 732):
        print("max level 0")

    if this_is_on_screen("word_max_level", 700, 391, 921, 863):
        print("max level 1")
        champ_position_array.append(1)
    else:
        champ_position_array.append(0)

    if this_is_on_screen("word_max_level", 986, 409, 1200, 864):
        print("max level 2")
        champ_position_array.append(1)
    else:
        champ_position_array.append(0)

    if this_is_on_screen("word_max_level", 1254, 399, 1467, 858):
        print("max level 3")
        champ_position_array.append(1)
    else:
        champ_position_array.append(0)

    if champ_position_array != [0, 0, 0]:
        return champ_position_array


def minimize_window():
    ptg.hotkey('win', 'down')


def click_all_heart_shields():
    while this_is_on_screen("button_heart_shield"):
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


def click_battle_button():
    click_button("button_battle")
    print("Battle button found")


def quest_checker():
    click_button("button_quests")
    time.sleep(2)
    ptg.click(x=188, y=188)
    time.sleep(1)
    drag_bottom_to_top()
    time.sleep(1)
    return this_is_on_screen("quests_beat_campaign_3_times")


def summon_three_champions():
    click_button("button_portal")
    time.sleep(2)
    click_button("button_summon_buy")


def clan_boss_routine():
    click_button("button_battle")
    time.sleep(1)
    drag_right_to_left()
    time.sleep(1)
    click_button("battle_menu_clanBoss")
    time.sleep(1)
    drag_bottom_to_top(1311, 844)
    time.sleep(1)
    click_button("clanBoss_nightmare")
    time.sleep(1)
    click_button("clanBoss_button_battle")
    time.sleep(1)

    if this_is_on_screen("clanBoss_buy_key"):
        click_button("button_exit")
        time.sleep(.5)
        click_button("button_exit")
        time.sleep(.5)
        click_button("button_exit")
        time.sleep(.5)
        return

    click_button("clanBoss_button_start")
    while True:
        if this_is_on_screen("note_result"):
            click_button("button_replay")
            time.sleep(1)
            if this_is_on_screen("clanBoss_buy_key"):
                break
    click_button("button_bastion")
    click_button("button_bastion")


def get_image_coordinates(button_name):
    button_path = screenshots_dir + button_name + '.png'
    pos = imagesearch(button_path)
    return pos


def campaign_routine():
    victory_count = 0
    quest_complete_max = 0
    do_boss_campaign = True  # quest_checker()
    click_button("button_exit")
    time.sleep(1)
    click_button("button_battle")
    time.sleep(1)
    click_button("battle_menu_campaign")
    time.sleep(1)

    while (this_is_on_screen("campaign_12") == False):
        drag_right_to_left()

    time.sleep(.5)
    click_button("campaign_12")
    time.sleep(1)

    print(do_boss_campaign)
    if do_boss_campaign:
        while not this_is_on_screen("campaign_12_7"):
            drag_bottom_to_top()

        click_button("campaign_button_battle7")
        quest_complete_max = 3
        time.sleep(.5)
    else:
        ptg.click(x=1733, y=556)
        time.sleep(1)
        click_button("campaign_button_battle3")
        quest_complete_max = 7

    time.sleep(.5)
    click_button("campaign_button_start")

    while victory_count < quest_complete_max:
        champion_is_max_level()
        print("victory" + str(victory_count) + "max" + str(quest_complete_max))
        if this_is_on_screen("campaign_note_buy_energy"):
            victory_count -= 1
            time.sleep(600)
        if this_is_on_screen("button_replay"):
            click_button("button_replay")
            victory_count += 1
            time.sleep(1)

    while not this_is_on_screen("button_bastion"):
        continue
    click_button("button_bastion")


def summon_3_champions_routine():
    print("Running summon 3 champs routine.")
    summon_count = 0
    click_button("button_portal")
    time.sleep(1)
    click_button("portal_menu_button_summon")
    summon_count += 1
    time.sleep(5)

    while summon_count < 4:
        time.sleep(1)
        if this_is_on_screen("portal_menu_button_summonRepeat"):
            click_button("portal_menu_button_summonRepeat")
            summon_count += 1

    time.sleep(5)

    while True:
        if this_is_on_screen("button_exit"):
            click_button("button_exit")
            time.sleep(.5)
            click_button("button_exit")
            break


def you_can_battle_this_opponent(opponent_number):
    arena_button_list = [[1710, 393], [1710, 569], [1710, 744], [1710, 922], [1710, 393], [1710, 569], [1710, 744],
                         [1710, 923]]

    ptg.click(arena_button_list[opponent_number][0], arena_button_list[opponent_number][1])
    time.sleep(1)

    if this_is_on_screen("screen_type_advantage_map"):
        click_button("arena_button_start")
        return True

    return False


def arena_battle_opponent(opponent_button_location):
    ptg.click(opponent_button_location)
    print("Opponent location: " + str(opponent_button_location))
    time.sleep(1)

    if not this_is_on_screen("screen_type_advantage_map"):
        print("Was not able to start battle.")
        return False
    else:
        return True


def claim_quests_routine():
    click_button("button_quests")

    time.sleep(1)

    while this_is_on_screen("quests_button_claim"):
        print("found claim")
        click_button("quests_button_claim")
        click_button("quests_button_claim_daily")

    time.sleep(1)
    click_button("button_exit")


def tavern_routine():
    click_button("button_tavern")

    time.sleep(1)

    while not this_is_on_screen("tavern_emptyChampionSlot"):
        drag_bottom_to_top(80)

    time.sleep(1)

    for count in range(5):
        click_button("tavern_levelOneChamp")
        time.sleep(.5)


def there_are_no_notifications():
    if this_is_on_screen("notification_energy"):
        print("energy note")
        return False
    if this_is_on_screen("alert_maintenence"):
        print("maintenance")
        close_game()
        time.sleep(1800)
        open_game()
        return False


def replace_max_level_champs_with_new_champs(champions_maxed):
    wait_until_on_screen_then_click("screen_type_advantage_map")
    remove_old_food_champs(champions_maxed)
    if_vault_included_on_change_to_off()
    sort_champ_list_by_level()
    move_to_end_of_chamption_list()
    click_last_four_champs_in_champ_list()


def buy_green_gems():
    while this_is_on_screen("market_button_mysteryShard_img"):
        time.sleep(1)
        ptg.click(get_image_coordinates("market_button_mysteryShard_img")[0] + 500,
                  get_image_coordinates("market_button_mysteryShard_img")[1] + 50)
        time.sleep(1)
        click_button("market_menu_button_5000_buy")
        time.sleep(1)


def buy_ancient_shards():
    while this_is_on_screen("market_button_ancientShard_img"):
        ancient_shard_coordinates = get_image_coordinates("market_button_ancientShard_img")
        ptg.click(ancient_shard_coordinates[0] + 500, ancient_shard_coordinates[1] + 50)
        time.sleep(1)
        click_button("market_menu_button_200000_buy")
        time.sleep(1)


def sparringPit_click_upgrade_buttons():
    while this_is_on_screen("sparringPit_note_levelReady"):
        level_ready_coordinates = get_image_coordinates("sparringPit_note_levelReady")
        ptg.leftClick(level_ready_coordinates[0] + 250, level_ready_coordinates[1] + 650)
        time.sleep(1)


def sparringPit_change_max_level_champ():
    while this_is_on_screen("sparringPit_notification_maxLevel"):
        level_ready_coordinates = get_image_coordinates("sparringPit_notification_maxLevel")
        ptg.leftClick(level_ready_coordinates[0] + 250, level_ready_coordinates[1] + 300)
        time.sleep(1)
        click_button("sparringPit_button_sort_by_rank")
        time.sleep(1)
        ptg.click(415, 187)
        time.sleep(1)
        click_button("sparringPit_button_confirm")


def collect_daily_login():
    time.sleep(1)
    click_button("daily_login_tab")
    time.sleep(1)
    click_button("button_daily_login_rewards")
    time.sleep(1)
    click_button("button_exit")


def collect_playtime_rewards():
    time.sleep(1)

    click_button("button_playtimeRewards")
    time.sleep(1)

    click_button("playtimeReward1")
    time.sleep(.5)

    click_button("playtimeReward2")
    time.sleep(.5)

    click_button("playtimeReward3")
    time.sleep(.5)

    click_button("playtimeReward4")
    time.sleep(.5)

    click_button("playtimeReward5")
    time.sleep(.5)

    click_button("button_exit")    


if __name__ == "__main__":
    print("complete")
