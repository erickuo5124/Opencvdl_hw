import cv2
import numpy as np

def load_img():
    img_path = 'Dataset_OpenCvDl_Hw1/Q1_Image/Sun.jpg'
    img = cv2.imread(img_path)
    height, width = img.shape[:2]
    print(f'Height : {height}\nWidth : {width}')
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def color_separation():
    img_path = 'Dataset_OpenCvDl_Hw1/Q1_Image/Sun.jpg'
    img = cv2.imread(img_path)
    (B, G, R) = cv2.split(img)
    zeros = np.zeros(img.shape[:2], dtype = np.uint8)
    R = cv2.merge([zeros, zeros, R])
    cv2.imshow('Red', R)
    G = cv2.merge([zeros, G, zeros])
    cv2.imshow('Green', G)
    B = cv2.merge([B, zeros, zeros])
    cv2.imshow('Blue', B)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def color_transformation():
    img_path = 'Dataset_OpenCvDl_Hw1/Q1_Image/Sun.jpg'
    img = cv2.imread(img_path)
    img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("OpenCV function", img_1)
    (B, G, R) = cv2.split(img)
    avg_weight = np.average(np.array(cv2.split(img)), axis=0)
    avg_weight = avg_weight.astype(np.uint8)
    img_2 = cv2.merge([avg_weight, avg_weight, avg_weight])
    cv2.imshow("Average weighted", img_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def blending():
    img_1_path = 'Dataset_OpenCvDl_Hw1/Q1_Image/Dog_Weak.jpg'
    img_2_path = 'Dataset_OpenCvDl_Hw1/Q1_Image/Dog_Strong.jpg'
    img_1 = cv2.imread(img_1_path)
    img_2 = cv2.imread(img_2_path)
    value = 50
    img_sum = cv2.addWeighted(img_1, 0.5, img_2, 0.5, 0)
    cv2.imshow("Blend", img_sum)

    def update(x):
        global value
        value = x
        img_sum = cv2.addWeighted(
            img_1, 
            value/100, 
            img_2, 
            (100-value)/100, 
            0
        )
        cv2.imshow("Blend", img_sum)
    
    cv2.createTrackbar('Blend\n' , 'Blend', 0, 100, update)
    cv2.setTrackbarPos('Blend\n','Blend', value)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
