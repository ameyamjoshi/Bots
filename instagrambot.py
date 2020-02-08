from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
class instabot:
    def __init__(self,email,pw):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.instagram.com")
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/button').click()
        sleep(4)
        login_field=self.driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(email)
        login_field=self.driver.find_element_by_xpath("//input[@name=\"pass\"]").send_keys(pw)
        login_field=self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div/span[2]").click()
        self.driver.get("https://www.instagram.com/virag___umathe/")
        sleep(5)
        self.driver.get("https://www.instagram.com/virag___umathe/tagged/")
        sleep(500)
        
instabot('Email','password')
