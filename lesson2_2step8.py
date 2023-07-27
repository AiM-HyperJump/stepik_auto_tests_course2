import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    my_link = "http://suninjuly.github.io/file_input.html"
    browser.get(my_link)
    browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']").send_keys("BIG")
    browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']").send_keys("WELD")
    browser.find_element(By.CSS_SELECTOR, "[name = 'email']").send_keys("mister@bigweld.pyos")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'fileFOR228.txt')
    print("file_path: ", file_path)
    browser.find_element(By.CSS_SELECTOR, "[type = 'file']").send_keys(file_path)
    
    #browser.find_element(By.ID, "file").send_keys(os.path.join(os.path.dirname(__file__), 'fileFOR228'))
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    time.sleep(3)


finally:
    time.sleep(5)
    browser.quit()
    