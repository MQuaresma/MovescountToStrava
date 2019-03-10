#!/usr/bin/env python3

import requests
import sys, getopt
from getpass import getpass

movescount_domain = "http://www.movescount.com"

def generateSessionCookie():
    moves_uname = input("Movescount email: ")
    moves_pwd = getpass("Movescount password: ")
    #TODO: RE cookie generation mechanism
    
def generateDebugSessionCookie():
    cookie_dir = "cookies/"
    cookies = {'MovesCountCookie':'', 'ASP.NET_SessionId':'', 'AWSELB':''}
    cookies['MovesCountCookie'] = open(cookie_dir+"movescount_movecountcookie").read()
    cookies['ASP.NET_SessionId'] = open(cookie_dir+"movescount_sessionid").read()
    cookies['AWSELB'] = open(cookie_dir+"movescount_awselb").read()
    return cookies

def getSession(cookies):
    session = requests.get(movescount_domain + '/latestmove', cookies=cookies)

    if(session.status_code == 200):
        print("Authencation successful \nFetching moves...")
        return True
    else:
        print("Authencation Failed")
        return False

def getMoveIDs():
    # TODO: crawl for Moves
    move_ids = ['273536684']
    return move_ids

def exportMove(cookies, move_id, exp_format = "gpx"):
    payload = {'id': move_id, 'format': exp_format}
    exp_move = requests.get(movescount_domain + "/move/export" , params=payload, cookies=cookies)
    if(exp_move.status_code == 200):
        move_dump = open(move_id + "." + exp_format, "wb")
        move_dump.write(exp_move.content)
        move_dump.close()

def main():
    args, _ = getopt.getopt(sys.argv[1:], "d")
    args = dict(args) 
    if "-d" in args:
        print("Creating debug session..")
        session_cookie = generateDebugSessionCookie()
    else:
        session_cookie = generateSessionCookie()
    
    if getSession(session_cookie):
        moves = getMoveIDs()
        if len(moves) > 0:
            for move_id in moves:
                exportMove(session_cookie, move_id)
            print("All moves exported")
        else:
            print("No moves to export")
    else:
        print("Exiting...")
    

if __name__ == "__main__":
    main()
