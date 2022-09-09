import cv2
import tkinter as tk
from tkinter import *
from tkinter import messagebox

ws = tk.Tk()
ws.geometry("700x700")
ws.title('Camera Fridge Object Detection')
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
    cv2.imshow('Camera Fridge Object Detection', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break


def product_List():
    ws3.withdraw()
    import productlist

nextButton = tk.Button(ws, text="Next", command=product_List)
nextnButton.place(x=700, y=525)

cap.release()
cv2.destroyAllWindows()
ws.mainloop()