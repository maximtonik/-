# Form implementation generated from reading ui file 'level_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        MainWindow1.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 140, 341, 361))
        self.label_2.setStyleSheet("background-color: rgba(255,255,255,200);\n"
"border: 1px solid rgba(255,255,255,70);\n"
"border-radius: 24px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 60, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255,255,255,200);\n"
"border: 1px solid rgba(255,255,255,70);\n"
"border-radius: 12px;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_27 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(20, 540, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color: rgba(255,255,255,200);\n"
"border: 1px solid rgba(255,255,255,70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,205,70);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,245,80);\n"
"}")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 380, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color: rgba(255,255,255,200);\n"
"border: 1px solid rgba(255,255,255,70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,205,70);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,245,80);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 280, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color: rgba(255,255,255,200);\n"
"border: 1px solid rgba(255,255,255,70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,205,70);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,245,80);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 180, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"color: black;\n"
"background-color: rgba(255,255,255,200);\n"
"border: 1px solid rgba(255,255,255,70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,205,70);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,245,80);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow1.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "Переливание"))
        self.label_3.setText(_translate("MainWindow1", "Выберите сложность уровней"))
        self.pushButton_27.setText(_translate("MainWindow1", "Меню"))
        self.pushButton_3.setText(_translate("MainWindow1", "Сложный"))
        self.pushButton_4.setText(_translate("MainWindow1", "Средний"))
        self.pushButton_5.setText(_translate("MainWindow1", "Легкий"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec())
