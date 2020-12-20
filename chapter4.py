import cv2
import numpy as np
#pada chapter 4 ini, kita mempelajari bagaimana untuk membuat shape didalam cv2
img = np.zeros((512,512,3), np.uint8)
#print(img.shape)
#img[200:300,100:500] = 255,0,0

#format warna adalah BGR, Blue, Green, Red
#line (starting point, akhir point, warna, ketebalan -dapat dilihat difungsi kite)
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,0,255), (3))
cv2.rectangle(img, (0,0), (300,320), (0,255,0), cv2.FILLED)
cv2.circle(img, (400,250), 30, (255,0,0), (4))
cv2.putText(img , "Testing Open cv", (250, 400), cv2.FONT_HERSHEY_PLAIN, 1.2 , (0,244,0), (1))

cv2.imshow("Image", img)

cv2.waitKey(0)
