import unittest
import cv2
import sys
import os
from main.clickAutomationHelper import *
from main.screenshots import *
from main.imagesearch import *
from pathlib import Path
import logging
import threading
from queue import Queue
from threading import Thread
import time
import tracemalloc


##################################################
# NOTE: You should not move mouse during tests. ##
##################################################


class RaidAutoClickerTests(unittest.TestCase):
    project_dir = str(Path(__file__).parents[1])
    screenshots_dir = project_dir + '\\main\\screenshots\\'
    thread_queue = Queue(maxsize=2)

    parent_dir = os.getcwd()
    file_path = os.path.abspath(__file__)

    def open_image_timed(self, image_name):
        img_location = screenshots_dir+image_name+'.png'
        img = cv2.imread(img_location)
        cv2.imshow('tesImage', img)
        cv2.moveWindow('tesImage', 0, 0)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
        self.thread_queue.put(True)

    def search_image(self, button_name):
        self.thread_queue.put(click_button(button_name))

    def assert_that_button_has_been_clicked(self, image_name):
        open_image_thread = Thread(target=self.open_image_timed, args=(image_name,))
        search_image_thread = Thread(target=self.search_image, args=(image_name,))

        open_image_thread.start()
        time.sleep(.1)
        search_image_thread.start()

        open_image_thread.join()
        search_image_thread.join()

        return self.thread_queue.get(),self.thread_queue.get()

    def test_battle_button_can_be_clicked(self):
        image_name = 'button_battle'
        image_path = self.screenshots_dir + image_name
        self.assertEqual(self.assert_that_button_has_been_clicked(image_name)[1],True)

    def test_index_button_can_be_clicked(self):
        image_name = 'button_index'
        image_path = self.screenshots_dir + image_name
        self.assertEqual(self.assert_that_button_has_been_clicked(image_name)[1],True)

    def test_portal_button_can_be_clicked(self):
        image_name = 'button_portal'
        image_path = self.screenshots_dir + image_name
        self.assertEqual(self.assert_that_button_has_been_clicked(image_name)[1],True)

    # def test_if_given_wrong_filename_return_file_not_found_exception(self):
    #     image_name = 'buttosn_battle.png'
    #     image_path = self.screenshots_dir + image_name
    #     self.assertEqual(click_button(image_path), "File not found.")


if __name__ == '__main__':

    tracemalloc.start()

    unittest.main()

    memory_allocation_snapshot = tracemalloc.take_snapshot().statistics('lineno')

    print("[ Top 10 ]")
    for stat in memory_allocation_snapshot[:10]:
        print(stat)
