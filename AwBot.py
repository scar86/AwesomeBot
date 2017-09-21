#!/usr/bin/env python

import os
import time
import telepot
import tempfile
from gtts import gTTS
from datetime import datetime
import yaml
import sys

class Log(object):
    
    def __init__(self,location):
        self.logfile = open(location, "a", 0)
        #self.write(" ")
        self.write("Start execution")
        self.write("My PID: {0}".format(os.getpid()))
    
    def write(self,text):
        self.t = datetime.now() #get the time
        self.time_format = "{0}{1}{2} {3}:{4}:{5}".format(self.t.year,self.t.month,self.t.day,self.t.hour,self.t.minute,self.t.second)
        self.logfile.write(self.time_format+": "+str(text)+" \n")
        
    def close(self):
        self.write("Closing log")
        self.logfile.close()
    

#This script is meant to be used with the runOnReceive parameter of gammu sms daemon

#Get variables from file on home/.Awbot.yml
reload(sys)  
sys.setdefaultencoding('utf8')

HOME_PATH="/home/scar" #Change this to your home, since this script will be run from cron env

with open("{0}/{1}".format(HOME_PATH,".AwBot.yml"), "r") as stream:
    INFO = yaml.load(stream)

#intialize log
log = Log("{0}/{1}".format(HOME_PATH,"AwBot.log"))

log.write(os.environ)

BOT_TOKEN = INFO["telegram"]["token"] # TEST_BOT env variable should contain the bot id
USER_ID = INFO["telegram"]["id"] #TEST_ID env variable should contain the user_id
USER = INFO["telegram"]["user"]

log.write("Token : {0}".format(BOT_TOKEN))
log.write("USER ID : {0}".format(USER_ID))
log.write("USER : {0}".format(USER))



if "SMS_1_NUMBER" not in os.environ :
    log.write("No SMS number in variables")
    bot = telepot.Bot(BOT_TOKEN) #Create bot
    bot.sendMessage(USER_ID, "Invocation, but missing variables") # send the same text that arrived on the sms
    sys.exit(0)
else:
    SMS_NUMBER = os.environ.get("SMS_1_NUMBER")
    log.write("SMS number : {0}".format(SMS_NUMBER))

try:
    numparts = int(os.environ['DECODED_PARTS']) # How many parts we got
except:
    numparts = 0
text = ''
# Are there any decoded parts?
#do we actually have text ?

if numparts == 0:
    text = os.environ['SMS_1_TEXT']
# Get all text parts
else:
    for i in range(0, numparts):
        varname = 'DECODED_%d_TEXT' % i
        if varname in os.environ:
            text = text + os.environ[varname]

# Do something with the text
full_text="Number {0} have sent text: {1}".format(SMS_NUMBER,text)
log.write(full_text)

bot = telepot.Bot(BOT_TOKEN) #Create bot
bot.sendMessage(USER_ID, full_text) # send the same text that arrived on the sms

# generate the mp3 message on the fly
tts = gTTS(text=text, lang="es",slow=False)
audio_tmp = tempfile.TemporaryFile() #generate a tmp file
tts.write_to_fp(audio_tmp) # write the audio to the tmp file, use tts.save("disk_file.mp3") to save it to disk
audio_tmp.seek(0) #need to seek to the beggining of the file to work

audio_name="audio_{0}.mp3".format(time_format)
bot.sendAudio(USER_ID, (audio_name,audio_tmp)) # send the file
audio_tmp.close() #Close the tmp file
