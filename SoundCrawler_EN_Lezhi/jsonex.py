import requests
import json

URL="https://www.baidu.com/sugrec?prod=pc_his&from=pc_web&json=1&sid=1467_31169_21088_31254_31422_31341_30901_31228_30823_31086_26350_31163_31196&hisdata=&csor=0"
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
cookiesDit={
    "sid":'123321'
}
response = requests.get(URL,headers=HEADERS,cookies=cookiesDit)
response.encoding='utf-8'
json=json.loads(response.text)
print(json)
print("err_no:",json.get("err_no"))
print(response.headers.get_dict())



