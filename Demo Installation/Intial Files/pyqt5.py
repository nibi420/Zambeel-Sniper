from turtle import width
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



class MyWindow(QMainWindow): ##inherit from QMainWindow
    def __init__(self):
        super(MyWindow,self).__init__()
        xpos= 200
        ypos = 200
        width = 500
        height = 300
    
        self.setGeometry(xpos,ypos,width,height)
        self.setWindowTitle("Zambeel Sniper")
        self.initUI()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Please Enter Roll Number")
        self.update()
        self.label.move(40,50 )

        self.b1=QtWidgets.QPushButton(self)
        self.b1.setText("Enroll")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("ENROLLED!s uwh uwehweuhirwue ")
        self.update()


    def update(self):
        self.label.adjustSize()



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()