#!/usr/bin/env python
from  scarpkg import logStart, logStop, logMsg, Log, get_info, Bot

#logStart('/Users/Scar/log',True)

#logMsg("test message")

#logStop()

log = Log(verbose=True)
log.msg("okey")
log.stop()


INFO = get_info("/Users/Scar/.variables.yaml")
print INFO

my_bot=Bot(INFO['telegram']['token'],INFO['telegram']['id'],INFO['telegram']['user'])

my_bot.msg("Hola mundo")
#my_bot.photo("/Users/Scar/garfield.jpg")
my_bot.audio("/Users/Scar/Fate_of_the_unknown.mp3")
#log.start()
