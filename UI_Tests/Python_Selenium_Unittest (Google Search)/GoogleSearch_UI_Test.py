#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/opt/chromedriver')

    def test_googleSearch(self):
        page_url = "https://www.google.com/"
        driver = self.driver
        driver.maximize_window()
        driver.get(page_url)
        goo_input = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//*[contains(@class, 'gLFyf')]")))
        goo_input.clear()
        goo_input.send_keys("Test")
        goo_search_btn = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//*[contains(@class, 'gNO89b')]")))
        goo_search_btn.click()
        self.assertIn("Test -", driver.title)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
            unittest.main()
