from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import Bumble
import Tinder
import Email

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

if __name__ == "__main__":
    loginName = input("Your email/facebook login  :  ")
    loginPassword = input("Your facebook password  :  ")
    redFlag = input("what don't you like about people?  :  ")
    driver = webdriver.Chrome()
    facebookLogin(driver, loginName, loginPassword)
    Bumble.bumbleLogin(driver)
    Bumble.readProfile(driver)
    Tinder.tinderLogin(driver)
    Tinder.tinderSwipe(driver)
    Email.allDoneSwiping(loginName)


