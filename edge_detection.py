import cv2
import numpy as np
from scipy import signal

img_path = 'Dataset_OpenCvDl_Hw1/Q3_Image/House.jpg'
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def get_gaussian_blur():
    # 3*3 Gassian filter
    x, y = np.mgrid[-1:2, -1:2]
    gaussian_kernel = np.exp(-(x**2+y**2))
    # Normalization
    gaussian_kernel = gaussian_kernel / gaussian_kernel.sum()
    # Apply filter
    grad = signal.convolve2d(gray, gaussian_kernel, boundary='symm', mode='same') 
    grad = np.array(grad).astype(np.uint8)
    return grad

def my_gaussian_blur():
    cv2.imshow('Original',img)
    cv2.imshow('Grayscale', gray)

    grad = get_gaussian_blur()
    cv2.imshow('Gaussian Blur', grad)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# x = 0, y = 1
def get_sobel(axis=0):
    operator = [
        np.array(
        [[-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]]),
        np.array(
        [[1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]])
    ]
    gaussian = get_gaussian_blur()
    grad = signal.convolve2d(gaussian, operator[axis], mode='same')
    grad = np.absolute(grad)
    grad = grad/grad.max()
    return grad

def sobel(axis=0):
    grad = get_sobel(axis)

    cv2.imshow(f'Sobel {"X" if axis == 0 else "Y"}', grad)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def magnitude():
    sobel_x = get_sobel(0)
    sobel_y = get_sobel(1)
    mag = np.sqrt(sobel_x**2 + sobel_y**2).astype(np.float64)
    cv2.imshow('Gaussian Blur', mag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
