import cv2 
image = cv2.imread('image.jpg')
h,w,c=image.shape
watermark = cv2.imread('watermark.png',)
watermark = cv2.resize(watermark, (w,h))
new_image = cv2.addWeighted(watermark, 1, image, 1, 0)
cv2.imshow(' watermarkedimage', new_image)
cv2.waitKey(0)
cv2.imwrite('watermarkedimage.jpg', new_image)
cv2.destroyAllWindows()