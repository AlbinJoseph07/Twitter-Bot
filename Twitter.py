from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot = webdriver.Chrome()
    
    def Login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email=bot.find_elements_by_class_name('email-input')
        password=bot.find_elements_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
    
    def like_tweet(self, hashtag):
        bot=self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets=bot.find_elements_by_class_name('tweet')
            links=[elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + tweet)
                try:
                    bot.find_elements_by_class_name('HeartAnimation').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(50)

er = TwitterBot('', '')
er.Login()
er.like_tweet('Xerox')