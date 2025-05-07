import cv2

image = cv2.imread("test.jpeg",cv2.IMREAD_UNCHANGED)
cv2.imshow("resized",image)

scale_percent = 50
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
output = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

cv2.imwrite("resized.jpg",output)
cv2.waitKey(0)