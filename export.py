#!/usr/bin/env python3

import requests
from getpass import getpass

movescount_domain = "http://www.movescount.com"

def getSession():
    cookie_dir = "cookies/"
    cookies = {'MovesCountCookie':'', 'ASP.NET_SessionId':'', 'AWSELB':''}
    cookies['MovesCountCookie'] = open(cookie_dir+"movescount_movecountcookie").read()
    cookies['ASP.NET_SessionId'] = open(cookie_dir+"movescount_sessionid").read()
    cookies['AWSELB'] = open(cookie_dir+"movescount_awselb").read()
    session = requests.get(movescount_domain + '/latestmove', cookies=cookies)

    if(session.status_code == 200):
        print("Authencation successful \nFetching moves...")
        return cookies
    else:
        print("Authencation Failed")
        return None

def getMoveIDs():
    # TODO: crawl for Moves
    move_ids = ['273536684']
    return move_ids

def exportMove(cookies, move_id, exp_format = "gpx"):
    payload = {'id': move_id, 'format': exp_format}
    exp_move = requests.get(movescount_domain + "/move/export" , params=payload, cookies=cookies)
    print(exp_move.status_code)

def main():
    #moves_uname = input("Movescount email: ")
    #moves_pwd = getpass("Movescount password: ")
    session_cookie = getSession()
    if session_cookie:
        moves = getMoveIDs()
        if len(moves) > 0:
            for move_id in moves:
                exportMove(session_cookie, move_id)
            print("All moves exported")
        else:
            print("No moves to export")
    

if __name__ == "__main__":
    main()
