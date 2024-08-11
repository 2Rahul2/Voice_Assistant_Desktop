# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 579)
        MainWindow.setStyleSheet("background-color:rgb(225, 223, 216);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 20))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame.setBaseSize(QtCore.QSize(0, 0))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(2, 7, 2, 7)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.about_button = QtWidgets.QPushButton(self.frame)
        self.about_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.about_button.setFont(font)
        self.about_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about_button.setStyleSheet("QPushButton {\n"
"    background-color: #CDB4DB;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"    border: none;\n"
"    border-radius:  5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-bottom:3px solid black;\n"
"}")
        self.about_button.setObjectName("about_button")
        self.horizontalLayout.addWidget(self.about_button)
        self.setting_button = QtWidgets.QPushButton(self.frame)
        self.setting_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.setting_button.setFont(font)
        self.setting_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setting_button.setStyleSheet("QPushButton {\n"
"    background-color: #FFC8DD;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"    border: none;\n"
"\n"
"    border-radius:  5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-bottom:3px solid black;\n"
"}")
        self.setting_button.setCheckable(False)
        self.setting_button.setObjectName("setting_button")
        self.horizontalLayout.addWidget(self.setting_button)
        self.chat_button = QtWidgets.QPushButton(self.frame)
        self.chat_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chat_button.setFont(font)
        self.chat_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chat_button.setStyleSheet("QPushButton {\n"
"    background-color: #A2D2FF;\n"
"    color: #252b30;\n"
"    font-size: 10pt;\n"
"    border: none;\n"
"\n"
"    border-radius:  5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-bottom:3px solid black;\n"
"}")
        self.chat_button.setObjectName("chat_button")
        self.horizontalLayout.addWidget(self.chat_button)
        self.how_button = QtWidgets.QPushButton(self.frame)
        self.how_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.how_button.setFont(font)
        self.how_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.how_button.setStyleSheet("QPushButton {\n"
"    background-color: #FFAFCC;\n"
"    color: #252b30;\n"
"    font-size: 11pt;\n"
"    border: none;\n"
"\n"
"    border-radius:  5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-bottom: 3px solid black ;\n"
"}")
        self.how_button.setObjectName("how_button")
        self.horizontalLayout.addWidget(self.how_button)
        self.extras_button = QtWidgets.QPushButton(self.frame)
        self.extras_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.extras_button.setFont(font)
        self.extras_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.extras_button.setStyleSheet("QPushButton {\n"
"    background-color: #CDB4DB;\n"
"    color: black;\n"
"    font-size: 10pt;\n"
"    border: none;\n"
"    border-radius:  5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-bottom:3px solid black;\n"
"}")
        self.extras_button.setObjectName("extras_button")
        self.horizontalLayout.addWidget(self.extras_button)
        self.verticalLayout.addWidget(self.frame)
        self.placeholderWidget = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeholderWidget.sizePolicy().hasHeightForWidth())
        self.placeholderWidget.setSizePolicy(sizePolicy)
        self.placeholderWidget.setStyleSheet("")
        self.placeholderWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.placeholderWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.placeholderWidget.setObjectName("placeholderWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.placeholderWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addWidget(self.placeholderWidget)
        self.music_animation = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.music_animation.sizePolicy().hasHeightForWidth())
        self.music_animation.setSizePolicy(sizePolicy)
        self.music_animation.setMinimumSize(QtCore.QSize(0, 40))
        self.music_animation.setObjectName("music_animation")
        self.music_animation_2 = QtWidgets.QVBoxLayout(self.music_animation)
        self.music_animation_2.setContentsMargins(-1, 0, -1, 5)
        self.music_animation_2.setObjectName("music_animation_2")
        self.music_widget = QtWidgets.QWidget(self.music_animation)
        self.music_widget.setMinimumSize(QtCore.QSize(180, 35))
        self.music_widget.setObjectName("music_widget")
        self.music_widget_2 = QtWidgets.QVBoxLayout(self.music_widget)
        self.music_widget_2.setContentsMargins(0, 0, 0, 0)
        self.music_widget_2.setSpacing(0)
        self.music_widget_2.setObjectName("music_widget_2")
        self.music_animation_2.addWidget(self.music_widget, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.music_animation)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.about_button.setText(_translate("MainWindow", "About"))
        self.setting_button.setText(_translate("MainWindow", "Settings"))
        self.chat_button.setText(_translate("MainWindow", "Chats"))
        self.how_button.setText(_translate("MainWindow", "How it woks?"))
        self.extras_button.setText(_translate("MainWindow", "Extras"))
