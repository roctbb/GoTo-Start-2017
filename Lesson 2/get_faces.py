import requests

file = open('faces.jpg', 'rb')
image_data = file.read()

headers={
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-Key": "ed949f112a524980ad1907524eb7d32d"
}

url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"

result = requests.post(url, data=image_data, headers=headers)

print(result.text)