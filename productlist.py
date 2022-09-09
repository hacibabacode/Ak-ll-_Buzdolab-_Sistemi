from tkinter import*
import tkinter as tk
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import ImageTk, Image

ws8= tk.Tk()
ws8.geometry("750x750")

img_rgb = cv2.imread('images/bz.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('images/balik1.jpg',0)
template1 = cv2.imread('images/sut1.jpg',0)
template2 = cv2.imread('images/karpuz1.jpg',0)
template3 = cv2.imread('images/meyve1.jpg',0)
template4 = cv2.imread('images/icecek1.jpg',0)
template5 = cv2.imread('images/kahvalti1.jpg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
res1 = cv2.matchTemplate(img_gray,template1,cv2.TM_CCOEFF_NORMED)
res2 = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
res3 = cv2.matchTemplate(img_gray,template3,cv2.TM_CCOEFF_NORMED)
res4 = cv2.matchTemplate(img_gray,template4,cv2.TM_CCOEFF_NORMED)
res5 = cv2.matchTemplate(img_gray,template5,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
loc1 = np.where( res1 >= threshold)
loc2 = np.where( res2 >= threshold)
loc3 = np.where( res3 >= threshold)
loc4 = np.where( res4 >= threshold)
loc5 = np.where( res5 >= threshold)
for pt in zip(*loc[::-1]):
     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
     
for pt in zip(*loc1[::-1]):
     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)     
 
for pt in zip(*loc2[::-1]):
     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

for pt in zip(*loc3[::-1]):
     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

for pt in zip(*loc4[::-1]):
     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

for pt in zip(*loc5[::-1]):
     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('images/Refrigerator.jpg',img_rgb)



ws8.mainloop()