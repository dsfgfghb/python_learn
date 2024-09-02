import requests
import json

url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

requests_dict = r.json()
response_string = json.dumps(requests_dict, indent=4)   #requests_dict 字典转换为 JSON 格式的字符串，并设置缩进为 4 个空格
print(response_string)