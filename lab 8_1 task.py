import cv2
#1 задание
image = cv2.imread('image-variant2.jpg')
blurred_image = cv2.GaussianBlur(image, ksize=(11, 11), sigmaX =0, sigmaY=0)
cv2.imwrite('blurred_image.jpg', blurred_image)
