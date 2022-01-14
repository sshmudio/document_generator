# import cv2
# import numpy as np


# def background_rm(image):
#     img = cv2.imread(image)
#     lower = np.array([210, 210, 210])
#     upper = np.array([255, 255, 255])
#     thresh = cv2.inRange(img, lower, upper)
#     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20))
#     morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
#     mask = 255 - morph
#     result = cv2.bitwise_and(img, img, mask=mask)

#     cv2.imwrite('pills_result.png', result)


# background_rm('lebed.jpg')
from PIL import Image

img = Image.open('lebed.jpg').convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("img2.png", "PNG")
