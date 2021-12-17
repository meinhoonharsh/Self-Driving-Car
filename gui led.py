import os
import sys
import serial
from PyQt5 import QtGui,QtCore,QtWidgets

class window(QtWidgets.QMainWindow):
   def __init__(self):
      super(window,self).__init__()
      self.setGeometry(50,50,1400,900)  # setGeometry() to define the size of the window and where to place it on your screen.
                                        #The first two parameters are the x and y coordinates at which the window will be placed on the screen.
                                        #The third and fourth parameters are the width and height of the window.
      
      self.setWindowTitle("LED GUI | www.techtrunk.in") # With .setWindowTitle(), you can add a title to your application’s window.
                                                                     #In this case, the title to (show is Self Driving Car App | www.techtrunk.in
      self.label1=QtWidgets.QLabel("COM Port(e.g. COM13)",self)
      self.label1.resize(200,30)
      self.label1.move(50,80)
      self.comport=QtWidgets.QLineEdit(self)
      self.comport.move(50,115)
      self.comport.resize(80,30)
      self.off=QtWidgets.QPushButton("OFF",self)
      self.off.resize(80,50)
      self.off.move(130,480)
      self.on=QtWidgets.QPushButton("ON",self)
      self.on.resize(80,50)
      self.on.move(130,400)
      self.start=QtWidgets.QPushButton("Start",self)
      self.start.resize(80,50)
      self.start.move(80,600)
      self.stop=QtWidgets.QPushButton("Close",self)
      self.stop.resize(80,50)
      self.stop.move(180,600)
      self.start.clicked.connect(self.openport)
      self.stop.clicked.connect(self.closeport)
      self.off.clicked.connect(self.LedOff)
      self.on.clicked.connect(self.LedOn)           
      self.show()

   def openport(self):
      com=self.comport.text()      
      self.s=serial.Serial(com,9600)

   def closeport(self):
      self.s.close()

   def LedOn(self):
      self.s.write(b'H')
      

   def LedOff(self):
      self.s.write(b'L')
      
app=QtWidgets.QApplication(sys.argv)
GUI=window()

sys.exit(app.exec_()) #  Run your application's event loop (or main loop)
