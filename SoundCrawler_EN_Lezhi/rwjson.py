import os
import json

jsonData={'_SID_': 'N2I5ZTVlMDQtOTFmYS00NTIxLTkxZWYtNmUwNzZjY2EyNGE4'}

cookie = open('cookie.txt','w',encoding='utf-8')
cookie.write(str(jsonData))

print(os.path.exists('cookie.txt'))

