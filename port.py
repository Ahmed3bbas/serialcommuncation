# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'port.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 444)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ports_box = QtWidgets.QComboBox(self.centralwidget)
        self.ports_box.setGeometry(QtCore.QRect(50, 40, 201, 22))
        self.ports_box.setObjectName("ports_box")
        self.refersh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refersh_btn.setGeometry(QtCore.QRect(70, 100, 75, 23))
        self.refersh_btn.setObjectName("refersh_btn")
        self.connect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.connect_btn.setGeometry(QtCore.QRect(210, 100, 75, 23))
        self.connect_btn.setObjectName("connect_btn")
        self.disconnect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.disconnect_btn.setGeometry(QtCore.QRect(350, 100, 75, 23))
        self.disconnect_btn.setObjectName("disconnect_btn")
        self.state = QtWidgets.QLabel(self.centralwidget)
        self.state.setGeometry(QtCore.QRect(340, 40, 71, 20))
        self.state.setObjectName("state")
        self.text_box = QtWidgets.QLineEdit(self.centralwidget)
        self.text_box.setGeometry(QtCore.QRect(40, 150, 400, 30))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.text_box.setFont(font)
        self.text_box.setText("")
        self.text_box.setObjectName("text_box")
        self.send_btn = QtWidgets.QPushButton(self.centralwidget)
        self.send_btn.setGeometry(QtCore.QRect(210, 200, 75, 23))
        self.send_btn.setObjectName("send_btn")
        self.read_box = QtWidgets.QLineEdit(self.centralwidget)
        self.read_box.setGeometry(QtCore.QRect(40, 260, 400, 30))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setItalic(True)
        self.read_box.setFont(font)
        self.read_box.setReadOnly(True)
        self.read_box.setObjectName("read_box")
        self.read_btn = QtWidgets.QPushButton(self.centralwidget)
        self.read_btn.setGeometry(QtCore.QRect(210, 320, 75, 23))
        self.read_btn.setObjectName("read_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial communication with python"))
        self.refersh_btn.setText(_translate("MainWindow", "Refresh"))
        self.connect_btn.setText(_translate("MainWindow", "Connect"))
        self.disconnect_btn.setText(_translate("MainWindow", "Disconnect"))
        self.state.setText(_translate("MainWindow", "Disconnected"))
        self.text_box.setPlaceholderText(_translate("MainWindow", "Data Sending"))
        self.send_btn.setText(_translate("MainWindow", "send"))
        self.read_box.setPlaceholderText(_translate("MainWindow", "Data Reading"))
        self.read_btn.setText(_translate("MainWindow", "Read"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

