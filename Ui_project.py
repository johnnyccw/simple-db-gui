# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wei/Desktop/DBMS_project/project.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 914)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exe_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exe_btn.setGeometry(QtCore.QRect(670, 410, 91, 51))
        self.exe_btn.setObjectName("exe_btn")
        self.select_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_btn.setGeometry(QtCore.QRect(60, 30, 121, 41))
        self.select_btn.setObjectName("select_btn")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 490, 691, 371))
        self.groupBox.setObjectName("groupBox")
        self.output = QtWidgets.QTableWidget(self.groupBox)
        self.output.setGeometry(QtCore.QRect(30, 50, 631, 291))
        self.output.setRowCount(0)
        self.output.setColumnCount(0)
        self.output.setObjectName("output")
        self.output.horizontalHeader().setVisible(True)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 200, 581, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.input = QtWidgets.QTextEdit(self.groupBox_2)
        self.input.setGeometry(QtCore.QRect(30, 50, 521, 201))
        self.input.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input.setFrameShadow(QtWidgets.QFrame.Plain)
        self.input.setObjectName("input")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(670, 334, 91, 51))
        self.clear_btn.setObjectName("clear_btn")
        self.where_btn = QtWidgets.QPushButton(self.centralwidget)
        self.where_btn.setGeometry(QtCore.QRect(200, 30, 121, 41))
        self.where_btn.setObjectName("where_btn")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(340, 30, 121, 41))
        self.delete_btn.setObjectName("delete_btn")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(620, 30, 121, 41))
        self.update_btn.setObjectName("update_btn")
        self.insert_btn = QtWidgets.QPushButton(self.centralwidget)
        self.insert_btn.setGeometry(QtCore.QRect(480, 30, 121, 41))
        self.insert_btn.setObjectName("insert_btn")
        self.in_btn = QtWidgets.QPushButton(self.centralwidget)
        self.in_btn.setGeometry(QtCore.QRect(60, 80, 121, 41))
        self.in_btn.setObjectName("in_btn")
        self.not_in_btn = QtWidgets.QPushButton(self.centralwidget)
        self.not_in_btn.setGeometry(QtCore.QRect(200, 80, 121, 41))
        self.not_in_btn.setObjectName("not_in_btn")
        self.exists_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exists_btn.setGeometry(QtCore.QRect(340, 80, 121, 41))
        self.exists_btn.setObjectName("exists_btn")
        self.not_exists_btn = QtWidgets.QPushButton(self.centralwidget)
        self.not_exists_btn.setGeometry(QtCore.QRect(480, 80, 121, 41))
        self.not_exists_btn.setObjectName("not_exists_btn")
        self.count_btn = QtWidgets.QPushButton(self.centralwidget)
        self.count_btn.setGeometry(QtCore.QRect(620, 80, 121, 41))
        self.count_btn.setObjectName("count_btn")
        self.sum_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sum_btn.setGeometry(QtCore.QRect(60, 130, 121, 41))
        self.sum_btn.setObjectName("sum_btn")
        self.max_btn = QtWidgets.QPushButton(self.centralwidget)
        self.max_btn.setGeometry(QtCore.QRect(200, 130, 121, 41))
        self.max_btn.setObjectName("max_btn")
        self.min_btn = QtWidgets.QPushButton(self.centralwidget)
        self.min_btn.setGeometry(QtCore.QRect(340, 130, 121, 41))
        self.min_btn.setObjectName("min_btn")
        self.avg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.avg_btn.setGeometry(QtCore.QRect(480, 130, 121, 41))
        self.avg_btn.setObjectName("avg_btn")
        self.having_btn = QtWidgets.QPushButton(self.centralwidget)
        self.having_btn.setGeometry(QtCore.QRect(620, 130, 121, 41))
        self.having_btn.setObjectName("having_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exe_btn.setText(_translate("MainWindow", "excute"))
        self.select_btn.setText(_translate("MainWindow", "select"))
        self.groupBox.setTitle(_translate("MainWindow", "Result"))
        self.groupBox_2.setTitle(_translate("MainWindow", "SQL Command"))
        self.input.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'PMingLiU\'; font-size:9pt;\"><br /></p></body></html>"))
        self.clear_btn.setText(_translate("MainWindow", "clear"))
        self.where_btn.setText(_translate("MainWindow", "where"))
        self.delete_btn.setText(_translate("MainWindow", "delete"))
        self.update_btn.setText(_translate("MainWindow", "update"))
        self.insert_btn.setText(_translate("MainWindow", "insert"))
        self.in_btn.setText(_translate("MainWindow", "in"))
        self.not_in_btn.setText(_translate("MainWindow", "not in"))
        self.exists_btn.setText(_translate("MainWindow", "exists"))
        self.not_exists_btn.setText(_translate("MainWindow", "not exists"))
        self.count_btn.setText(_translate("MainWindow", "count"))
        self.sum_btn.setText(_translate("MainWindow", "sum"))
        self.max_btn.setText(_translate("MainWindow", "max"))
        self.min_btn.setText(_translate("MainWindow", "min"))
        self.avg_btn.setText(_translate("MainWindow", "avg"))
        self.having_btn.setText(_translate("MainWindow", "Having"))

