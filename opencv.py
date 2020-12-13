import cv2
#from tesseract import main11,frame1
from threading import Thread
import pytesseract
# from speak import Data
from speak import speaking
# from speak import speak
#print(Data)
import keyboard
import pyautogui
#t11 = Thread(target=speak)
#main()

text = []
def reading():
    count = 0 
    video= cv2.imread('D:/Destop/EDITH/read.png') #'D:\Destop\Recording\Adobe_Spark_Video.mp4'
    #t11.start()
    # cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    # ret,frame = cap.read()
    frame = video  
    while True:
        # count += 1  
        # print(count)
        cv2.imshow('Object detector', frame)
        cv2.waitKey(10)            
        cv2.imwrite('D:/Destop/EDITH/reads.jpg',frame)
        break
    cv2.destroyAllWindows()
    frame = cv2.imread('D:/Destop/EDITH/reads.jpg')
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    text1 = pytesseract.image_to_string(frame)
    data = text1.split()
    speaking(data) 
#t1.join()

reading()
# video = cv2.imread('D:/Destop/EDITH/read.png')
# pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
# text1 = pytesseract.image_to_string(video)
# print(text1)
# speaking(text1)