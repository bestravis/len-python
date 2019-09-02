from lxml import etree
from string import Template
import requests
import xlwt
import xlrd
import re

#本脚本根据导入的列表去各大电商网 搜搜对应的英文书籍

#修改url中的参数
jd_url='''
    https://search.jd.com/Search?keyword={0}&enc=utf-8&wq={1}
'''

dd_url='''
    http://search.dangdang.com/?key={0}&act=input
'''

tm_url='''
    https://list.tmall.com/search_product.htm?q={0}
'''

jd_div='''
    <a target="_blank" title="开学总动员！自营图书每满100减50！更多好书快快抢购！点击直达会场" 
        href="//item.jd.com/10880192.html" onclick="searchlog(1,10880192,0,2,'','flagsClk=1077940872')">
        <img width="200" height="200" class="" data-img="1" source-data-lazy-img="" data-lazy-img="done" 
            src="//img12.360buyimg.com/n1/s200x200_19732/0fabff7e-d5ab-461e-b480-dca2431ce4a9.jpg">
    </a>
'''

workbook = xlrd.open_workbook(r'book.xls')

sheet1 = workbook.sheet_by_index(0)#通过索引获取表格
cols = sheet1.col_values(0)#获取列内容
cols.remove('书本名称')
print(cols)


HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}


def fmtJD():
    # print("链接:",jd_url)
    response = requests.get(jd_url,headers=HEADERS)
    text = response.content.decode('utf-8')
    html = etree.HTML(text)
    title=html.xpath('//div[@class="p-name"]//a')

    books=[]
    for i in title:
        arr=i.attrib
        tmp={}
        
        if(arr.get('target')!=None and arr.get('title')!=None):
            if(arr.get('title') == ''  or arr.get('title')[0].isalpha() == False):
                continue
            tmp["url"]="https:"+arr.get('href')
            tmp["title"]=fmtTitle(arr.get('title'))
            books.append(tmp)
            continue
    # print(books)
    return books
        
def fmtTitle(str):
    tmp=re.sub(u"([\u4e00-\u9fa5])","",str).strip()
    return tmp




bookList=[]
errorList=[]
for b in cols:
    # print(b)
    orginName=b
    b=b+" 英文"
    jd_url='https://search.jd.com/Search?keyword={0}&enc=utf-8&wq={1}'.format(b,b)
    books=fmtJD()
    # time.sleep(1)
    if(len(books)>0):
        tmp=books.pop()
        tmp["chsTitle"]=orginName
        bookList.append(tmp)
        continue
    else:
        errorList.append(orginName)
# print(bookList)
print("未找到：",errorList)


bookResult = xlwt.Workbook('utf-8')
sheet = bookResult.add_sheet('result')
head=['英文书名','京东','中文书名']

for h in range(len(head)):
    sheet.write(0, h, head[h])  # 写入表头
sheet.col(0).width = 9000
sheet.col(1).width = 9000
sheet.col(2).width = 9000

y = 0
x = 1
for o in bookList:
    sheet.write(x, y, o['title'])
    sheet.write(x, y+1, o['url'])
    sheet.write(x, y+2, o['chsTitle'])
    x=x+1
bookResult.save('bookResult.xls')

print('done')
