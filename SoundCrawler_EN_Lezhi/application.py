from lxml import etree
import requests
import xlwt
import xlrd
import json

# === 准备数据 ===

# 读取xls
booksXls = xlrd.open_workbook('books.xls')
sheets=booksXls.sheets()
bookList = sheets[0]
bookListSize = bookList.nrows

# 将单元格数据保存到数组
pot={}
temp={}
bookJsonArr=[]
for i in range(1,bookListSize):
    pot=bookList.row_values(i)
    temp["bookId"] = int(pot[0])
    temp["bookName"] = pot[1]
    temp["series"] = pot[2]

    bookJsonArr.append(temp)

print(bookJsonArr[0]["bookId"])


# === 登陆函数 ===
# 1.先检查账号密码，成功后取出response的sid
# https://console.51wanxue.com/checkProtocolState.do
# post formdata 
# email=1&password=1
# 
# 2.调用登陆接口，在cookie中加入sid，使得sid生效，入参同上
# https://console.51wanxue.com/login.do

