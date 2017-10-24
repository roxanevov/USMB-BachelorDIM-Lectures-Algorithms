# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:11:15 2017

@author: vovardr
"""

import cv2
import numpy as np 
img_gray=cv2.imread('img_s3.jpg',0)
img_bgr=cv2.imread('img_s3.jpg',1) 
print("Gray levels image shape = "+str(img_gray.shape)) 

def invert_colors_manual(input_img):
   img_inv=np.zeros(img_bgr.shape,dtype=np.uint8) 
   for rowIdx in xrange(img_bgr.shape[0]):
       for colIdx in xrange(img_bgr.shape[1]):
           for chIdx in xrange(img_bgr.shape[2]):
               img_inv[rowIdx,colIdx,chIdx]=255-img_bgr[rowIdx,colIdx,chIdx]
   return img_inv

def invert_colors_numpy(input_img):
    img_inv=np.zeros(img_bgr.shape,dtype=np.uint8)
    img_inv=255-img_bgr
    return img_inv

def invert_colors_opencv(input_img):
    img_inv=np.zeros(img_bgr.shape,dtype=np.uint8)
    img_inv=cv2.bitwise_not(input_img)
    return img_inv
    
img_manual=invert_colors_manual(img_bgr)
#cv2.imshow("BGR image", img_manual)
#cv2.waitKey()

img_numpy=invert_colors_numpy(img_bgr)
#cv2.imshow("BGR image", img_numpy)
#cv2.waitKey()

img_cv2=invert_colors_opencv(img_bgr)
cv2.imshow("BGR image", img_cv2)
cv2.waitKey()