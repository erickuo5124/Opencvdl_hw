from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QGroupBox
)
from image_processing import (
    load_img, 
    color_separation, 
    color_transformation, 
    blending
)
from image_smoothing import (
    gaussian_blur,
    bilateral_filter,
    median_filter
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Opencvdl_hw1")

        layout = QHBoxLayout()
        
        layout.addWidget(self.q1())
        layout.addWidget(self.q2())
        layout.addWidget(self.q3())
        layout.addWidget(self.q4())

        self.setLayout(layout)

    def q1(self):
        groupbox = QGroupBox("Image Processing")
        load_img_btn = QPushButton('1.1 Load Image')
        color_separation_btn = QPushButton('1.2 Color Separation')
        color_transformation_btn = QPushButton('1.3 Color Transformation')
        blending_btn = QPushButton('1.4 Blending')

        load_img_btn.clicked.connect(load_img)
        color_separation_btn.clicked.connect(color_separation)
        color_transformation_btn.clicked.connect(color_transformation)
        blending_btn.clicked.connect(blending)

        v_layout = QVBoxLayout()
        groupbox.setLayout(v_layout)
        
        v_layout.addWidget(load_img_btn)
        v_layout.addWidget(color_separation_btn)
        v_layout.addWidget(color_transformation_btn)
        v_layout.addWidget(blending_btn)

        return groupbox

    def q2(self):
        groupbox = QGroupBox("Image Smoothing")
        gaussian_blur_btn = QPushButton('2.1 Gaussian Blur')
        bilateral_filter_btn = QPushButton('2.2 Bilateral Filter')
        median_filter_btn = QPushButton('2.3 Median Filter')

        gaussian_blur_btn.clicked.connect(gaussian_blur)
        bilateral_filter_btn.clicked.connect(bilateral_filter)
        median_filter_btn.clicked.connect(median_filter)

        v_layout = QVBoxLayout()
        groupbox.setLayout(v_layout)

        v_layout.addWidget(gaussian_blur_btn)
        v_layout.addWidget(bilateral_filter_btn)
        v_layout.addWidget(median_filter_btn)

        return groupbox

    def q3(self):
        groupbox = QGroupBox("Edge Detection")
        gaussian_blur_btn = QPushButton('3.1 Gaussian Blur')
        sobel_x_btn = QPushButton('3.2 Sobel X')
        sobel_y_btn = QPushButton('3.3 Sobel Y')
        magnitude_btn = QPushButton('3.4 Magnitude')

        v_layout = QVBoxLayout()
        groupbox.setLayout(v_layout)

        v_layout.addWidget(gaussian_blur_btn)
        v_layout.addWidget(sobel_x_btn)
        v_layout.addWidget(sobel_y_btn)
        v_layout.addWidget(magnitude_btn)

        return groupbox
    
    def q4(self):
        groupbox = QGroupBox("Transformation")
        resize_btn = QPushButton('4.1 Resize')
        translation_btn = QPushButton('4.2 Translation')
        rotation_scaling_btn = QPushButton('4.3 Rotation, Scaling')
        shearing_btn = QPushButton('4.4 Shearing')

        v_layout = QVBoxLayout()
        groupbox.setLayout(v_layout)

        v_layout.addWidget(resize_btn)
        v_layout.addWidget(translation_btn)
        v_layout.addWidget(rotation_scaling_btn)
        v_layout.addWidget(shearing_btn)

        return groupbox
