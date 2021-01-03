import cv2
import numpy as np
#contours/shape detection
#kita akan mendeteksi dia termasuk shape apa, brp titik sudut dari shape, 
#dan berapa luas per-area

#kita harus mendefinisikan bgmn caranya kita mengambil bentuk garisnya
#makanya kita membuatkan getContours
def getContours(img):
    #cv2.findContours (target gambar, metode yg kita pake utk mengambil shape)
    #kita pake retr_external utk mencari detail luarnya saja
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #membuat looping utk mencetak garis contour
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print (area)
        #dsini dituliskan utk mendeteksi luas pixel area, jika kurang dri 
        # yg dituliskan, maka akan dilakukan perhitungan approximation
        if area > 500:
            #menggambar garis contour (target img, contoursnya, garis utk mendeteksi
            # semua shape, (warna garis), ktebalan garis)
            cv2.drawContours(imgContour, cnt, -1,(255,0,0), 3)
            #peri mengartikkan parameter/ perimeter, true mengartikan jika 
            # shapenya tertutup atau tdk, krn tertutup, maka true
            peri = cv2.arcLength(cnt, True)
            # print (peri)
            
            #approx adalah utk print perkiraan banyak sudut shape
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print (approx)
            #mendefinsikan banyak corner
            objCor = len(approx)
            #kita membuat kotak utk mendeteksi shape
            x, y , w, h = cv2.boundingRect(approx)
            
            #skrg, bila sudut sm dgn 3, maka shapenya adalah segitiga
            if objCor == 3: objectType = "Segitiga"
            #jika shapenya sm dgn 4, maka kotak / persegi panjang
            #utk bisa membedakan, kita mesti membagi aspect rationya
            #jika asp rationya kurang lebih sama, maka dikategorikan persegi
            #jika tidak, masuknya persegi panjang
            elif objCor == 4: 
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05: objectType = "Kotak"
                else: objectType = "Panjang"
            #bila sudut diatas dgn 4, maka shapenya adalah lingkaran
            elif objCor > 4: objectType = "Lingkaran"
            #lebih dari ini, maka dikategorikan undefined / blm didefinisikan
            else : objectType = "Undefined"
            
            #fungsi dibawah utk memberikkan dimensi kotak thd contour shape
            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 2)
            #fungsi dubawah utk memberikan text ditengah2 kotak diatas
            cv2.putText(imgContour, objectType, 
                        (x+(w//2)-10,y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                        (0,0,0), 2)
            

path = "Resources/shapes.png"
img = cv2.imread(path)
#img contour = img copy, maksudnya isinya sm dgn img
imgContour = img.copy()

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Gaussian blur (target img, (tingkat blur h/w), sigma itu tingkat blurry)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)
imgCanny = cv2.Canny(imgBlur, 50,50)
getContours(imgCanny)

#kita mau menambahkan img blank, agar array stacknya terpenuhi
imgBlank = np.zeros_like(img)
imgStack = stackImages(0.6, ([img,imgGray, imgBlur], 
                             [imgCanny, imgContour, imgBlank]))

# cv2.imshow("Testing shapes", img)
# cv2.imshow("Testing Blur", imgBlur)
cv2.imshow("Gambar Gabungan", imgStack)
cv2.waitKey(0)