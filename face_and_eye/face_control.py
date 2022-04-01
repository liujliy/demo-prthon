import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/LIU.JIANG/Desktop/1.jpeg' , 0)
flag,frame = cv.threshold(img , 70 , 255 , cv.THRESH_BINARY)

contor,_ = cv.findContours(frame.copy(),cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

hull = [cv.convexHull(c) for c in contor]

final = cv.drawContours(img , hull , -1 , (0 , 0 , 0) )
cv.imshow('original_image' , img)
cv.imshow('thres' , frame)
cv.imshow('final_hsv' , final)

cv.waitKey(0)
cv.destroyAllWindows()