import time
import logging
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def functionOpenPage(driver, page):
    driver.get(page)
    time.sleep(2)

def _wait_for_element(driver, by, value):
    return WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((by, value))
    )

def _click_element(driver, by, value):
    _wait_for_element(driver, by, value).click()
    time.sleep(1)
    logger.info(f"Elemento clickeado {value}")

def _send_text(driver, by, value, text):
    elem = _wait_for_element(driver, by, value)
    elem.send_keys(text)
    logger.info(f"Texto enviado a {value}")

def searchById(driver, id):
    return _wait_for_element(driver, By.ID, id)

def searchByClass(driver, class_name):
    return _wait_for_element(driver, By.CLASS_NAME, class_name)

def searchByXPath(driver, xpath):
    return _wait_for_element(driver, By.XPATH, xpath)

def selectClickButton(driver, xpath):
    _click_element(driver, By.XPATH, xpath)

def selectClickById(driver, id):
    _click_element(driver, By.ID, id)

def selectClickByClass(driver, class_name):
    _click_element(driver, By.CLASS_NAME, class_name)

def selectClickByXPath(driver, xpath):
    _click_element(driver, By.XPATH, xpath)

def introduceText(driver, id, text):
    _send_text(driver, By.ID, id, text)

def introduceTextById(driver, id, text):
    _send_text(driver, By.ID, id, text)

def introduceTextByClass(driver, class_name, text):
    _send_text(driver, By.CLASS_NAME, class_name, text)

def introduceTextByXPath(driver, xpath, text):
    _send_text(driver, By.XPATH, xpath, text)



