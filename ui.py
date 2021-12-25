from PyQt5.QtWidgets import (
  QApplication,
  QHBoxLayout,
  QVBoxLayout,
  QPushButton,
  QWidget,
  QGroupBox,
  QLineEdit,
  QLabel
)
from PyQt5.QtGui import QIntValidator
from camera_calibration import (
    corner_detection,
    find_intrinsic,
    find_extrinsic,
    find_distortion,
    show_result
)

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Opencvdl_hw1")

    layout = QHBoxLayout()
    
    layout.addWidget(self.q2())
    layout.addWidget(self.q5())

    self.setLayout(layout)

  def q2(self):
    find_corners_btn = QPushButton('2.1 Find Corners')
    find_intrinsic_btn = QPushButton('2.2 Find Intrinsic')

    find_extrinsic_group = QGroupBox("Find Extrinsic")
    img_input = QLineEdit()
    img_input.setValidator(QIntValidator())
    img_label = QLabel('select image: ')
    img_select = QHBoxLayout()
    img_select.addWidget(img_label)
    img_select.addWidget(img_input)
    find_extrinsic_btn = QPushButton('2.3 Find Extrinsic')
    v_layout = QVBoxLayout()
    v_layout.addLayout(img_select)
    v_layout.addWidget(find_extrinsic_btn)
    find_extrinsic_group.setLayout(v_layout)

    find_distortion_btn = QPushButton('2.4 Find Distortion')
    show_result_btn = QPushButton('2.5 Show Result')

    find_corners_btn.clicked.connect(corner_detection)
    find_intrinsic_btn.clicked.connect(find_intrinsic)
    find_extrinsic_btn.clicked.connect(find_extrinsic)
    find_distortion_btn.clicked.connect(find_distortion)
    show_result_btn.clicked.connect(show_result)

    groupbox = QGroupBox("Calibration")
    v_layout = QVBoxLayout()

    v_layout.addWidget(find_corners_btn)
    v_layout.addWidget(find_intrinsic_btn)
    v_layout.addWidget(find_extrinsic_group)
    v_layout.addWidget(find_distortion_btn)
    v_layout.addWidget(show_result_btn)
    groupbox.setLayout(v_layout)
    return groupbox

  def q5(self):
    show_model_btn = QPushButton('5.1 Show Model Structure')
    show_board_btn = QPushButton('5.2 Show TensorBoard')
    test_btn = QPushButton('5.3 Test')
    img_select = QLineEdit()
    show_augmentation_btn = QPushButton('5.4 Data Augmentation')

    groupbox = QGroupBox("Dogs and Cats classification Using ResNet50")
    v_layout = QVBoxLayout()

    v_layout.addWidget(show_model_btn)
    v_layout.addWidget(show_board_btn)
    v_layout.addWidget(test_btn)
    v_layout.addWidget(img_select)
    v_layout.addWidget(show_augmentation_btn)
    groupbox.setLayout(v_layout)
    return groupbox

