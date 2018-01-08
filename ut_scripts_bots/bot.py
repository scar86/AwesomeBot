#!/usr/bin/python
import sys
import time
import telepot
from pprint import pprint

def handle(msg):
    pprint(msg)

bot = telepot.Bot ('API_KEY')
#quien soy
print bot.getMe()

#response = bot.getUpdates()
#pprint(response)

#bot.sendPhoto(id_user, photo=open('/home/scar/camera/lastsnap.jpg', 'rb'))
bot.sendPhoto(id_user, photo='http://172.31.10.141/cgi-bin/nph-mjgrab?1')
#print bot.message_loop(handle)
# mi id id_user


#mantener programa corriendo
#while 1:
#    time.sleep(10)
