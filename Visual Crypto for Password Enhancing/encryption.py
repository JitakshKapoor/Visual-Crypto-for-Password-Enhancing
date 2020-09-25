from PIL import Image, ImageDraw
from random import SystemRandom

random = SystemRandom()
img = Image.open("Pictures/password.png")

img = img.convert('1')

outfileA = Image.new('1', (img.size[0]*2, img.size[1]*2))
outfileB = Image.new('1', (img.size[0]*2, img.size[1]*2))

imgA = ImageDraw.Draw(outfileA)
imgB = ImageDraw.Draw(outfileB)

patterns = ((1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1),
            (0, 1, 1, 0), (0, 1, 0, 1), (0, 0, 1, 1))

for x in range(0, img.size[0]):
    for y in range(0, img.size[1]):
        pixel = img.getpixel((x, y))
        pat = random.choice(patterns)
        imgA.point((x*2, y*2), pat[0])
        imgA.point((x*2 + 1, y*2), pat[1])
        imgA.point((x*2, y*2+1), pat[2])
        imgA.point((x*2 + 1, y*2 + 1), pat[3])
        if pixel == 0:
            imgB.point((x*2, y*2), 1 - pat[0])
            imgB.point((x*2 + 1, y*2), 1 - pat[1])
            imgB.point((x*2, y*2 + 1), 1 - pat[2])
            imgB.point((x*2 + 1, y*2 + 1), 1 - pat[3])
        else:
            imgB.point((x*2, y*2), pat[0])
            imgB.point((x*2 + 1, y*2), pat[1])
            imgB.point((x*2, y*2 + 1), pat[2])
            imgB.point((x*2 + 1, y*2 + 1), pat[3])

outfileA.save("Shared Images\sharedImage1.png")
outfileB.save("Shared Images\sharedImage2.png")