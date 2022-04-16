import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import cv2 as cv2
import pyautogui
import time
from pytesseract import pytesseract
from PIL import Image

root = Tk()
root.title('Tkinter App')

main_frame = Frame(root, borderwidth=1, relief=SOLID)
main_frame.pack()

def picCapture():
    pic = cv2.VideoCapture(0)
    result, image = pic.read()
    if result:
        # print(image)
        # cv2.imshow("GeeksForGeeks", image) 
        cv2.imwrite("Image.png", image)
        imgToText("image")
        # cv2.waitKey(0)
        # cv2.destroyWindow("GeeksForGeeks")

def showCam():
    vid = cv2.VideoCapture(0)
  
    while(True):
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            picCapture()
            break
    vid.release()
    cv2.destroyAllWindows()

def screenCapture():
    root.withdraw()
    time.sleep(1)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    filename = filedialog.asksaveasfilename(initialdir="", filetypes=(("png files", "*.png"),))
    if(filename!=""):
        filename = filename.replace(".png", "")
        cv2.imwrite(f"{filename}.png", image)
        imgToText(filename)
    root.deiconify()

def imgToText(filename):
    path_to_tesseract = r"C:\\Program Files\\Tesseract-OCR\\tesseract"
    image_path = f"{filename}.png"
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)
    entry = Text(root, font=("Halvetica", 16), height=100, width=100)
    entry.pack(padx=10, pady=10)
    entry.insert(END, text)

button1= Button(main_frame, text="Take Screenshot", command=screenCapture)
button1.pack(padx=10, pady=10)

button2= Button(main_frame, text="Take Picture", command=showCam)
button2.pack(padx=10, pady=10)

root.mainloop()