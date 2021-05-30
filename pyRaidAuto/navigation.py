import clickAutomationHelper as cah
import scroll_util as su
import time

def navigate_to_clan_boss_from_bastion():
    cah.click_button("button_battle")
    time.sleep(1)
    su.scroll_right_to_left()
    time.sleep(1)
    cah.click_button("battle_menu_clanBoss")

def navigate_to_bastion_from_arena():
    print("WARNING: Returning to home screen from dungeon due to lack of energy.")
    for x in range(4):
        cah.click_button("button_battle")
        time.sleep(2)


def navigate_to_bastion_from_dungeon():
    print("WARNING: Returning to home screen from dungeon due to lack of energy.")
    for x in range(3):
        click_button("button_exit")
        time.sleep(1)

    click_button("button_bastion")


def navigate_to_open_dungeon_from_bastion(dungeon_type):
    click_button("button_battle")
    time.sleep(1)
    click_button("gameModes_dungeon")
    time.sleep(1)

    if dungeon_type == "force":
        click_button("dungeonMap_forceKeep")

    if dungeon_type == "void":
        click_button("dungeonMap_voidKeep")

    if dungeon_type == "spirit":
        click_button("dungeonMap_spiritKeep")

    if dungeon_type == "arcane":
        click_button("dungeonMap_arcaneKeep")

    if dungeon_type == "magic":
        click_button("dungeonMap_magicKeep")

    if dungeon_type == "spiders":
        drag_right_to_left()
        drag_right_to_left()
        time.sleep(1)
        click_button("dungeonMap_spidersDen")

    if dungeon_type == "dragons":
        drag_right_to_left()
        drag_right_to_left()
        time.sleep(1)
        click_button("dungeonMap_dragonsLair")

    if dungeon_type == "minataursLabrynth":
        drag_right_to_left()
        drag_right_to_left()
        time.sleep(1)
        click_button("dungeonMap_minataursLabrynth")

    if dungeon_type == "fireKnight":
        drag_right_to_left()
        drag_right_to_left()
        time.sleep(1)
        click_button("dungeonMap_fireKnightsCastle")


def navigate_to_campaign_12_3_from_bastion():
    click_button("button_battle")
    time.sleep(1)
    click_button("gameModes_campaign")
    time.sleep(1)

    while not this_is_on_screen("campaign_12"):
        drag_right_to_left()

    time.sleep(.5)
    click_button("campaign_12")
    time.sleep(.5)
    ptg.click(x=1733, y=556)
    time.sleep(1)
    # click_button("campaign_button_battle3")
    # time.sleep(1)

    if this_is_on_screen("campaign_empty_champion_slot"):
        sort_champ_list_by_level()
        move_to_end_of_chamption_list()
        click_last_four_champs_in_champ_list()

    click_button("button_start")

    # click_button("campaign_button_start")

    return


def navigate_to_bastion_from_campaign():
    print("WARNING: Returning to home screen due to lack of energy.")
    click_button("button_exit")
    time.sleep(1)
    click_button("button_exit")
    time.sleep(1)
    click_button("button_bastion")


def navigate_from_bastion_to_classic_arena():
    cah.click_button("button_battle")
    time.sleep(1)
    cah.click_button("gameModes_button_arena")
    time.sleep(1)
    cah.click_button("button_classicArena")
    time.sleep(1)


def navigate_from_bastion_to_tagTeam_arena():
    click_button("button_battle")
    time.sleep(1)
    click_button("gameModes_button_arena")
    time.sleep(1)
    click_button("button_tagTeamArena")
    time.sleep(1)


def navigate_from_bastion_to_campaign_12_3_start():
    if this_is_on_screen("button_home_battle"):
        click_button("button_home_battle")
        time.sleep(1)
        click_button("button_campaign")
        time.sleep(1)
        drag_right_to_left()
        drag_right_to_left()
        drag_right_to_left()
        click_button("campaign_12")
        time.sleep(1)
        drag_bottom_to_top()
        time.sleep(1)
        clickstage("campaign_12_3")
        time.sleep(1)
        click_button("button_start")

