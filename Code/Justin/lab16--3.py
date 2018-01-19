from PIL import Image



img1 = Image.open("./gifs/dude.jpg")
img2 = Image.open("./gifs/flower.jpg")
img3 = img2


width, height = img1.size
pixels1 = img1.load()
pixels2 = img2.load()
pixels3 = img3.load()




for i in range(width):
    for j in range(height):
        r1, g1, b1 = pixels1[i, j]
        r2, g2, b2 = pixels2[i, j]

        r3 = int((r1 + r2) / 2)
        g3 = int((g1 + g2) / 2)
        b3 = int((b1 + b2) / 2)



        pixels3[i, j] = (r3, g3, b3)



img3.show()