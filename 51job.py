from lxml import etree
import requests
import xlwt

#本脚本还没写成循环抓取数据，目前只抓取第一页。实现这个功能需要更改url参数（2.html，3.html.....）
#xpath的api资料不好找，目前是直接抓取所有el下的元素，根据一定的规律取出数据 用flag每5个为一条数据
#执行时不能打开excel文档，会有读写冲突

#修改url中的 1.html 翻页
URL='''
    https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,
    2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9
    &fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
'''
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
response = requests.get(URL,headers=HEADERS)
text = response.content.decode('gbk')
html = etree.HTML(text)


#标题
title=html.xpath('//div[contains(@class,"el") and contains(@class,"title")]//span/text()')
title.append('工作链接')
title.append('公司链接')
print(title)

htmlData=html.xpath('//div[@class="dw_table"]//div[@class="el"]/./descendant::*')

jobs=list()
def fmtItem(foo):
    tmp={}
    for i in foo:
        arr=i.attrib
        
        if(arr.get('target')!=None and arr.get('onmousedown')!=None):
            tmp["job"]=arr.get('title')
            tmp["jobUrl"]=arr.get('href')
            continue
        if(arr.get('target')!=None and arr.get('onmousedown')==None):
            tmp["company"]=arr.get('title')
            tmp["companyUrl"]=arr.get('href')
            continue
        if(arr.get('class')!=None and arr.get('class')=='t3'):
            tmp["salary"]=i.text
            continue
        if(arr.get('class')!=None and arr.get('class')=='t4'):
            tmp["address"]=i.text
            continue
        if(arr.get('class')!=None and arr.get('class')=='t5'):
            tmp["date"]=i.text
            #print(tmp)
            jobs.append(tmp)
            tmp={}

#格式化数据
fmtItem(htmlData)

book = xlwt.Workbook('utf-8')
sheet = book.add_sheet('jobs')
head = title
for h in range(len(head)):
    sheet.write(0, h, head[h])  # 写入表头
sheet.col(0).width = 8000
sheet.col(1).width = 8000
sheet.col(2).width = 4000
sheet.col(3).width = 4000
sheet.col(4).width = 4000
sheet.col(5).width = 4000
sheet.col(6).width = 4000
y = 0
x = 1
for o in jobs:
    sheet.write(x, y, o['job'])
    sheet.write(x, y+1, o['company'])
    sheet.write(x, y+2, o['salary'])
    sheet.write(x, y+3, o['address'])
    sheet.write(x, y+4, o['date'])
    sheet.write(x, y+5, o['jobUrl'])
    sheet.write(x, y+6, o['companyUrl'])
    x=x+1
book.save('jobs.xls')




