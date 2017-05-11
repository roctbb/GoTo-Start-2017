from PIL import Image

im = Image.open("dog.jpg")
pixels = im.load()

for i in range(im.width):
    for j in range(im.height):
        r, g, b = pixels[i, j]
        S = (r+g+b)//3
        pixels[i, j] = (S, S, S)

im.show()