import json
import time

seriesBookMap={}
singleBookList=[]

def updateMap(book):
    global seriesBookMap
    global singleBookList
    
    arr=seriesBookMap.get(book.get("series"))
    if(arr!=None):
        seriesBookMap.get(book.get("series")).append(book)
    else:
        seriesBookMap[book["series"]]=[]
        seriesBookMap.get(book.get("series")).append(book)


updateMap({"bookName":"name1","bookId":123,"series":"s1"})
updateMap({"bookName":"name2","bookId":1231,"series":"s2"})
updateMap({"bookName":"name3","bookId":1232,"series":"s2"})
updateMap({"bookName":"name4","bookId":1233,"series":"s3"})

# print(json.dumps(seriesBookMap))

time.sleep(3)
print(1)
