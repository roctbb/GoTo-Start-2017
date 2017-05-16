import requests
from PIL import Image

file = open('faces.jpg', 'rb')
image_data = file.read()

headers = {
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-Key": "ed949f112a524980ad1907524eb7d32d"
}

url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"

result = requests.post(url, data=image_data, headers=headers)
faces_list = result.json()

im = Image.open("faces.jpg").convert("RGBA")

print(faces_list)

for face in faces_list:
    coords = face["faceRectangle"]
    emotions = face["scores"]



    print("face:")
    print("width: {0}".format(coords['width']))
    print("height: {0}".format(coords['height']))
    print("x: {0}".format(coords['left']))
    print("y: {0}".format(coords['top']))
    print("\n")

    x1 = coords['left']
    y1 = coords['top']

    x2 = x1 + coords['width']
    y2 = y1 + coords['height']

    box = (x1, y1, x2, y2)
    face_image = im.crop(box)
    face_image = face_image.rotate(45)

    im.paste(face_image, box, face_image)

im.show()