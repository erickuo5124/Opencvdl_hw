import cv2
import os
import numpy as np

dir_path = './Dataset/Q2_Image'
col = 11
row = 8
img_index = 0

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((row*col,3), np.float32)
objp[:,:2] = np.mgrid[0:col,0:row].T.reshape(-1,2)

objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

img_paths = []
for (dirpath, dirnames, filenames) in os.walk(dir_path):
    for filename in filenames:
        path_name = dir_path + '/' + filename
        assert os.path.exists(path_name)
        img_paths.append(path_name)

def input_changed(num):
    global img_index
    img_index = int(num) - 1

def corner_detection():
    for img_path in img_paths:
        img = cv2.imread(img_path)
        ok, corners = cv2.findChessboardCorners(img, (col, row), None)
        if ok:
            cv2.drawChessboardCorners(img, (col, row), corners, ok)
            cv2.imshow('find corners', img)
            cv2.waitKey(500)
            cv2.destroyAllWindows()
        else: print('Corner not found!')

def find_intrinsic():
    for img_path in img_paths:
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ok, corners = cv2.findChessboardCorners(gray, (col, row), None)
        if ok:
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners)
        else: print('Corner not found!')
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    print(mtx)

def find_extrinsic():
    for img_path in img_paths:
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ok, corners = cv2.findChessboardCorners(gray, (col, row), None)
        if ok:
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners)
        else: print('Corner not found!')
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    global img_index
    rvecs, tvecs = np.float32(rvecs[img_index]), np.float32(tvecs[img_index])
    dst, jacobin = cv2.Rodrigues(rvecs)
    extrinsic = np.append(dst, tvecs, axis=1)
    np.set_printoptions(suppress=True)
    print(extrinsic)

def find_distortion():
    for img_path in img_paths:
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ok, corners = cv2.findChessboardCorners(gray, (col, row), None)
        if ok:
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners)
        else: print('Corner not found!')
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    print(dist)

def show_result():
    for img_path in img_paths:
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ok, corners = cv2.findChessboardCorners(gray, (col, row), None)
        if ok:
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners)
        else: print('Corner not found!')
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    for img_path in img_paths:
        img = cv2.imread(img_path)
        h,  w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

        # undistort
        dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
        # crop the image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]
        cv2.imshow('origin image', img)
        cv2.imshow('calibresult', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
