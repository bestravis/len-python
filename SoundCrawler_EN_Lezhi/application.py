from lxml import etree
import requests
import xlwt
import xlrd
import json
import requests
import cookie_file
import time

# === 准备数据 ===

# 读取xls
booksXls = xlrd.open_workbook('book_all.xls')
sheets=booksXls.sheets()
bookList = sheets[0]
bookListSize = bookList.nrows

seriesBookMap={}
singleBookList=[]
def updateMap(book):
    global seriesBookMap
    
    series=book.get("series")
    arr=seriesBookMap.get(series)
    if(arr!=None):
        seriesBookMap.get(series).append(book)
    else:
        seriesBookMap[series]=[]
        seriesBookMap.get(series).append(book)



# 将单元格数据保存到数组
pot={}
bookjsonDataArr=[]
for i in range(1,bookListSize):
    pot=bookList.row_values(i)
    temp={}
    temp["bookId"] = int(pot[2])
    temp["bookName"] = pot[1]
    temp["series"] = pot[0]

    updateMap(temp)



def exitByError(msg):
    print(msg)
    exit()


# 音频路径
# https://files-api1.51wanxue.com/brs/content/picturebook/
# 157606/voice/2f1af3e9-7ad0-40b8-a844-c8b547903cd3.mp3

# === 登陆函数 ===
# 1.先检查账号密码，成功后取出response的sid
# https://console.51wanxue.com/checkProtocolState.do
# post formdata 
# email=1&password=1
# 
# 2.调用登陆接口，在cookie中加入sid，使得sid生效，入参同上
# https://console.51wanxue.com/login.do


HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
cookiesDit={}
def login():
    global cookiesDit
    params="?email=product01@reading-pen.com&password=lzjy123456"
    url="https://console.51wanxue.com/checkProtocolState.do"+params
    url2="https://console.51wanxue.com/login.do"+params

    response = requests.get(url,headers=HEADERS)
    jsonData=json.loads(response.text)

    if(jsonData.get('code')==0):
        print("checkProtocolState success ...",jsonData)
        cookiesDit=response.cookies.get_dict()
    else:
        exitByError("checkProtocolState error ...")
        return
    
    response = requests.get(url2,headers=HEADERS,cookies=cookiesDit)
    jsonData=json.loads(response.text)

    if(jsonData.get('code')==0):
        print("login success ...",jsonData)
    else:
        exitByError("login error ...")
        return

    print(cookiesDit)


singleBookList=[]
seriesBookList=[]
def findPageData(bookId):
    # 获取书本所有页码数据
    url="https://console.51wanxue.com/cms/listPages.do?repoId=271&bookId="+str(bookId)
    response = requests.get(url,headers=HEADERS,cookies=cookiesDit)

    foo=json.loads(response.text)
    pageIds=[]
    if(foo.get("code")==0):
        pot=foo.get("data").get("pages")
        for i in pot:
            pageIds.append(i.get("id"))
    else:
        exitByError("请求页码数据错误")
    
    return pageIds

    # 获取页码数据
    # url="https://console.51wanxue.com/cms/loadPageInfo.do?repoId=271&pageId="+pageId
    # response = requests.get(url,headers=HEADERS,cookies=cookiesDit)

def findAudioData(pageIds):
    sounds=[]
    for pageId in pageIds:
        url="https://console.51wanxue.com/cms/loadPageInfo.do?repoId=271&pageId="+str(pageId)
        response = requests.get(url,headers=HEADERS,cookies=cookiesDit)

        foo=json.loads(response.text)
        
        if(foo.get("code")==0):
            voiceArr=foo.get("data").get("voice").get("voice")
            if(len(voiceArr)!=0):
                sounds.append({"pageNo":foo.get("data").get("physicalIndex"),"tempFileName":voiceArr[0].get("tempFileName")})
        else:
            print("请求页码数据错误")
    
    return sounds


# 遍历套系书
for o in seriesBookMap:
    print(seriesBookMap[o][0])

def main():
    global cookiesDit
    if(cookie_file.checkCookieUsable()==True):
        cookiesDit=cookie_file.readCookie()
    else:
        print("自动登陆...")
        login()
        cookie_file.writeCookieFile(cookiesDit)

    # pageIds=findPageData(155817)
    # sounds=findAudioData(pageIds)
    
    # print(json.dumps(sounds))
    print("=======")
    saveBookData(seriesBookMap)
    # print("json:",json.dumps(seriesBookMap,ensure_ascii=False))

    jsonFile = open('jsonFile.txt','w',encoding='utf-8')
    jsonFile.write(json.dumps(seriesBookMap,ensure_ascii=False))

def saveBookData(seriesMap):
    global seriesBookMap
    for j in seriesMap:
        pot=[]
        for i in seriesMap[j]:
            print(i.get("bookName"))
            pageIds=findPageData(i.get("bookId"))
            sounds=findAudioData(pageIds)
            i["sounds"]=sounds
            pot.append(i)
            # slepp 1s
            time.sleep(1)
        seriesBookMap[j]=pot          
        
#程序开始
main()