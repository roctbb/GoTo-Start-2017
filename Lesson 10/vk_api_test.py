import requests


url = "https://api.vk.com/method/{0}?{1}&access_token={2}&v={3}"
method = "wall.get"
token = "5481ac075481ac075481ac073a54ddd87e554815481ac070db33118649cb6131da032cb"
v = "5.65"
params = "domain=goto_msk&count=100&offset={0}"

full_url = url.format(method, params.format(0),token,v)
result = requests.get(full_url)

json_result = result.json()

response = json_result["response"]
items = response["items"]
count = response["count"]

print(count)

posts = []

for offset in range(0, count, 100):
    full_url = url.format(method, params.format(offset), token, v)
    result = requests.get(full_url)
    json_result = result.json()
    response = json_result["response"]
    items = response["items"]
    posts += items

for post in posts:
    print(post["text"])