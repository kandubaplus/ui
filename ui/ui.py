# -*- coding: utf-8 -*-
import vk_api
import sys
import time
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLineEdit,
                             QLabel,QGridLayout,QMessageBox)
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(477, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 10, 71, 21))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 40, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.ID = QtWidgets.QLineEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(210, 150, 113, 20))
        self.ID.setObjectName("ID")
        self.tex = QtWidgets.QTextEdit(self.centralwidget)
        self.tex.setGeometry(QtCore.QRect(10, 140, 161, 81))
        self.tex.setObjectName("text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 120, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 130, 21, 20))
        self.label_3.setObjectName("label_3")
        self.antig = QtWidgets.QLineEdit(self.centralwidget)
        self.antig.setGeometry(QtCore.QRect(210, 190, 113, 20))
        self.antig.setObjectName("antig")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 170, 51, 16))
        self.label_4.setObjectName("label_4")
        self.but_send = QtWidgets.QPushButton(self.centralwidget)
        self.but_send.setGeometry(QtCore.QRect(320, 150, 41, 21))
        self.but_send.setObjectName("but_send")
        self.ID_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.ID_2.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.ID_2.setObjectName("ID_2")
        self.ID_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.ID_3.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.ID_3.setObjectName("ID_3")
        self.but_auth_2 = QtWidgets.QPushButton(self.centralwidget)
        self.but_auth_2.setGeometry(QtCore.QRect(90, 70, 75, 23))
        self.but_auth_2.setObjectName("but_auth_2")
        self.but_select_2 = QtWidgets.QPushButton(self.centralwidget)
        self.but_select_2.setGeometry(QtCore.QRect(280, 40, 71, 23))
        self.but_select_2.setObjectName("but_select_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 260, 461, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 239, 51, 21))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 477, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Spam!"))
        self.label.setText(_translate("MainWindow", "Тext:"))
        self.label_2.setText(_translate("MainWindow", "login:password"))
        #self.but_auth.setText(_translate("MainWindow", "Auth"))
        self.label_3.setText(_translate("MainWindow", "ID:"))
        self.label_4.setText(_translate("MainWindow", "Antigate:"))
        self.but_send.setText(_translate("MainWindow", "Send"))
        self.but_auth_2.setText(_translate("MainWindow", "Add"))
        self.but_select_2.setText(_translate("MainWindow", "Stop"))
        self.label_5.setText(_translate("MainWindow", "Log:"))

class main1(Ui_MainWindow):
    
    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        self.but_auth_2.clicked.connect(self.logins)
        self.but_send.clicked.connect(self.send)
        self.pushButton.clicked.connect(self.spam)
           
    def logins(self):
        log = self.ID_2.text()
        passw = self.ID_3.text()
        e1.auth1(log,passw)
        
    def send(self):
        status = 0
        te = self.tex.toPlainText()
        usrid = self.ID.text()
        e1.spam_friend(te,usrid)

    def spam(self):
        status = 1
        te = self.tex.toPlainText()
        usrid = self.ID.text()
        e1.spam_friends(te)

logi =[]
passwor = [] 

class spamer:
    
    def auth1(self,login, password):
        
        vk_session = vk_api.VkApi(login, password)
        try:
            vk_session.auth()
            ui.textBrowser.append(login+' Autorized')
        except vk_api.AuthError as error_msg:
            ui.textBrowser.append('Wrong login or password')
            return 
        logi.append(login)
        passwor.append(password)
        vk = vk_session.get_api()
        ui.comboBox.addItem(login)

    def auth(self,login, password):
     
        vk_session = vk_api.VkApi(login, password)
        try:
            vk_session.auth()        
        except vk_api.AuthError as error_msg:
            ui.textBrowser.append('Wrong login or password')
            return   
        vk = vk_session.get_api()
        ui.comboBox.addItem(login)

    def spam_friend(self,text,usr):
        i = ui.comboBox.currentIndex()
        vk_session = vk_api.VkApi(logi[i], passwor[i])
        try:
            vk_session.auth()        
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return
        vk = vk_session.get_api() 
        self.auth(logi[i],passwor[i])  
        vk.messages.send(user_id = usr,message=text)
        ui.textBrowser.append('Send message'+usr)

    def spam_friends(self,text):
        i = ui.comboBox.currentIndex()
        vk_session = vk_api.VkApi(logi[i], passwor[i])
        try:
            vk_session.auth()
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return
        vk = vk_session.get_api() 
        self.auth(logi[i],passwor[i])
        with vk_api.VkRequestsPool(vk_session) as pool:
            friends = pool.method('friends.get')
        item = friends.result.get('items')
        for k in range(len(item)):
            time.sleep(5)
            if ui.but_select_2.isChecked():
                break
            vk.messages.send(user_id = item[k],message=text)
            kk = str(item[k])
            ui.textBrowser.append('Send text to a friend '+kk+' whis account account '+logi[i])
            time.sleep(12)
 
if __name__ == '__main__':   
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = main1(MainWindow)
    e1 = spamer()
    MainWindow.show()
    sys.exit(app.exec_())



