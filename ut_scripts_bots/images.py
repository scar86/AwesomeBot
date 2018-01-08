#!/usr/bin/python


import sys
import time
import telepot
import urllib
import ipgetter

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if chat_id == 12345 or chat_id == 12345 or chat_id == 12345 : # replce with the permited ids
        if content_type == 'text' and msg['text'] == 'Ping' :
            bot.sendMessage(chat_id, 'Capurando imagenes' )
            urllib.urlretrieve('http://172.31.10.61/cgi-bin/nph-mjgrab?1', '/tmp/test.jpeg')
            #image = response.read()
            #bot.sendPhoto(4067854, photo=open('test.jpg', 'rb'))
            bot.sendPhoto(chat_id, photo=open('/tmp/test.jpeg', 'rb') )
            urllib.urlretrieve('http://172.31.10.61/cgi-bin/nph-mjgrab2?1', '/tmp/test2.jpeg')
            bot.sendPhoto(chat_id, photo=open('/tmp/test2.jpeg', 'rb') )
	elif content_type == 'text' and msg['text'] == 'IP' :
		myip = ipgetter.myip()
	        if myip:
			bot.sendMessage(chat_id, myip )	
		else:
			bot.sendMessage(chat_id, 'Unable to get ip' )
        else:
            bot.sendMessage(chat_id, msg['text'])
    elif content_type == 'text':
           bot.sendMessage(chat_id, msg['text']) 

#TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot('API_KEY')
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
