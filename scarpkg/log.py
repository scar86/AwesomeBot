import logging
import os
import __main__
from logging.handlers import RotatingFileHandler

my_pid = os.getpid() # my PID
    
            
def logStart(logpath='/tmp',verbose=False):
    """
    Start logging 
    logStart(logpath='/path/to/log',verbose=False)
    Start a log with the caller name under logpath
    Example : /home/user/log/script.log
    """
    #Overview of steps to create the loggers
    # 1 - Create a python logger
    # 2 - Set the logger level
    # 3 - Create a python handler
    # 4 - Set the handler level
    # 5 - Create a formatter
    # 6 - Add formatter to  the handler
    # 7 - Add handler to  thelogger
    # 8 - Log a messages
    try:
        my_name = os.path.basename(__main__.__file__) # get the caller name
    except:
        my_name = 'live_script'
        
    my_path = logpath # get the path to where to log 
    my_logfile = "{0}/{1}.log".format(my_path,my_name) #path + script name
    
    logger = logging.getLogger(my_name) # Step 1
    
    logger.setLevel(logging.DEBUG) # Step 2   
    
    filehandler = RotatingFileHandler(my_logfile, maxBytes=5242880, backupCount=10) # Step 3 - 10 logs, 5M each 
    
    filehandler.setLevel(logging.DEBUG) # Step 4
    
    formatter = logging.Formatter('%(asctime)s - %(message)s',  datefmt='%d/%m/%Y %H:%M:%S') # Step 5 - create a format, 10/27/2017 12:05:17 - test.py - DEBUG - test log

    filehandler.setFormatter(formatter) # Step 6
    
    logger.addHandler(filehandler) # Step 7
    
    
    if verbose : # Add a console handler to logger
        ch = logging.StreamHandler() # Step 3
        ch.setLevel(logging.DEBUG) # Step 4
        verbformatter = logging.Formatter('%(asctime)s - %(message)s',  datefmt='%d/%m/%Y %H:%M:%S')
        ch.setFormatter(verbformatter) # step 6
        logger.addHandler(ch) # Step 7

    logMsg("# Start execution of {0} PID {1} #".format(my_name,my_pid))
    
def logStop(rc=0):
    """
    Stop logging
    logStop(rc)
    Print footer to log with the return code as well (0 if not specified)
    """
    
    my_name = __main__.__file__ # get caller file name
    #my_path = logpath # get the path of the main script
    
    logMsg("# Finish execution of {0} PID {1} RC={2} #".format(my_name,my_pid,rc))
    # Add l
def logMsg(msg='',screen=False):
    """
    logMsg
    logMsg(msg='message')
    Log a message to like:
    2/11/2017 19:01:29 - 7296 - Message_to_log
    If verbose is enable, output will be print to screen too
    
    """
    
    try:
        my_name = os.path.basename(__main__.__file__) # get the caller name
    except:
        my_name = 'live_script'
    #my_path = logpath # get the path of the main script
    
    logger = logging.getLogger(my_name) # get logger with script name
    #logger = logging.LoggerAdapter(logger, extra_logging)
    logger.debug(str(msg)) # log message, if verbose is enabled it will print to screen too

        
class Log(object):
    def __init__(self,path="/tmp",verbose=False):
        self.path = path
        self.verbose = verbose
        self.name = os.path.basename(__main__.__file__)
        self.logfile = "{0}/{1}.log".format(self.path,self.name)
        self.pid = os.getpid()
        self.start()
    
    def start(self):
        """
        Start logging 
        logStart(logpath='/path/to/log',verbose=False)
        Start a log with the caller name under logpath
        Example : /home/user/log/script.log
        """
        #Overview of steps to create the loggers
        # 1 - Create a python logger
        # 2 - Set the logger level
        # 3 - Create a python handler
        # 4 - Set the handler level
        # 5 - Create a formatter
        # 6 - Add formatter to  the handler
        # 7 - Add handler to  thelogger
        # 8 - Log a messages
        
    
         # get the caller name
        #selpath = logpath # get the path to where to log 
         #path + script name
        
        self.logger = logging.getLogger(self.name) # Step 1
        
        self.logger.setLevel(logging.DEBUG) # Step 2   
        
        self.filehandler = RotatingFileHandler(self.logfile, maxBytes=5242880, backupCount=10) # Step 3 - 10 logs, 5M each 
        
        self.filehandler.setLevel(logging.DEBUG) # Step 4
        
        self.formatter = logging.Formatter('%(asctime)s - %(message)s',  datefmt='%d/%m/%Y %H:%M:%S') # Step 5 - create a format, 10/27/2017 12:05:17 - test.py - DEBUG - test log
    
        self.filehandler.setFormatter(self.formatter) # Step 6
        
        self.logger.addHandler(self.filehandler) # Step 7
        
        
        if self.verbose : # Add a console handler to logger
            self.ch = logging.StreamHandler() # Step 3
            self.ch.setLevel(logging.DEBUG) # Step 4
            self.verbformatter = logging.Formatter('%(asctime)s - %(message)s',  datefmt='%d/%m/%Y %H:%M:%S')
            self.ch.setFormatter(self.verbformatter) # step 6
            self.logger.addHandler(self.ch) # Step 7
            
        #self.a = "hola"
        #self.msg(self.a)
        self.msg("# Start execution of {0} PID {1} #".format(self.name,self.pid))
        #self.msg("start test dfdfd")
        #print "Start logging pid : {0}".format(self.pid)
        #print "name : {0}".format(self.name)
        
    def stop(self,rc=0):
        """
        Stop logging
        logStop(rc)
        Print footer to log with the return code as well (0 if not specified)
        """
        self.rc = rc
        #my_name = __main__.__file__ # get caller file name
        #my_path = logpath # get the path of the main script
        
        self.msg("# Finish execution of {0} PID {1} RC={2} #".format(self.name,self.pid,self.rc))
        #print "Stop logging"
        
    def msg(self,txt):
        """
        logMsg
        logMsg(msg='message')
        Log a message to like:
        2/11/2017 19:01:29 - 7296 - Message_to_log
        If verbose is enable, output will be print to screen too
        
        """
        self.txt = txt
        #self.msg = msg
        #my_name = __main__.__file__ # get caller file name
        #my_path = logpath # get the path of the main script
        
        #self.logger = logging.getLogger(my_name) # get logger with script name
        #logger = logging.LoggerAdapter(logger, extra_logging)
        self.logger.debug(str(self.txt)) # log message, if verbose is enabled it will print to screen too
        
        #print  self.txt
