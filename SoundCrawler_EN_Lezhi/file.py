import os

singleBookDir="单行书"
seriesBooKDir="套系书"

if not os.path.exists(singleBookDir):
    os.makedirs(singleBookDir)

if not os.path.exists(seriesBooKDir):
    os.makedirs(seriesBooKDir)



def getFloder(bookId,bookName,series):
    xpath=str(bookId)+"-"+bookName
    if not os.path.exists(bookName):
        os.makedirs(bookName)
        return bookName
    elif not os.path.exists(xpath):
        os.makedirs(xpath)
        return xpath
    else:
        return xpath
        
print(getFloder(2,"单行书","series"))
