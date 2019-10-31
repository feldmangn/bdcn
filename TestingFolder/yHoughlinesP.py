import cv2
import numpy as np

img = cv2.imread('/home/pc/Documents/BiDirectionalCascadeEdge/images/wrongImages/bdcn/26.jpg')
threshold=200
minLineLength = 30
rho=5
maxLineGap=100
theta = 1

# here you convert the image to grayscale and then threshhold to binary
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
cv2.imshow("gray", gray)

# continue with the threshholded image instead
# gray = cv2.Canny(gray, 150, 100)

lines = cv2.HoughLinesP(gray, rho, theta, threshold, np.array([]), minLineLength=minLineLength, maxLineGap=maxLineGap)
for i in range(len(lines)):
  for line in lines[i]:
     cv2.line(img, (line[0],line[1]), (line[2],line[3]), (0,255,0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
