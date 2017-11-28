#!/usr/bin/env python
from  scarpkg import logStart, logStop, logMsg, Log

#logStart('/Users/Scar/log',True)

#logMsg("test message")

#logStop()

log = Log(verbose=True)
log.msg("okey")
log.stop()
#log.start()
