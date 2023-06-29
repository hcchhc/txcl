# -*- codeing = utf-8 -*-
# @Author : han
# @File : UI.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QWidget, QPushButton, QMessageBox
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Button', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        sender = self.sender()
        QMessageBox.information(self, 'Information', 'Button "%s" clicked' % sender.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyWidget()

    MainWindow.show()
    sys.exit(app.exec_())