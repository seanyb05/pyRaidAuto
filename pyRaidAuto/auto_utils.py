import time
import clickAutomationHelper as cah
import navigation as nav
import scroll_util as scroll


def auto_classicArena_routine():
    arena_button_list = [
        [1710, 393],
        [1710, 569],
        [1710, 744],
        [1710, 922],
        [1710, 393],
        [1710, 569],
        [1710, 744],
        [1710, 923]
    ]

    arena_battle_button = 0

    time.sleep(1)

    nav.navigate_from_bastion_to_classic_arena()

    if cah.this_is_on_screen("arena_button_refreshList"):
        cah.click_button("arena_button_refreshList")
        time.sleep(1)

    while arena_battle_button < 8:

        if arena_battle_button > 3:
            scroll.scroll_bottom_to_top(694, 910)
            time.sleep(1)
            scroll.scroll_bottom_to_top(694, 910)
            time.sleep(1)

        if  cah.arena_battle_opponent(arena_button_list[arena_battle_button]):
            cah.click_button("arena_button_start")
            cah.wait_until_on_screen_then_click("arena_button_auto_silver","arena_button_auto_gold")
            cah.wait_until_on_screen_then_click("button_arena_tapToContinue")
            cah.wait_until_on_screen_then_click("button_arena_returnToArena")
            arena_battle_button += 1
            time.sleep(1)

        else:
            arena_battle_button += 1

            if cah.this_is_on_screen("notification_classicArena_refillTokens"):
                cah.click_button("button_exit")
                nav.navigate_to_bastion_from_arena()
                break

            # if this_is_on_screen("notification_5Tokens"):
            #     click_button("arena_button_confirm")
            #     time.sleep(1)
            #     continue

            # if this_is_on_screen("arena_button_useTokenRefill"):
            #     time.sleep(1)
            #     click_button("arena_button_confirmTokenRefill")
            #     time.sleep(1)
            #     continue

            if arena_battle_button == 7:
                nav.navigate_to_bastion_from_arena()
                break


def auto_teamArena_routine():
    arena_button_list = [
        [1710, 393],
        [1710, 569],
        [1710, 744],
        [1710, 922],
        [1710, 393],
        [1710, 569],
        [1710, 744],
        [1710, 923]
    ]

    arena_battle_button = 0

    time.sleep(1)

    navigate_from_bastion_to_tagTeam_arena()

    if this_is_on_screen("arena_button_refreshList"):
        click_button("arena_button_refreshList")
        print("Clicked refresh")
        time.sleep(1)

    while arena_battle_button < 8:

        if arena_battle_button > 3:
            drag_bottom_to_top(694, 910)
            time.sleep(1)
            drag_bottom_to_top(694, 910)
            time.sleep(1)

        if arena_battle_opponent(arena_button_list[arena_battle_button]):
            click_button("arena_button_start")
            while not this_is_on_screen("button_arena_tapToContinue"):
                time.sleep(.5)
                click_button("arena_button_auto")
            wait_until_on_screen_then_click("button_arena_tapToContinue")
            wait_until_on_screen_then_click("button_arena_returnToArena")
            arena_battle_button += 1
            time.sleep(1)

        else:
            arena_battle_button += 1

            if this_is_on_screen("arena_notification_tokens"):
                navigate_to_bastion_from_arena()
                break

            # if this_is_on_screen("notification_5Tokens"):
            #     click_button("arena_button_confirm")
            #     time.sleep(1)
            #     continue

            # if this_is_on_screen("arena_button_useTokenRefill"):
            #     time.sleep(1)
            #     click_button("arena_button_confirmTokenRefill")
            #     time.sleep(1)
            #     continue

            if arena_battle_button == 7:
                navigate_to_bastion_from_arena()
                break


def auto_campaign_routine():
    print("inside of campaign")
    time.sleep(1)

    navigate_to_campaign_12_3_from_bastion()

    if this_is_on_screen("notification_campaignMenu_restore_energy"):
        navigate_to_bastion_from_campaign()
        return
    else:
        click_button("campaign_button_battle3")
        time.sleep(1)

    while not this_is_on_screen("notification_campaign_restore_energy"):
        time.sleep(2)
        wait_until_on_screen_dont_click("button_replay")

        if this_is_on_screen("notification_campaign_restore_energy"):
            navigate_to_bastion_from_campaign()
            break

        if champion_is_max_level():
            champions_maxed = champion_is_max_level()
            click_button("button_edit_team")
            time.sleep(1)
            if this_is_on_screen("notification_campaign_restore_energy"):
                navigate_to_bastion_from_campaign()
                break
            replace_max_level_champs_with_new_champs(champions_maxed)
            time.sleep(1)
            click_button("button_start")

        click_button("button_replay")

    navigate_to_bastion_from_campaign()
    return


def auto_replay_campaign():
    print("inside of campaign")
    time.sleep(1)

    if this_is_on_screen("notification_campaignMenu_restore_energy"):
        navigate_to_bastion_from_campaign()
        return
    else:
        click_button("campaign_button_battle3")
        time.sleep(1)

    while not this_is_on_screen("notification_campaign_restore_energy"):
        time.sleep(2)
        wait_until_on_screen_dont_click("button_replay")

        if champion_is_max_level():
            champions_maxed = champion_is_max_level()
            click_button("button_edit_team")
            time.sleep(1)
            if this_is_on_screen("notification_campaign_restore_energy"):
                navigate_to_bastion_from_campaign()
                break
            replace_max_level_champs_with_new_champs(champions_maxed)
            time.sleep(1)
            click_button("button_start")

        click_button("button_replay")
    return


def auto_dungeon_routine(dungeon_type):
    navigate_to_open_dungeon_from_bastion(dungeon_type)

    time.sleep(1)

    for x in range(4):
        drag_bottom_to_top()

    time.sleep(1)

    ptg.click(1684, 920)

    time.sleep(1)

    if this_is_on_screen("notification_energy"):
        navigate_to_bastion_from_dungeon()
        return

    click_button("dungeon_button_start")
    time.sleep(1)

    wait_until_on_screen_then_click("button_bastion")
    print("exiting dungeon for loop")


def auto_leveling_routine():
    while True:
        if this_is_on_screen("alert_maintenence"):
            print("WARNING: Waiting 15 Minutes because of maintenence")
            click_button("button_replay")
            time.sleep(900)
            click_button("screenshots/button_maintenence_ok")
        time.sleep(1)
        champion_is_max_level()
        time.sleep(1)
        click_button("button_replay")
        time.sleep(1)


def auto_doomTower():
    i = 0
    while i < 10:
        time.sleep(1)
        if this_is_on_screen("button_doomTower_next"):
            i += 1
            click_button("button_doomTower_next")
            time.sleep(1)
            click_button("button_doomTower_start")
            time.sleep(1)


def auto_replay():
    while True:
        time.sleep(1)
        click_button("button_replay")

        if this_is_on_screen("notification_label_error"):
            click_button("notification_button_continue")


def auto_clan_boss():
    navigation.navigate_to_clan_boss_from_bastion()
    su.scroll_bottom_to_top(1311, 844)
    time.sleep(1)
    click_button("clanBoss_nightmare")
    time.sleep(1)
    click_button("clanBoss_button_battle")
    time.sleep(1)

    if this_is_on_screen("notification_clanBoss_buy_key"):
        click_button("button_exit")
        time.sleep(.5)
        click_button("button_exit")
        time.sleep(.5)
        click_button("button_exit")
        time.sleep(.5)
        return False

    # while True:
    #     if this_is_on_screen("note_result"):
    #         click_button("button_replay")
    #         time.sleep(1)
    #         if this_is_on_screen("clanBoss_buy_key"):
    #             break
    # click_button("button_bastion")
    # click_button("button_bastion")


def auto_all_tasks():
    collect_playtime_rewards()
    time.sleep(1)
    click_button("notification_gems")
    time.sleep(1)
    auto_market_routine()
    time.sleep(1)
    auto_sparringPit()
    time.sleep(1)
    auto_classicArena_routine()
    time.sleep(1)
    auto_teamArena_routine()
    time.sleep(1)
    auto_dungeon_routine("arcane")
    time.sleep(1)


def auto_market_routine():
    time.sleep(1)
    click_button("button_market")
    time.sleep(2)
    buy_green_gems()
    time.sleep(1)
    buy_ancient_shards()
    drag_bottom_to_top(764, 679)
    buy_green_gems()
    time.sleep(1)
    buy_ancient_shards()
    time.sleep(1)
    click_button("button_exit")


def auto_sparringPit():
    time.sleep(1)
    click_button("notification_sparringPit")
    time.sleep(1)
    sparringPit_click_upgrade_buttons()
    time.sleep(1)
    sparringPit_change_max_level_champ()
    click_button("button_exit")
