from selenium import webdriver
from time import sleep

from secret import username, password

class October():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def getDriver(self):
        return self.driver

    def login(self):
        self.driver.get('https://fr.october.eu/')
        login_page_btn = self.driver.find_element_by_xpath('//*[@id="button-log-in"]')
        login_page_btn.click()
        sleep(3)
        
        username_input = self.driver.find_element_by_xpath('//*[@name="email"]')
        username_input.send_keys(username)

        password_input = self.driver.find_element_by_xpath('//*[@name="password"]')
        password_input.send_keys(password)
        
        login_btn = self.driver.find_element_by_xpath('//*[@class="actions"]/button')
        login_btn.click()


app = October()
app.login()