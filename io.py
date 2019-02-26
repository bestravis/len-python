f = open('file.txt','w',encoding='utf-8') #文件句柄,使用w时事实上是创建了一个新文件，如果源文件存在，会覆盖
f.write("I will go home!") 
f.write('\nByeBye!')
f.write('\nadfas')