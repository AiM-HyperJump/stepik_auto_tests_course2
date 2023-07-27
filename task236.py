from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    my_link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(my_link)
    browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()
    browser.switch_to.window(browser.window_handles[1])
    x= int(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(math.log(abs(12*math.sin(x))))
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    print(browser.switch_to.alert.text[browser.switch_to.alert.text.find(":")+1:])
    browser.switch_to.alert.accept()
   


finally:
    browser.quit()
    