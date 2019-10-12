from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytesseract
import os
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains
import re
from selenium.common.exceptions import NoSuchElementException

def facebookLogin(driver):
    driver.get('http://www.facebook.com/')
    time.sleep(3)
    username = driver.find_element_by_css_selector("input[name=email")
    username.send_keys('')
    password = driver.find_element_by_css_selector('input[name=pass]')
    password.send_keys('')
    try:
        driver.find_element_by_css_selector('input[type=submit]').click()
    except:
        NoSuchElementException
    time.sleep(5)

def bumbleLogin(driver):
    driver.get("https://www.bumble.com/get-started")
    time.sleep(5)
    try:
        driver.find_element_by_xpath("//div[contains(@class, 'color-provider-facebook')]").click()
    except:
        NoSuchElementException

def readProfile(driver):
    actions = ActionChains(driver)
    profileText = []
    for x in range(5):
        driver.save_screenshot('screen.png')
        profileText.append(pytesseract.image_to_string(Image.open('screen.png')))
        if os.path.exists('screen.png'):
            os.remove('screen.png')
        actions.send_keys(Keys.ARROW_DOWN)
    judgeProfile(profileText, driver)

def judgeProfile(profileText, driver):
    ActionChains.send_keys(Keys.ARROW_LEFT) if (re.match('fluent in sarcasm',''.join(profileText))) else ActionChains.send_keys(Keys.ARROW_RIGHT)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    facebookLogin(driver)
    bumbleLogin(driver)
    readProfile(driver)
    time.sleep(5)
    driver.close()
