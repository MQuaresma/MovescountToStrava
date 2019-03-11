#!/usr/bin/env python3

import sys, getopt
from getpass import getpass
import movescount
import strava

def main():
    args, _ = getopt.getopt(sys.argv[1:], "d")
    args = dict(args) 

    if "-d" in args:
        print("Creating debug session..")
        session_cookie = movescount.generateDebugSessionCookie()
    else:
        session_cookie = movescount.generateSessionCookie()
    
    if movescount.getSession(session_cookie):
        moves = movescount.getMoveIDs()
        if len(moves) > 0:
            for move_id in moves:
                movescount.exportMove(session_cookie, move_id)
            print("All moves exported")
        else:
            print("No moves to export")
    else:
        print("Exiting...")
    

if __name__ == "__main__":
    main()
