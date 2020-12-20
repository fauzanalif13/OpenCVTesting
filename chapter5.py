import cv2
import numpy as np
#mengambil gambar dalam gambar
#atau dapat dibilang mengambil dan mengonversi gambar dri gambar, agar bisa jd lebih jelas
img = cv2.imread("D:\Fauzan Alif\Learn Python\Resources/card.jpg")

# #mencoba mengambil 1 gambar dri foto,
# pertama mengenali dlu letak pixelnya (bisa melalui paint)
# kemudian diterjemahkan ke dimensi kartu (yg kemudian nnti akan digunakan di matrix)
# setelah itu dioper ke variabel imgOutput kemudian ditampilkan
width, height = 250,350

#mengambil titik2 point pixel dari gambar referensi
assekop = np.float32([[563,102],[820,102],[566,477],[821,477]])
#didefinisikan secara variabel ksong, utk memuat target gambar yg nnti diambil
assekop2 = np.float32([[0,0],[width,0],[0,height],[width, height]])
matrix = cv2.getPerspectiveTransform(assekop, assekop2)

#mari kita menampilkan img
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Testing", imgOutput)

cv2.waitKey(0)