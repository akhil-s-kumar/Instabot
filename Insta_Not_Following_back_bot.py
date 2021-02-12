from instabot import Bot
from time import sleep
from random import randint
import authentication

bot = Bot()

bot.login(username = authentication.USERNAME, password = authentication.PASSWORD)

following = (bot.following)
followers = (bot.followers)

for i in following:
    if i in followers:
       continue
    else:
        print((bot.get_user_info(i))['username'])
        # If you want to unfollow them too, uncomment the bellow two lines as well.
        #bot.unfollow(i)
        #sleep(randint(6,12))
