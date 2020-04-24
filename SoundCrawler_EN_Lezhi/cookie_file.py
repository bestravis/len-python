import os
import json
import time


def initFloder():
    jsonData={'_SID_': 'N2I5ZTVlMDQtOTFmYS00NTIxLTkxZWYtNmUwNzZjY2EyNGE4'}
    bo=os.path.exists('cookie.txt')
    cookie = open('cookie.txt','w',encoding='utf-8')
    if(bo):
        cookie.write(str(jsonData))

    else:
        cookie = open('cookie.txt','w',encoding='utf-8')


def writeCookieFile(cookieData):
    cookie = open('cookie.txt','w',encoding='utf-8')
    cookie.write(str(cookieData).replace("\'","\"")+"\n")
    cookie.write(str({"time":time.time()}).replace("\'","\"")+"\n")
    cookie.close()

def checkCookieUsable():
    cookie = open('cookie.txt','r',encoding='utf-8')
    fileTime=json.loads(cookie.readlines()[1]).get("time")
    freeTime=time.time()-fileTime
    print("cookies生效：",freeTime<(60*4),freeTime)
    return freeTime<(60*4)

def readCookie():
    cookie = open('cookie.txt','r',encoding='utf-8')
    line=json.loads(cookie.readlines()[0])
    print("cookie：",line)
    return line

# writeCookieFile({'_SID_': 'N2I5ZTVlMDQtOTFmYS00NTIxLTkxZWYtNmUwNzZjY2EyNGE4'})
# checkCookieUsable()
# readCookie()