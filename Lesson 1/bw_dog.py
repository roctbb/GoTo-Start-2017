from PIL import Image
file = input("введите имя картинки:")
im = Image.open(file)
pixels = im.load()

for i in range(im.width//2):
    for j in range(im.height):
        r, g, b = pixels[i, j]
        S = (r+g+b)//3
        if S < 100:
            pixels[i, j] = (255,255,255)
        else:
            pixels[i, j] = (0,125,125)
for i in range(im.width//2, im.width):
    for j in range(im.height):
        r, g, b = pixels[i, j]
        S = (r+g+b)//3
        if S < 100:
            pixels[i, j] = (255,255,255)
        else:
            pixels[i, j] = (125,125,0)
im.show()
im.save("result.jpg")