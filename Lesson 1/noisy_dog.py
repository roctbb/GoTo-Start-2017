from PIL import Image
from random import randint

im = Image.open("dog.jpg")
pixels = im.load()

for i in range(im.width):
    for j in range(im.height):
        r, g, b = pixels[i, j]
        k = randint(0,100);
        r = (r + k) % 256
        g = (g + k) % 256
        b = (b + k) % 256
        pixels[i, j] = (r, g, b)

im.show()