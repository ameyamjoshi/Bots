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
       # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        self.driver.find_element_by_class_name("aOOlW   HoLwm ")
        sleep(4)
        #self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div/span[2]").click()
        #self.driver.get("https://www.instagram.com/_manali_195/")
        #sleep(5)
        #self.driver.get("https://www.instagram.com/_manali_195/tagged/")
        #sleep(500)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[1]/div/div/div/div[1]/button/span/img')
        sleep(5)
instabot(email id,password)
