import os
import time
try:
	import telepot
except:
	import telegram as telepot
import tempfile
from datetime import datetime
import yaml
import sys



class Bot(object):
    def __init__(self,bot_key,user_id,user_name):
        self.bot_key = bot_key
        self.user_id = user_id
        self.user_name = user_name
        self.bot = telepot.Bot(bot_key)
        
    def msg(self,txt,usr_id=''):
        if not usr_id:
            self.usr_id = self.user_id
        else:
            self.usr_id = usr_id
        self.bot.sendMessage(self.usr_id, txt)
    
    def photo(self,photo,usr_id=''):
        if not usr_id:
            self.usr_id = self.user_id
        else:
            self.usr_id = usr_id
        
        if type(photo) is str:
            
            self.bot.sendPhoto(self.usr_id, photo=open(photo, 'rb') )
        elif type(photo) is file:
            t = datetime.now() #get the time
            time_format = "{0}{1}{2}_{3}{4}{5}".format(t.year,t.month,t.day,t.hour,t.minute,t.second)
            
            self.bot.sendPhoto(self.usr_id, ("photo_{0}.jpg".format(time_format), photo))
    
    def audio(self,audio,usr_id=''):
        if not usr_id:
            self.usr_id = self.user_id
        else:
            self.usr_id = usr_id
            
        if type(audio) is str:
            
            self.bot.sendAudio(self.usr_id, audio=open(audio, 'rb') )
        elif type(audio) is file:
            t = datetime.now() #get the time
            time_format = "{0}{1}{2}_{3}{4}{5}".format(t.year,t.month,t.day,t.hour,t.minute,t.second)
            
            self.bot.sendAudio(self.usr_id, ("audio_{0}.mp3".format(time_format), audio))
            
    def video(self,video,usr_id=''):
        if not usr_id:
            self.usr_id = self.user_id
        else:
            self.usr_id = usr_id
            
        if type(video) is str:
            
            self.bot.sendVideo(self.usr_id, video=open(video, 'rb') )
        elif type(video) is file:
            t = datetime.now() #get the time
            time_format = "{0}{1}{2}_{3}{4}{5}".format(t.year,t.month,t.day,t.hour,t.minute,t.second)
            
            self.bot.sendAudio(self.usr_id, ("video_{0}.mp4".format(time_format), video))

#bot = telepot.Bot(BOT_TOKEN) #Create bot
#bot.sendMessage(USER_ID, full_text) # send the same text that arrived on the sms
