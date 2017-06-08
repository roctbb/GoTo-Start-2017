import requests

headers = {
    "Host": 'habrahabr.ru',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

result = requests.get("https://habrahabr.ru", headers=headers)



with open("habr.html", 'wb') as file:
    file.write(result.content)