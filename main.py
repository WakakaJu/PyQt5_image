import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets, QtCore
# import image_processing
from image_processing import Ui_MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())