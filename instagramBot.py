from  instagramInfos import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Instagram:
    def __init__(self,username,password):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.browser = webdriver.Chrome(options=options)
        self.username = username
        self.password = password

    def signIn(self):
       
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):
        time.sleep(2)
        self.browser.get(f"https://www.instagram.com/{username}")

        followersUrl = self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div") 
        followersUrl.click()
        time.sleep(2)


    def passSavePopUp(self):
        time.sleep(2)
        self.browser.find_element(By.XPATH,"//button[contains(text(),'Şimdi Değil')]").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH,"//button[contains(text(),'Şimdi Değil')]").click()

    


instagram = Instagram(username,password)
instagram.signIn()
instagram.passSavePopUp()
instagram.getFollowers()


