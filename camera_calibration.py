import cv2
import os

dir_path = './Dataset/Q2_Image'
col = 11
row = 8

def corner_detection():
    for (dirpath, dirnames, filenames) in os.walk(dir_path):
        for filename in filenames:
            path_name = dir_path + '/' + filename
            assert os.path.exists(path_name)
            img = cv2.imread(path_name)
            ok, corners = cv2.findChessboardCorners(img, (col, row), None)
            if ok:
                cv2.drawChessboardCorners(img, (col, row), corners, ok)
                cv2.imshow('find corners', img)
                cv2.waitKey(500)
                cv2.destroyAllWindows()
            else: print('Corner not found!')

def find_intrinsic():
    print('find_intrinsic')

def find_extrinsic():
    print('find_extrinsic')

def find_distortion():
    print('find_distortion')

def show_result():
    print('show_result')