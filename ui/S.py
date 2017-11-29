import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLineEdit,
                             QLabel,QGridLayout,QMessageBox)
from PyQt5.QtGui import QFont
from stockxsdk import Stockx




class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        
        self.btn = QPushButton('Check',self)
        title = QLabel('EMail')
        password = QLabel('Password')
        self.titleEdit = QLineEdit()
        self.passwordEdit = QLineEdit()
        
        grid = QGridLayout()
        grid.setSpacing(0)

        grid.addWidget(title, 1, 0)
        grid.addWidget(self.titleEdit, 1, 1)

        grid.addWidget(password, 2, 0)
        grid.addWidget(self.passwordEdit, 2, 1)

        grid.addWidget(self.btn, 3, 0)
        
        self.setLayout(grid)
        self.setGeometry(150, 150, 250, 150)
        self.setWindowTitle('StockX Checker by J3sseC0d3R')
        self.show()
        self.btn.clicked.connect(self.buttonClicked)
        
    def buttonClicked(self):
        
        logged_in = None 
        stockx = Stockx()
        email = self.titleEdit.text()
    
        password = self.passwordEdit.text()
        print(password,email)
        try:
            logged_in = stockx.authenticate(email, password)
        except ValueError:
            QMessageBox.about(self, "Result", "Account not valid")
        else:
            logged_in = True
        print(logged_in)
        if(logged_in == True):

            QMessageBox.about(self, "Result", "Account is valid")
            
        else:
            QMessageBox.about(self, "Result", "Account not valid")
            logged_in = False

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())