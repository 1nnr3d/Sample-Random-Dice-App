import sys
import random2
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtTest

dice1 = "images/1.png"
dice2 = "images/2.png"
dice3 = "images/3.png"
dice4 = "images/4.png"
dice5 = "images/5.png"
dice6 = "images/6.png"
gif = "images/dicerandom.gif"
windowIcon = "images/icon.svg"

fontBtn = QtGui.QFont("Sailar", 18)

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Dice")
        self.setWindowIcon(QtGui.QIcon(windowIcon))
        self.setFixedSize(600,600)
        self.main = QtWidgets.QWidget()

        self.img = QtWidgets.QLabel()
        self.gif = QtGui.QMovie(gif)
        self.img.setMovie(self.gif)
        self.img.setHidden(True)

        self.result = QtWidgets.QLabel()
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result1 = QtWidgets.QLabel()
        self.result1.setAlignment(QtCore.Qt.AlignCenter)

        self.onediceBtn = QtWidgets.QPushButton("One Dice")
        self.onediceBtn.setFont(fontBtn)
        self.onediceBtn.clicked.connect(self.oneDice)
        self.twodiceBtn = QtWidgets.QPushButton("Two Dice")
        self.twodiceBtn.setFont(fontBtn)
        self.twodiceBtn.clicked.connect(self.twoDice)
        self.off = QtWidgets.QPushButton("Reset")
        self.off.setFont(fontBtn)
        self.off.clicked.connect(self.reseT)
        self.off.setHidden(True)

        horizontal = QtWidgets.QHBoxLayout()
        vertical = QtWidgets.QVBoxLayout()

        horizontal1 = QtWidgets.QHBoxLayout()

        horizontal1.addStretch()
        horizontal1.addWidget(self.result)
        horizontal1.addWidget(self.result1)
        horizontal1.addStretch()

        vertical.addStretch()
        vertical.addStretch()
        vertical.addWidget(self.img)
        vertical.addLayout(horizontal1)
        vertical.addStretch()
        vertical.addWidget(self.onediceBtn)
        vertical.addWidget(self.twodiceBtn)
        vertical.addWidget(self.off)
        vertical.addStretch()
        vertical.addStretch()

        horizontal.addStretch()
        horizontal.addLayout(vertical)
        horizontal.addStretch()
        
        self.main.setLayout(horizontal)
        self.setCentralWidget(self.main)
        self.show()
    def oneDice(self):
        self.result.setPixmap(QtGui.QPixmap(""))
        self.result1.setPixmap(QtGui.QPixmap(""))
        self.off.setHidden(True)
        
        self.img.setHidden(False)
        self.gif.start()

        self.diceS = [dice1,dice2,dice3,dice4,dice5,dice6]
        self.dice = random2.choice(self.diceS)

        QtTest.QTest.qWait(5000)

        self.img.setHidden(True)
        self.gif.stop()

        self.result.setPixmap(QtGui.QPixmap(self.dice))
        self.off.setHidden(False)
    def twoDice(self):
        self.result.setPixmap(QtGui.QPixmap(""))
        self.result1.setPixmap(QtGui.QPixmap(""))
        self.off.setHidden(True)
        
        self.img.setHidden(False)
        self.gif.start()

        self.diceS = [dice1,dice2,dice3,dice4,dice5,dice6]
        self.dice1 = random2.choice(self.diceS)
        self.dice2 = random2.choice(self.diceS)

        QtTest.QTest.qWait(5000)

        self.img.setHidden(True)
        self.gif.stop()

        self.result.setPixmap(QtGui.QPixmap(self.dice1))
        self.result1.setPixmap(QtGui.QPixmap(self.dice2))
        self.off.setHidden(False)
    def reseT(self):
        self.result.setPixmap(QtGui.QPixmap(""))
        self.result1.setPixmap(QtGui.QPixmap(""))
        self.off.setHidden(True)
stylesheet = """
QWidget{
    background-color: black;
}
QPushButton{
    color: white;
    border: 2px solid white;
    border-radius: 5px;
    background-color: black;
}
QPushButton:hover{
    color: black;
    border: 2.5px solid black;
    border-radius: 3px;
    background-color: white;
}
"""
app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(stylesheet)
mainw = mainWindow()
sys.exit(app.exec_())

