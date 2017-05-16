import requests
from PIL import Image

file = open('faces.jpg', 'rb')
image_data = file.read()

headers = {
    "Content-Type": "application/octet-stream",
    "Ocp-Apim-Subscription-Key": "4e1b81e79bc54477b874a9bfae3e45e9"
}

url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"

result = requests.post(url, data=image_data, headers=headers)

faces_list = result.json()
im = Image.open('faces.jpg')
for face in faces_list:
    coords = face['faceRectangle']
    emotions = face['scores']
    emotions_list = list(emotions.items())
    emotions_sorted = sorted(emotions_list, key=lambda x: x[1], reverse=True)
    emotions = emotions_sorted[0][0]

    if emotions == 'Anger':
        smile = Image.open('Anger.png').convert('RGBA')
        smile = smile.resize((coords['width'], coords['height']))
    elif emotions == 'Contempt':
        smile = Image.open('Contempt.png').convert('RGBA')
        smile = smile.resize((coords['width'], coords['height']))
    elif emotions == 'Disgust':
        smile = Image.open('Disgust.png').convert('RGBA')
        smile = smile.resize((coords['width'], coords['height']))
    elif emotions == 'Surprise':
        smile = Image.open('Neutral.png').convert('RGBA')
        smile = smile.resize((coords['width'], coords['height']))
    elif emotions == 'Fear':
        smile = Image.open('Fear.png').convert('RGBA')
        smile = smile.resize((coords['width'], coords['height']))
    elif emotions == 'Happiness':
        smile = Image.open('Happiness.png').convert('RGBA')
        smile = smile.resize((coords['width'], coords['height']))
    elif emotions == 'Neutral':
        smile = Image.open('Neutral.png').convert('RGBA')
        smile = smile.resize((coords['width'], coords['height']))
    elif emotions == 'Sadness':
        smile = Image.open('Sadness.png').convert('RGBA')
        smile = smile.resize((coords['width'], coords['height']))

    im.paste(smile, box, smile)
im.show()