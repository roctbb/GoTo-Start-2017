import requests

#формируем адрес страницы
url = "https://api.vk.com/method/{0}?{1}&access_token={2}&v={3}"
method = "wall.get"
token = "2feef6c285d89838e0f23489f6a0ebb93d4ae9660e5544b25b9cc72dd8b5067ac1fa72ccd56b5164b3ba1"
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

#sorted_posts = sorted(posts, key=lambda x:x["likes"]["count"], reverse=True)

#выводим
c = 0
for post in posts:
    if str(post["text"]).find("#kinopoisk") != -1:
        c+=1
        print(post["text"])

print("Number: {0}".format(c))