from selenium import webdriver
from selenium.webdirver.common.keys import Keys

class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
    def closedBrowser(self):
        self.driver.close()

    def login(self):
        drive = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)



myuseri = InstagramBot("user","pass")
myuseri.login()

