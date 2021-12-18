from PyQt5 import QtWidgets
import sys

from ui import Window

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec_())