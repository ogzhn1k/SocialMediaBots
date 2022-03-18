from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Whatsapp:
    def __init__(self):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--start-maximized")

        self.browser = webdriver.Chrome(options=options)

    def openWp(self):
        self.browser.get("https://web.whatsapp.com/")
        time.sleep(10)


    def searchPersonOrGroup(self,personOrGroup):
        searchInput = self.browser.find_element(By.XPATH,"//*[@id='side']/div[1]/div/label/div/div[2]")
        searchInput.send_keys(personOrGroup)
        time.sleep(2)

        # target = self.browser.find_elements(By.XPATH,"//div[@data-testid='cell-frame-container']/div[2]/div[1]/div[1]/span[1]/span[1]")
        targets = self.browser.find_elements(By.XPATH,"//div[@data-testid='cell-frame-container']/div[2]/div[1]")
 
        counter = 1
        for item in targets:
            if(counter==1):
                item.click()
            counter+=1

        time.sleep(2)



        

whatsapp = Whatsapp()
whatsapp.openWp()
whatsapp.searchPersonOrGroup("*****")