import requests

metadata_dir = ".debug/"
movescount_domain = "http://www.movescount.com"

def generateSessionCookie():
    moves_uname = input("Movescount email: ")
    moves_pwd = getpass("Movescount password: ")
    #TODO: RE cookie generation mechanism
    
def generateDebugSessionCookie():
    cookies = {'MovesCountCookie':'', 'ASP.NET_SessionId':'', 'AWSELB':''}
    cookies['MovesCountCookie'] = open(metadata_dir+"movescount_movecountcookie").read()
    cookies['ASP.NET_SessionId'] = open(metadata_dir+"movescount_sessionid").read()
    cookies['AWSELB'] = open(metadata_dir+"movescount_awselb").read()
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
