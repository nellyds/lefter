from selenium import webdriver
import time
import pytesseract
import os
from PIL import Image
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def facebookLogin(driver, loginName, loginPassword):
    driver.get('http://www.facebook.com/')
    time.sleep(3)
    username = driver.find_element_by_css_selector("input[name=email")
    username.send_keys(loginName)
    password = driver.find_element_by_css_selector('input[name=pass]')
    password.send_keys(loginPassword)
    try:
        driver.find_element_by_css_selector('input[type=submit]').click()
    except:
        NoSuchElementException
        facebookLogin(driver, loginName, loginPassword)

def bumbleLogin(driver):
    driver.get("https://www.bumble.com/get-started")
    time.sleep(5)
    try:
        driver.find_element_by_xpath("//div[contains(@class, 'color-provider-facebook')]").click()
    except:
        NoSuchElementException
        bumbleLogin(driver)

def readProfile(driver):
    actions = ActionChains(driver)
    time.sleep(5)
    profileText = []
    for x in range(5):
        driver.save_screenshot('screen.png')
        profileText.append(pytesseract.image_to_string(Image.open('screen.png')))
        if os.path.exists('screen.png'):
            os.remove('screen.png')
        try:
            profileWindow = driver.find_element_by_xpath("//div[contains(@class, 'encounters-action--like')]")
            actions.move_to_element(profileWindow).send_keys(Keys.DOWN).perform()
        except:
            NoSuchElementException
            driver.close()
        time.sleep(1)
    profileText = ''.join(profileText)
    judgeProfile(profileText)

def buildRedFlagRegex(redFlag):
    redFlag = redFlag.split(",")
    return '^('+''.join(['(?!'+ x + ')' for x in redFlag])+'.)*$'

def judgeProfile(profileText):
    driver.find_element_by_xpath("//*[contains(@class, 'encounters-action--like')]").click() if \
        (re.match(buildRedFlagRegex(redFlag), profileText)) else \
        driver.find_element_by_xpath("//div[contains(@class, 'encounters-action--dislike')]").click()


def main_loop(driver):
    try:
        driver.find_element_by_xpath("//*[contains(text(), 'all caught up')]")
        driver.close()
    except:
        readProfile(driver)




if __name__ == "__main__":
    loginName = input("Your email/facebook login  :  ")
    # loginPassword = input("Your facebook password  :  ")
    redFlag = input("what don't you like about people?  :  ")
    driver = webdriver.Chrome()
    facebookLogin(driver, 'ndsilva822@gmail.com', 'ppfFrisky11')
    bumbleLogin(driver)
    main_loop(driver)


