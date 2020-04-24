import urllib.request
import json
import os


def getAudioURL(bookId,tempFileName):
    if(bookId==None or tempFileName == None):
        print("页码键值缺失",bookId,tempFileName)
    url="https://files-api1.51wanxue.com/brs/content/picturebook/"+str(bookId)+"/voice/"+str(tempFileName)
    return url


def fmtFileName(name):
    name=str(name)
    name=name.replace("?","").replace("!","")
    return name.strip()

# singleBookDir="单行书"

# fileurl="https://www.0dutv.com/upload/dance/20200419/5C0B03D1E3FD2BDBC8CF14C48A9FCE63.mp3"
# filename = fileurl.split('/')[-1]
# filepath = singleBookDir + '/' + filename
# urllib.request.urlretrieve("https://www.0dutv.com/upload/dance/20200419/5C0B03D1E3FD2BDBC8CF14C48A9FCE63.mp3",filepath)

seriesBooKDir="套系书"

jsonFile = open('jsonFile.txt','r',encoding='utf-8')
books=json.loads(jsonFile.read())

bookWithSounds=[]
for j in books:
    for  i in books[j]:
        bookFloder=seriesBooKDir+"/"+j+"/"+fmtFileName(i.get("bookName"))
        bookFloder=bookFloder.replace("?","").replace("!","")
        if(not os.path.exists(bookFloder)):
            os.makedirs(bookFloder)
        for k in i.get("sounds"):
            url=getAudioURL(i.get("bookId"),k.get("tempFileName"))
            fileName=str(bookFloder+'/' + str(k.get("pageNo"))+".mp3")
            urllib.request.urlretrieve(url,fileName)
            
