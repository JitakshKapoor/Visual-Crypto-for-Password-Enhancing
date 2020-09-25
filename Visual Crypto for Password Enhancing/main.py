
from PIL import Image, ImageDraw, ImageFont

image = Image.open('Pictures/background.png')

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('Roboto-Bold.ttf', size = 80)

(x, y) = (50, 50)

color = 'rgb(0, 0, 0)'
print("Enter the password to be encrypted: ")
message = input()
draw.text((x, y), message, fill = color, font = font)
image.save('Pictures/password.png')

