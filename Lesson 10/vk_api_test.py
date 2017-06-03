import requests

#формируем адрес страницы
url = "https://api.vk.com/method/{0}?{1}&access_token={2}&v={3}"
method = "wall.get"
token = "5481ac075481ac075481ac073a54ddd87e554815481ac070db33118649cb6131da032cb"
v = "5.65"
params = "domain=roctbb&count=100&offset={0}"
full_url = url.format(method, params.format(0),token,v)

#делаем запрос
result = requests.get(full_url)

#узнаем количество записей
json_result = result.json()
response = json_result["response"]
count = response["count"]

print(count)

#теперь скачиваем все посты
posts = []

for offset in range(0, count, 100):
    full_url = url.format(method, params.format(offset), token, v)
    result = requests.get(full_url)
    json_result = result.json()
    response = json_result["response"]
    items = response["items"]
    posts += items

sorted_posts = sorted(posts, key=lambda x:x["likes"]["count"], reverse=True)

#выводим
for post in sorted_posts:
    print(post["likes"]["count"])
    print(post["text"])