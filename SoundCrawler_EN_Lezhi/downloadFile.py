import urllib.request


singleBookDir="单行书"

fileurl="https://www.0dutv.com/upload/dance/20200419/5C0B03D1E3FD2BDBC8CF14C48A9FCE63.mp3"
filename = fileurl.split('/')[-1]
filepath = singleBookDir + '/' + filename
urllib.request.urlretrieve("https://www.0dutv.com/upload/dance/20200419/5C0B03D1E3FD2BDBC8CF14C48A9FCE63.mp3",filepath)