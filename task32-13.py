from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestLinks(unittest.TestCase):
    def test_link1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//*[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//*[@placeholder='Input your email']")
        input3.send_keys("fsddf@fs.fs")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Хрень произошла")
    
    def test_link2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        input1 = browser.find_element(By.CLASS_NAME, "form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//*[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//*[@placeholder='Input your email']")
        input3.send_keys("fsddf@fs.fs")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Хрень произошла")
 

if __name__ == "__main__":
    unittest.main()