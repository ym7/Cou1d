from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox
import sys
from PyQt5.QtGui import QIcon


class Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        # menu = self.menuBar()
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Demo')
        self.setWindowIcon(QIcon('iweb.jpg'))
        self.buttonMaker()
        self.show()

    def buttonMaker(self):
        btn = QPushButton('确定',self)
        btn.move(50,50)

        btn2 = QPushButton('取消',self)
        btn2.move(50,100)

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'消息','You want to quit?',QMessageBox.Yes | QMessageBox.No | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec_())



'''
# app = QApplication(sys.argv)
# w = QWidget()
# w.resize(250,150)
# # w.move(300,300)
# w.setWindowTitle('Demo_One')
# w.show()
# sys.exit(app.exec_())
'''

