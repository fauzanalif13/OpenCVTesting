import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
print(img.shape)

#fungsi resize diatur dengan weidht dlu, lalu height
imgResize = cv2.resize(img, (600, 200))
print(imgResize.shape)

#image crop harus diperhatikan baik2, karena heigh dlu, lalu weidht
imgCrop = img[0:400, 200:512]

cv2.imshow("lena", img)
cv2.imshow("lena Resize", imgResize)
cv2.imshow("lena cropped", imgCrop)
cv2.waitKey(0)

