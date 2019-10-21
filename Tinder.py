from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

def tinderLogin(driver):
    driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[2]/div/div[3]/div/button/span").click()
    time.sleep(3)

def tinderSwipe(driver):
    actions = ActionChains(driver)
    try:
        while (driver.find_element_by_xpath("//div[contains(@aria-label, 'Like')]")):
            time.sleep(.5)
            actions.move_to_element(driver.find_element_by_xpath("//div[contains(@aria-label, 'Like')]")).click().perform()
    except:
        NoSuchElementException


