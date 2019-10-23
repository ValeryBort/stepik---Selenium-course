from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    # import ipdb; ipdb.sset_trace(); print()
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    get_num = browser.find_element_by_css_selector("#input_value")
    num = int(get_num.text)
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(calc(num))
    option3 = browser.find_element_by_css_selector("[type='submit']")
    option3.click()
    time.sleep(30)
