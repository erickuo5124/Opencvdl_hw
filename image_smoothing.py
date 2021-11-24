import cv2

def gaussian_blur():
    img_path = 'Dataset_OpenCvDl_Hw1/Q2_Image/Lenna_whiteNoise.jpg'
    img = cv2.imread(img_path)
    blur = cv2.GaussianBlur(img,(5,5),0)
    cv2.imshow("Gaussian Blur", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def bilateral_filter():
    img_path = 'Dataset_OpenCvDl_Hw1/Q2_Image/Lenna_whiteNoise.jpg'
    img = cv2.imread(img_path)
    bilateral = cv2.bilateralFilter(img, 9, 90, 90)
    cv2.imshow("Bilateral Filter", bilateral)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def median_filter():
    img_path = 'Dataset_OpenCvDl_Hw1/Q2_Image/Lenna_pepperSalt.jpg'
    img = cv2.imread(img_path)
    median_3 = cv2.medianBlur(img, 3)
    median_5 = cv2.medianBlur(img, 5)
    cv2.imshow("Median Blur 3x3", median_3)
    cv2.imshow("Median Blur 5x5", median_5)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
