import cv2
import numpy as np


def resize():
    img_path = 'Dataset_OpenCvDl_Hw1/Q4_Image/SQUARE-01.png'
    img = cv2.imread(img_path)    
    img = cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA)
    cv2.imshow('Resize',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def translation():
    img_path = 'Dataset_OpenCvDl_Hw1/Q4_Image/SQUARE-01.png'
    img = cv2.imread(img_path) 
    resized = cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA)

    M = np.float32([[1, 0, 0], [0, 1, 60]])
    shifted = cv2.warpAffine(resized, M, (img.shape[1], img.shape[0]))
    cv2.imshow('Translation',shifted)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotation_scaling():
    img_path = 'Dataset_OpenCvDl_Hw1/Q4_Image/SQUARE-01.png'
    img = cv2.imread(img_path) 
    resized = cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA)
    M = np.float32([[1, 0, 0], [0, 1, 60]])
    shifted = cv2.warpAffine(resized, M, (img.shape[1], img.shape[0]))

    M = cv2.getRotationMatrix2D((128, 188), 10, 0.5)
    rotated = cv2.warpAffine(shifted, M, (400, 300))
    cv2.imshow('Rotation, Scaling',rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def shearing():
    img_path = 'Dataset_OpenCvDl_Hw1/Q4_Image/SQUARE-01.png'
    img = cv2.imread(img_path) 
    resized = cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA)
    M = np.float32([[1, 0, 0], [0, 1, 60]])
    shifted = cv2.warpAffine(resized, M, (img.shape[1], img.shape[0]))
    M = cv2.getRotationMatrix2D((128, 188), 10, 0.5)
    rotated = cv2.warpAffine(shifted, M, (400, 300))

    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    M = cv2.getAffineTransform(pts1,pts2)
    sheared = cv2.warpAffine(rotated, M, (400, 300))
    cv2.imshow('Shearing',sheared)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
