import sys
import random
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt

form_class=loadUiType("Sudoku.ui")[0]

class SudokuUI(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        global AVal, ButtonList

        ButtonList = [[self.A00, self.A01, self.A02, self.A03, self.A04, self.A05, self.A06, self.A07, self.A08],
                      [self.A10, self.A11, self.A12, self.A13, self.A14, self.A15, self.A16, self.A17, self.A18],
                      [self.A20, self.A21, self.A22, self.A23, self.A24, self.A25, self.A26, self.A27, self.A28],
                      [self.A30, self.A31, self.A32, self.A33, self.A34, self.A35, self.A36, self.A37, self.A38],
                      [self.A40, self.A41, self.A42, self.A43, self.A44, self.A45, self.A46, self.A47, self.A48],
                      [self.A50, self.A51, self.A52, self.A53, self.A54, self.A55, self.A56, self.A57, self.A58],
                      [self.A60, self.A61, self.A62, self.A63, self.A64, self.A65, self.A66, self.A67, self.A68],
                      [self.A70, self.A71, self.A72, self.A73, self.A74, self.A75, self.A76, self.A77, self.A78],
                      [self.A80, self.A81, self.A82, self.A83, self.A84, self.A85, self.A86, self.A87, self.A88]]

        #숫자 버튼에 NumClick함수 연결하기
        for i in range(0,9):
            for number in ButtonList[i]:
                number.clicked.connect(self.NumClick)

        #버튼 화면에 구성하기
        AVal=[]
        for i in range(0,9):
            temp=[]
            for j in range(0,9):
                temp.append(str(ButtonList[i][j].text()))
            AVal.append(temp)

        self.ShuffleClick()
        self.ShuffleButton.clicked.connect(self.ShuffleClick)
        self.FinishButton.clicked.connect(self.CompleteTestClick)

    def ShuffleClick(self):
        random19=list(range(1,10))
        random.shuffle(random19)

        for i in range(0,9):
            for j in range(0,9):
                ButtonList[i][j].setText(str(random19[int(AVal[i][j])-1]))


        #pEdit에 있는 확률보다 큰 경우에는 빈칸으로 만든다.
        for i in range(0,9):
            for j in range(0,9):
                if random.random() > float(self.pEdit.text()):
                    ButtonList[i][j].setText("")

    def NumClick(self):
         global XLoc, YLoc
         for i in range(0,9):
             for j in range(0,9):
                if self.sender() == ButtonList[i][j]:
                    # i, j는 행렬의 위치
                    XLoc=i
                    YLoc=j

    #"키보드 자판"을 눌렀을 때 작동한다
    def keyPressEvent(self, event):
        if type(event) == QKeyEvent:
            if event.key() == Qt.Key_1 :
                ButtonList[XLoc][YLoc].setText("1")
            elif event.key() == Qt.Key_2 :
                ButtonList[XLoc][YLoc].setText("2")
            elif event.key() == Qt.Key_3 :
                ButtonList[XLoc][YLoc].setText("3")
            elif event.key() == Qt.Key_4 :
                ButtonList[XLoc][YLoc].setText("4")
            elif event.key() == Qt.Key_5 :
                ButtonList[XLoc][YLoc].setText("5")
            elif event.key() == Qt.Key_6 :
                ButtonList[XLoc][YLoc].setText("6")
            elif event.key() == Qt.Key_7 :
                ButtonList[XLoc][YLoc].setText("7")
            elif event.key() == Qt.Key_8 :
                ButtonList[XLoc][YLoc].setText("8")
            elif event.key() == Qt.Key_9 :
                ButtonList[XLoc][YLoc].setText("9")
            else:
                print ("Error")
        ButtonList[XLoc][YLoc].setStyleSheet('QPushButton {color: red;}')

    def CompleteTestClick(self):
        err=0
        self.resEdit.setText("")
        for i in range(0,9):
            for j in range(0,9):
                AVal[i][j]=ButtonList[i][j].text()

 # Row Test
        for i in range(0,9):
            temp=[]
            for j in range(0,9):
                temp.append(AVal[i][j])
            print(len(set(temp)))
            if len(set(temp)) != 9:
                self.resEdit.setText(str(i+1)+"'row Error")
                err=1
                break

# Col Test
        for j in range(0,9):
            temp=[]
            for i in range(0,9):
                temp.append(AVal[i][j])
            if len(set(temp)) != 9:
                self.resEdit.setText(str(i+1)+"'column Error")
                err=1
                break

# 9 Area Test
        index=[0,3,6]
        for i in index:
            for j in index:
                temp=[]
                for k in range(0,3):
                    temp.append(AVal[i][j+k])
                    temp.append(AVal[i+1][j+k])
                    temp.append(AVal[i+2][j+k])
                print(temp)
                if len(set(temp)) != 9:
                    self.resEdit.setText(str(i)+", "+ str(j)+ "'Error")
                    err=1
                    break

        if err==0:
            self.resEdit.setText("Congratulation!")

app=QApplication(sys.argv)
myWindow=SudokuUI(None)
myWindow.show()
app.exec_()


