import cv2
import numpy as np
#face detection
#menggunakan metode viola & jones (realtime)
#menggunakan cascades (sebuah detector sdh jadi) untuk mendeteksi object tertentu
#cascade method bkn merupakkan metode paling akurat utk mendeteksi objeect
#tp cascade ini meotde yg paling cepat utk digunakan. metode cascade ini bisa kita 
#temukan pada detector kamera scara realtime

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/lena.png")
imgGray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)

#face cascade.detect multi scale (target gambar, luas besar kotaknya
# , minNeighbor (dapat dilihat pada kite) )
faces = faceCascade.detectMultiScale(imgGray, 1.5,4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 3)

cv2.imshow("Hasil",img)
cv2.waitKey(0)