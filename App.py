from selenium import webdriver
import time
driver = webdriver.Chrome()


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
        print("That didn't work")

    time.sleep(5)

def bumbleLogin(driver):
    driver.get("https://www.bumble.com/get-started")
    time.sleep(58)
    try:
        driver.find_element_by_xpath("//div[contains(@class, 'color-provider-facebook')]").click()
    except:
        print("That didn't work")
    try:
        driver.find_element_by_xpath()
    except:
    driver.save_screenshot('screenshot.png')
facebookLogin(driver)
bumbleLogin(driver)
