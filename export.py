#!/usr/bin/env python3

import requests
from getpass import getpass


def getSession():
    movescount_domain = "http://www.movescount.com"
    cookie_dir = "cookies/"
    cookies = {'MovesCountCookie':'', 'ASP.NET_SessionId':'', 'AWSELB':''}
    cookies['MovesCountCookie'] = open(cookie_dir+"movescount_movecountcookie").read()
    cookies['ASP.NET_SessionId'] = open(cookie_dir+"movescount_sessionid").read()
    cookies['AWSELB'] = open(cookie_dir+"movescount_awselb").read()

    l_move = requests.get(movescount_domain + '/latestmove', cookies=cookies)

    if(l_move.status_code == 200):
        print("200")
    else:
        print("302")

def getMoveIDs():
    move_ids = ['273536684']
    # TODO: crawl for Moves
    return move_ids

def exportMove(move_id):
    


def main():
    #moves_uname = input("Movescount email: ")
    #moves_pwd = getpass("Movescount password: ")
    getSession()
    

if __name__ == "__main__":
    main()
