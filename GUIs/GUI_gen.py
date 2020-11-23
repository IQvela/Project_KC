#importing PyQt5 for making the interface
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
# QMessageBox


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        #event that is going to do when click button
        self.label.setText("adding project soon")
        self.update()

    def initUI(self):
        #create window
        self.setGeometry(200, 200, 300, 300) #position and size
        self.setWindowTitle("KC data")
        #create label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("KC data")
        self.label.move(50,50)
        #create button
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("add project")
        self.b1.clicked.connect(self.button_clicked) #event to happen

    def update(self):
        self.label.adjustSize()

#define window and calling
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()