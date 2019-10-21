from selenium import webdriver
import time
import pytesseract
import os
from PIL import Image
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Email import allDoneSwiping


def bumbleLogin(driver):
    driver.get("https://www.bumble.com/get-started")
    time.sleep(5)
    try:
        driver.find_element_by_xpath("//div[contains(@class, 'color-provider-facebook')]").click()
        time.sleep(5)
    except:
        NoSuchElementException
        bumbleLogin(driver)

def readProfile(driver):
    actions = ActionChains(driver)
    try:
        while (driver.find_element_by_xpath("//div[contains(@class, 'encounters-action--like')]")):
            profileText = []
            for x in range(6):
                driver.save_screenshot('screen.png')
                profileText.append(pytesseract.image_to_string(Image.open('screen.png')))
                if os.path.exists('screen.png'):
                    os.remove('screen.png')
                profileWindow = driver.find_element_by_xpath("//div[contains(@class, 'encounters-action--like')]")
                actions.move_to_element(profileWindow).send_keys(Keys.DOWN).perform()
                time.sleep(.5)
            profileText = ''.join(profileText)
        judgeProfile(profileText, driver)
    except:
        NoSuchElementException
        try:
            driver.find_element_by_xpath("//*[contains(text(), 'all caught up')]")

        except:
            NoSuchElementException
            readProfile(driver)

def buildRedFlagRegex(redFlag):
    redFlag = redFlag.split(",")
    return '^('+''.join(['(?!'+ x + ')' for x in redFlag])+'.)*$'

def judgeProfile(profileText, driver, redFlag):
    driver.find_element_by_xpath("//*[contains(@class, 'encounters-action--dislike')]").click() if \
        (re.match(buildRedFlagRegex(redFlag), profileText)) else \
        driver.find_element_by_xpath("//div[contains(@class, 'encounters-action--like')]").click()


# def main_loop(driver):
#     try:
#         readProfile(driver)
#     except:
#         try:
#             driver.find_element_by_xpath("//*[contains(text(), 'all caught up')]")
#
#         except:
#             NoSuchElementException
#

