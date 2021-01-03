import cv2
import numpy as np
#1.kali ini kita akan mencoba untuk mendeteksi warna

#2. mendefinisikan img yg ingin dideteksi warnanya
img = cv2.imread("Resources/lambo.png")

#7. disini kita akan mendefinisikan dari variabel, tapi tak berisikan apapun kecuali huruf a
def empty(a):
    pass

#anyway, berikut source code untuk menstackk gambar
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

#5. nah karena kita ingin mendeteksi warna, kita mesti tau margin warnanya
cv2.namedWindow("Track Bars")
cv2.resizeWindow("Track Bars", 640, 240)
#6. membuat trackbar untuk Hue, angka pertama adalah min, kedua adalah max, 
#dan ketiga adalah fungsi yang kita panggil setiap user mengubah trackbarsnya
cv2.createTrackbar("Hue Min", "Track Bars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Track Bars", 26, 179, empty)
cv2.createTrackbar("Sat Min", "Track Bars", 139, 255, empty)
cv2.createTrackbar("Sat Max", "Track Bars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Track Bars", 160, 255, empty)
cv2.createTrackbar("Val Max", "Track Bars", 255, 255, empty)
#8. setelah membuat trackbarnya, sekarang kita membutuhkan trackbar ini
#agar dapat diimplementasikan ke image kita

#11. kita mulai while truenya
while True:
    #3. kita harus menggunakan HSV space terlebih dahulu
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #4. tapi karena kita tidak mengetahui margin min-max dari warna yang ingin kita
    #deteksi, maka kita mesti membuat trackbar warna, mari kita buat diatas
    #9. berikut untuk implemented perubahan dari step 8
    h_min = cv2.getTrackbarPos("Hue Min", "Track Bars")
    h_max = cv2.getTrackbarPos("Hue Max", "Track Bars")
    s_min = cv2.getTrackbarPos("Sat Min", "Track Bars")
    s_max = cv2.getTrackbarPos("Sat Max", "Track Bars")
    v_min = cv2.getTrackbarPos("Val Min", "Track Bars")
    v_max = cv2.getTrackbarPos("Val Max", "Track Bars")
    print (h_min, h_max, s_min, s_max, v_min, v_max)
    #10. karena kita menginginkan agar nilai yg kita ubah terus terpanggil
    #makanya kita butuh untuk menyimpannya dalam while true
    
    #11. sekarang kita mencoba untuk membuat mask
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    #fungsi bitwise berfungsi sebagai memanggil 2 gambar dan menggabungkannya langsung
    #and, maka mengambil 2 gambar jd 1 gambar baru
    #mask pertama adalah mask, mask kedua adalah variabel
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    #4.2 kita testing manggil, img dan imghsv
    # cv2.imshow("Testing Image", img)
    # cv2.imshow("Testing Image HSV", imgHSV)
    # cv2.imshow("Testing Image Mask", mask)
    # cv2.imshow("Testing Result Mask", imgResult)
    
    #karena sudah ada stack images, maka cv2imshow diatas dibuat sbg komentar sj
    imgStack = stackImages(0.6, ([img, imgHSV],[mask, imgResult]))
    cv2.imshow("Gambar All in One", imgStack)

    if cv2.waitKey(1) & 0XFF ==ord('q'):
        break
