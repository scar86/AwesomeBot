#!/usr/bin/env python

import os
import time
import telepot
import tempfile
from gtts import gTTS
from datetime import datetime
import yaml


#This script is meant to be used with the runOnReceive parameter of gammu sms daemon

#Get variables from file on home/.Awbot.yml

with open("{0}/{1}".format(os.environ.get("HOME"),".AwBot.yml"), "r") as stream:
    INFO = yaml.load(stream)

BOT_TOKEN = INFO["telegram"]["token"] # TEST_BOT env variable should contain the bot id
USER_ID = INFO["telegram"]["id"] #TEST_ID env variable should contain the user_id
USER = INFO["telegram"]["user"]
PID = os.getpid() # get PID, currently not used
try:
    SMS_NUMBER = os.environ.get("SMS_1_NUMBER")
except:
    bot = telepot.Bot(BOT_TOKEN) #Create bot
    bot.sendMessage(USER_ID, "Invocation, but no number on system variables") # send the same text that arrived on the sms
    sys.exit(0)
    
t = datetime.now() #get the time

time_format = "{0}{1}{2}_{3}{4}".format(t.year,t.month,t.day,t.hour,t.minute)

try:
    numparts = int(os.environ['DECODED_PARTS']) # How many parts we got
except:
    numparts = 0
text = ''
# Are there any decoded parts?
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
