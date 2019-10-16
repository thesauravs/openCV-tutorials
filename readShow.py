import cv2 as cv

img = cv.imread('./data/lena.jpg', 0) #grayscale
#print(img)
cv.imshow('GrayScale', img)

#Save the image to target folder
cv.imwrite('lena_copy_gray.png', img)

imgColor = cv.imread('./data/lena.jpg', 1) #Color
#print(img)
cv.imshow('Color', imgColor)

cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
cv.waitKey(1)