import requests

url = "https://api.vk.com/method/{0}?{1}&access_token={2}&v={3}"
method = "wall.post"
token = "2feef6c285d89838e0f23489f6a0ebb93d4ae9660e5544b25b9cc72dd8b5067ac1fa72ccd56b5164b3ba1"
v = "5.65"
params = "owner_id={0}&message=vk_api_test"
target = ""
full_url = url.format(method, params.format(target),token,v)
for i in range(5):
    result = requests.get(full_url)
    print(result.text)