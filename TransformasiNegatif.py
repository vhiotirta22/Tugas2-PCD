print("Nama\t: Vhio Tirta Anggun Azizah")
print("Stambuk\t: F55122066\n")

import cv2

img = cv2.imread("mammogram.jpg")

img_1 = 255-img
cv2.imshow( "Original Image", img)
cv2.imshow("Image Negative", img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()



