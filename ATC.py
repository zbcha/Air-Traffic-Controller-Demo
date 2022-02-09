from PyQt5 import QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QRect, Qt
from PyQt5.QtGui import QPainter, QPen
from random import random
import math
import sys

PI = 3.1415

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "ACT System"
        self.top = 100
        self.left = 100
        self.width = 1000
        self.height = 600

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.button = QPushButton("To Lane#1", self)
        self.button.resize(100,32)
        self.button.move(30, 30)
        self.button.clicked.connect(self.animation_b1)
        
        self.button2 = QPushButton("To Lane#2", self)
        self.button2.resize(100,32)
        self.button2.move(30, 70)
        self.button2.clicked.connect(self.animation_b2)
        
        self.button3 = QPushButton("Hold", self)
        self.button3.resize(100,32)
        self.button3.move(30, 110)
        self.button3.clicked.connect(self.animation_b3)
        
        self.button3 = QPushButton("Restart", self)
        self.button3.resize(100,32)
        self.button3.move(30, 150)
        self.button3.clicked.connect(self.animation)
        
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText("#1")
        self.l1.move(580, 230)
        
        self.l2 = QtWidgets.QLabel(self)
        self.l2.setText("#2")
        self.l2.move(640, 230)
        
        self.hold = False
        self.frame = QFrame(self)
        self.frame.setFrameStyle(QFrame.Panel)

        self.animation()
        self.show()
        
    def paintEvent(self,e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
        painter.drawEllipse(420, 100, 400, 400)
        painter.drawRect(580,260,20,80)
        painter.drawRect(640,260,20,80)
        
    def animation(self):
        self.hold = False
        self.r = 200
        self.theta = random() * 2 * PI
        self.x = 620 + self.r * math.cos(self.theta)
        self.y = 300 + self.r * math.sin(self.theta)
        
        
        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(10000)
        self.anim.setStartValue(QRect(self.x, self.y, 5, 5))
        self.anim.setEndValue(QRect(588, 340, 5, 5))
        
        self.anim2 = QPropertyAnimation(self.frame, b"geometry")
        self.anim2.setDuration(10000*(80/200))
        self.anim2.setStartValue(QRect(588, 340, 5, 5))
        self.anim2.setEndValue(QRect(588, 260, 5, 5))
        
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim2)
        print(self.frame.pos())
        self.anim_group.start()
        
    def animation_b1(self):
        self.hold = False
        self.x = self.frame.pos().x()
        self.y = self.frame.pos().y()
        self.distance = math.sqrt((588-self.x)**2 + (340-self.y)**2)
        
        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(10000*(self.distance/200))
        self.anim.setStartValue(QRect(self.x, self.y, 5, 5))
        self.anim.setEndValue(QRect(588, 340, 5, 5))
        
        self.anim2 = QPropertyAnimation(self.frame, b"geometry")
        self.anim2.setDuration(10000*(80/200))
        self.anim2.setStartValue(QRect(588, 340, 5, 5))
        self.anim2.setEndValue(QRect(588, 260, 5, 5))
        
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim2)
        self.anim_group.start()
        
    def animation_b2(self):
        self.hold = False
        self.x = self.frame.pos().x()
        self.y = self.frame.pos().y()
        self.distance = math.sqrt((648-self.x)**2 + (340-self.y)**2)
        
        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(10000*(self.distance/200))
        self.anim.setStartValue(QRect(self.x, self.y, 5, 5))
        self.anim.setEndValue(QRect(648, 340, 5, 5))
        
        self.anim2 = QPropertyAnimation(self.frame, b"geometry")
        self.anim2.setDuration(10000*(80/200))
        self.anim2.setStartValue(QRect(648, 340, 5, 5))
        self.anim2.setEndValue(QRect(648, 260, 5, 5))
        
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim2)
        self.anim_group.start()
        
    def animation_b3(self):
        self.angle = 1
        self.hold = True
        self.x = self.frame.pos().x()
        self.y = self.frame.pos().y()
        
        self.anim_group = QSequentialAnimationGroup()
        
        #Dummy Animation 
        for i in range(80):
            self.anim = QPropertyAnimation(self.frame, b"geometry")
            self.anim.setDuration(400)
            self.anim.setStartValue(QRect(self.x, self.y, 5, 5))
            self.anim.setEndValue(QRect(self.x+math.sin(self.angle)*10, 
                                        self.y+math.cos(self.angle)*10, 5, 5))
            self.anim_group.addAnimation(self.anim)
            self.x = self.x+math.sin(self.angle)*10
            self.y = self.y+math.cos(self.angle)*10
            self.angle += 0.3
            
        self.anim_group.start()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())