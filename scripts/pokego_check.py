#!/usr/bin/env python
import sys
from pprint import pprint, pformat
from  scarpkg import logStart, logStop, logMsg, Log, get_info, Bot, save_info
#import getopt
import __main__
import os
import argparse
import requests
from bs4 import BeautifulSoup

poke_file = os.environ['HOME']+"/.poke.yaml"
verbose=False

def get_my_args():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--verbose", help="Set verbose to True",action="store_true")
    parser.add_argument("-l","--log", help="Set logpath, default=/tmp",default="/tmp")
    parser.add_argument("-I","--variables", help="File with variables info default {0}/.variales.yaml".format(os.environ['HOME']),default=os.environ['HOME']+"/.variables.yaml") 
    args = parser.parse_args()
    
    return args

def get_poke_info(poke_url):
    try:
        poke = requests.get(poke_url)
    except :
        log("Problem while retriving pokemon info")
        my_bot.msg("Problem while retriving pokemon info")
        logStop(1)
        sys.exit(1)

    if poke.status_code == 200:
        log("Poke info retrieved successfully")
    else:
        log("Can't retrieve poke info")
        log("status code : {0}".format(poke.status_code))
        logStop(1)
        sys.exit(1)
    
    poke_soup =  BeautifulSoup(poke.content,features="html.parser")
    mydivs = poke_soup.find_all("div", class_="elementor-clearfix")
    for a in mydivs:
        if "Version" in a.get_text():
            poke_info = a.get_text()
            poke_info = poke_info.replace("[Change Log]","")
            poke_info = poke_info.replace("Tutorials & Tips","")    
    
    dummy, poke_version, poke_sub_version, dummy2, month, day, year = poke_info.split()
    poke_sub_version = poke_sub_version.replace("(","")
    poke_sub_version = poke_sub_version.replace(")","")
    poke_sub_version = str(poke_sub_version)
    poke_version = str(poke_version)
    log("Poke Version from page : {0}".format(poke_version))
    log("Poke Subversion from page : {0}".format(poke_sub_version))
    log("Date from page {0}/{1}/{2}".format(day.replace(",",""),month,year))
    return poke_version, poke_sub_version
        
def poke_check(POKE_INFO):
    poke_url = "https://www.ispoofer.com/ispoofer4pokemongo/"
    if not POKE_INFO:
        log("Gatering fresh info from poke page")
        poke_version, poke_subversion = get_poke_info(poke_url)
        POKE_INFO = {}
        POKE_INFO['version'] = poke_version
        POKE_INFO['subversion'] = poke_subversion
        save_info(poke_file,POKE_INFO)
        my_bot.msg("First time executing Poke-check \nVersion : {0}\nSubversion : {1}".format(poke_version,poke_subversion))
        logStop(0)
        sys.exit()

    poke_version, poke_subversion = get_poke_info(poke_url)

    if POKE_INFO['version'] != poke_version:
        my_bot.msg("New major Version of pokemon \nVersion on file : {0}\nVersion on Page : {1}".format(POKE_INFO['version'],poke_version))
    elif POKE_INFO['subversion'] != poke_subversion:
        my_bot.msg("New sub-version of pokemon \nSub-version on file : {0}\nSub-version on Page : {1}".format(POKE_INFO['subversion'],poke_subversion))
    else :
        log("No changes detected on version of Pokemon")

    # Save info
    POKE_INFO['version'] = poke_version
    POKE_INFO['subversion'] = poke_subversion
    save_info(poke_file,POKE_INFO)
    logStop(0)
    sys.exit()
        
    
if __name__ == "__main__":
    args = get_my_args()
    verbose=False
    log=logMsg
    if args.verbose:
        #global verbose
        verbose = True
    logStart(args.log,args.verbose)
    INFO = get_info(args.variables)
    
    telegram_bot_id=INFO['ScarBot']['id']
    telegram_bot_token=INFO['ScarBot']['token']
    my_user=INFO['ScarBot']['user']
    if os.path.isfile(poke_file):
        POKE_INFO = get_info(poke_file)
        log("Poke info from file "+pformat(POKE_INFO))
    else:
        POKE_INFO = ""
        log("Poke info file not found")
    #api = create_api()
    #order = api.lookup_order(ORDER['order']['id'])
    #order = order[0]
    #logMsg(pformat(order))
    my_bot=Bot(telegram_bot_token,telegram_bot_id,my_user)
    poke_check(POKE_INFO)
    
    
