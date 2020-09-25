import cv2
from PIL import Image
import PIL.ImageOps

img1 = cv2.imread('Shared Images\sharedImage1.png', 1)
img2 = cv2.imread('Shared Images\sharedImage2.png', 1)
img = cv2.add(img1, img2)

overlap = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('Final Results\Overlapped_Image.png', overlap)

d1 = cv2.GaussianBlur(overlap, (5,5), cv2.BORDER_DEFAULT)

ret3,d2 = cv2.threshold(d1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('Final Results\decrypt1.png', d2)

image = Image.open('Final Results\decrypt1.png')
Final_image = PIL.ImageOps.invert(image)
Final_image.save('Final Results\Final_Decrypted_Image.png')












