import cv2 as cv
import numpy as np

img = np.zeros((600, 900, 3), dtype=np.uint8)
cv.rectangle(img,(0,0),(900,600),(255,255,255), -1)
cv.rectangle(img,(40,40),(100,100), -1)
cv.circle(img,(200,150), 60, -1)
cv.line(img,(450,300), (0,300), 5)
font = cv.FONT_HERSHEY_COMPLEX_SMALL
cv.putText(img, "SIGMA", (120,490), font, 1.5, (0,0,0), 2)
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()