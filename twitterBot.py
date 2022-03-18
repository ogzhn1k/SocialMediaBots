from itertools import count
from re import search
from twitterInfos import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

class Twitter:
    def __init__(self,username,password):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        options.add_argument("--start-maximized")

        self.browser = webdriver.Chrome(options=options)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input")
        usernameInput.send_keys(self.username)
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(2)
        
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)

    def search(self,hashtag):
        searchInput = self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        results = []

        tweetList = self.browser.find_elements(By.XPATH,"//article[@data-testid='tweet']/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
        time.sleep(2)
        print("Count : "+str(len(tweetList)))

        for tweet in tweetList:
            results.append(tweet.text)

        scrollCounter = 0
        lastScrollHeight = self.browser.execute_script("return document.documentElement.scrollHeight")
        while(True):
            if scrollCounter > 3:
                break

            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_ScrollHeight = self.browser.execute_script("return document.documentElement.scrollHeight")
            if lastScrollHeight == new_ScrollHeight :
                break
            lastScrollHeight = new_ScrollHeight
            scrollCounter+=1

            tweetList = self.browser.find_elements(By.XPATH,"//article[@data-testid='tweet']/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
            time.sleep(2)
            print("Count : "+str(len(tweetList)))
            for tweet in tweetList:
                results.append(tweet.text)


        count = 1
        # for item in results:
        #     print(f"{count}-{item}")
        #     count+=1
        #     print("---------------------------------------------------------------------------")

        
        with open("TwitterBotTweets.txt","w",encoding="UTF-8") as file:
            for item in results:
                file.write(f"{count}- {item}\n")
                count+=1






twitter = Twitter(username,password)
twitter.signIn()
twitter.search("****")