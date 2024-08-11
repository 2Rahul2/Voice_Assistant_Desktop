# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(718, 486)
        Form.setStyleSheet("padding:0;\n"
"background-color:rgb(225, 223, 216);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#F26419;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.save_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setMinimumSize(QtCore.QSize(30, 40))
        self.save_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_button.setStyleSheet("QPushButton {\n"
"    font-size: 14px;\n"
" \n"
"    background-color:#9D4EDD;\n"
"    border:none;\n"
"    padding-left:12px;\n"
"    padding-right:12px;\n"
"    color:black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#C77DFF;\n"
"}")
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setStyleSheet("background-color:rgb(225, 223, 216);\n"
"border:none;")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 675, 1182))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(-1, 11, -1, 11)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 120))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 120))
        self.widget.setStyleSheet("border: 1px solid black;\n"
"background-color:#F1FFE7;\n"
"border-radius:10px")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(40, 10))
        self.label.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;\n"
"color:#2F4858;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path_label = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_label.sizePolicy().hasHeightForWidth())
        self.path_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.path_label.setFont(font)
        self.path_label.setStyleSheet("background-color:#CDB4DB;\n"
"color:black;\n"
"padding-left:10px;")
        self.path_label.setObjectName("path_label")
        self.horizontalLayout.addWidget(self.path_label)
        self.select_button = QtWidgets.QPushButton(self.widget_4)
        self.select_button.setMaximumSize(QtCore.QSize(120, 40))
        self.select_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_button.setStyleSheet("QPushButton {\n"
"    font-size: 12px;\n"
"    transition: font-size 0.8s ease;\n"
"    background-color:#A2D2FF;\n"
"    border:none;\n"
"    color:black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 14px;\n"
"}")
        self.select_button.setObjectName("select_button")
        self.horizontalLayout.addWidget(self.select_button)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 120))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.widget_2.setStyleSheet("border: 1px solid black;\n"
"background-color:#F1FFE7;\n"
"border-radius:10px")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMinimumSize(QtCore.QSize(25, 10))
        self.label_3.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:none;\n"
"color:#2F4858;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wake_word_label = QtWidgets.QLineEdit(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wake_word_label.sizePolicy().hasHeightForWidth())
        self.wake_word_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wake_word_label.setFont(font)
        self.wake_word_label.setStyleSheet("background-color:#CDB4DB;\n"
"color:black;\n"
"padding-left:10px;")
        self.wake_word_label.setObjectName("wake_word_label")
        self.horizontalLayout_2.addWidget(self.wake_word_label)
        self.wake_button = QtWidgets.QPushButton(self.widget_5)
        self.wake_button.setMaximumSize(QtCore.QSize(120, 40))
        self.wake_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wake_button.setStyleSheet("QPushButton {\n"
"    font-size: 12px;\n"
"    background-color:#A2D2FF;\n"
"    border:none;\n"
"    color:black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 14px;\n"
"}")
        self.wake_button.setObjectName("wake_button")
        self.horizontalLayout_2.addWidget(self.wake_button)
        self.default_wake_button = QtWidgets.QPushButton(self.widget_5)
        self.default_wake_button.setMaximumSize(QtCore.QSize(120, 40))
        self.default_wake_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.default_wake_button.setStyleSheet("QPushButton {\n"
"    font-size: 12px;\n"
"    background-color:#A2D2FF;\n"
"    border:none;\n"
"    color:black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 14px;\n"
"}")
        self.default_wake_button.setObjectName("default_wake_button")
        self.horizontalLayout_2.addWidget(self.default_wake_button)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 120))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.widget_3.setStyleSheet("border: 1px solid black;\n"
"background-color:#F1FFE7;\n"
"border-radius:10px")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:none;\n"
"color:#2F4858;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setStyleSheet("margin:0px;")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tray_check_box = QtWidgets.QCheckBox(self.widget_6)
        self.tray_check_box.setStyleSheet("border:none;\n"
"font-size:10pt;\n"
"background-color:#CDB4DB;\n"
"color:black;\n"
"padding:6px;")
        self.tray_check_box.setIconSize(QtCore.QSize(25, 25))
        self.tray_check_box.setObjectName("tray_check_box")
        self.horizontalLayout_3.addWidget(self.tray_check_box)
        self.verticalLayout_4.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 120))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 120))
        self.widget_7.setStyleSheet("border: 1px solid black;\n"
"background-color:#F1FFE7;\n"
"border-radius:10px")
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget_7)
        self.label_6.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border:none;\n"
"color:#2F4858;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.audio_device = QtWidgets.QComboBox(self.widget_7)
        self.audio_device.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.audio_device.setFont(font)
        self.audio_device.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.audio_device.setStyleSheet("border:none;\n"
"font-size:10pt;\n"
"background-color:#CDB4DB;\n"
"color:black;\n"
"padding:6px;")
        self.audio_device.setEditable(False)
        self.audio_device.setObjectName("audio_device")
        self.audio_device.addItem("")
        self.audio_device.addItem("")
        self.audio_device.addItem("")
        self.audio_device.addItem("")
        self.verticalLayout_5.addWidget(self.audio_device)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 600))
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 800))
        self.widget_8.setStyleSheet("border: 1px solid black;\n"
"background-color:#F1FFE7;\n"
"border-radius:10px")
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:none;\n"
"color:#2F4858;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.label_7 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border:none;\n"
"color:#2F4858;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.widget_9 = QtWidgets.QWidget(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 150))
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_10 = QtWidgets.QWidget(self.widget_9)
        self.widget_10.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_10.setStyleSheet("background-color:rgb(225, 223, 216);\n"
"border:none;")
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.day_combo = QtWidgets.QComboBox(self.widget_10)
        self.day_combo.setStyleSheet("border:none;\n"
"font-size:10pt;\n"
"background-color:#CDB4DB;\n"
"color:black;\n"
"padding:6px;")
        self.day_combo.setDuplicatesEnabled(False)
        self.day_combo.setObjectName("day_combo")
        self.day_combo.addItem("")
        self.day_combo.addItem("")
        self.day_combo.addItem("")
        self.day_combo.addItem("")
        self.day_combo.addItem("")
        self.day_combo.addItem("")
        self.day_combo.addItem("")
        self.horizontalLayout_4.addWidget(self.day_combo)
        self.day_time = QtWidgets.QTimeEdit(self.widget_10)
        self.day_time.setStyleSheet("border:none;\n"
"font-size:10pt;\n"
"background-color:#CDB4DB;\n"
"color:black;\n"
"padding:6px;")
        self.day_time.setObjectName("day_time")
        self.horizontalLayout_4.addWidget(self.day_time)
        self.day_text = QtWidgets.QTextEdit(self.widget_10)
        self.day_text.setStyleSheet("background-color:#CDB4DB;\n"
"color:black;\n"
"padding-left:10px;\n"
"border:1px solid #9D4EDD;")
        self.day_text.setObjectName("day_text")
        self.horizontalLayout_4.addWidget(self.day_text)
        self.verticalLayout_7.addWidget(self.widget_10)
        self.day_button = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.day_button.sizePolicy().hasHeightForWidth())
        self.day_button.setSizePolicy(sizePolicy)
        self.day_button.setMinimumSize(QtCore.QSize(0, 40))
        self.day_button.setMaximumSize(QtCore.QSize(120, 40))
        self.day_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.day_button.setStyleSheet("QPushButton {\n"
"    font-size: 14px;\n"
"    background-color:#A2D2FF;\n"
"    border:none;\n"
"    color:black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 16px;\n"
"}")
        self.day_button.setObjectName("day_button")
        self.verticalLayout_7.addWidget(self.day_button)
        self.verticalLayout_6.addWidget(self.widget_9)
        self.label_8 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border:none;\n"
"color:#2F4858;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.widget_11 = QtWidgets.QWidget(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_12 = QtWidgets.QWidget(self.widget_11)
        self.widget_12.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_12.setStyleSheet("background-color:rgb(225, 223, 216);\n"
"border:none;")
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.one_day_time = QtWidgets.QTimeEdit(self.widget_12)
        self.one_day_time.setStyleSheet("border:none;\n"
"font-size:10pt;\n"
"background-color:#CDB4DB;\n"
"color:black;\n"
"padding:6px;")
        self.one_day_time.setObjectName("one_day_time")
        self.horizontalLayout_5.addWidget(self.one_day_time)
        self.one_day_date = QtWidgets.QDateEdit(self.widget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.one_day_date.sizePolicy().hasHeightForWidth())
        self.one_day_date.setSizePolicy(sizePolicy)
        self.one_day_date.setMinimumSize(QtCore.QSize(150, 0))
        self.one_day_date.setStyleSheet("border:none;\n"
"font-size:10pt;\n"
"background-color:#CDB4DB;\n"
"color:black;\n"
"padding:6px;")
        self.one_day_date.setMinimumDate(QtCore.QDate(2024, 7, 14))
        self.one_day_date.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.one_day_date.setObjectName("one_day_date")
        self.horizontalLayout_5.addWidget(self.one_day_date)
        self.one_day_text = QtWidgets.QTextEdit(self.widget_12)
        self.one_day_text.setStyleSheet("background-color:#CDB4DB;\n"
"color:black;\n"
"padding-left:10px;\n"
"border:1px solid #9D4EDD;")
        self.one_day_text.setObjectName("one_day_text")
        self.horizontalLayout_5.addWidget(self.one_day_text)
        self.verticalLayout_8.addWidget(self.widget_12)
        self.one_day_button = QtWidgets.QPushButton(self.widget_11)
        self.one_day_button.setMinimumSize(QtCore.QSize(0, 40))
        self.one_day_button.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.one_day_button.setFont(font)
        self.one_day_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.one_day_button.setStyleSheet("QPushButton {\n"
"    font-size: 14px;\n"
"    background-color:#A2D2FF;\n"
"    border:none;\n"
"    color:black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 16px;\n"
"}")
        self.one_day_button.setObjectName("one_day_button")
        self.verticalLayout_8.addWidget(self.one_day_button)
        self.verticalLayout_6.addWidget(self.widget_11)
        self.label_9 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border:none;\n"
"color:#2F4858;")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.widget_13 = QtWidgets.QWidget(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_14 = QtWidgets.QWidget(self.widget_13)
        self.widget_14.setStyleSheet("background-color:rgb(225, 223, 216);\n"
"border:none;")
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.daily_time = QtWidgets.QTimeEdit(self.widget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daily_time.sizePolicy().hasHeightForWidth())
        self.daily_time.setSizePolicy(sizePolicy)
        self.daily_time.setMinimumSize(QtCore.QSize(110, 0))
        self.daily_time.setStyleSheet("border:none;\n"
"font-size:10pt;\n"
"background-color:#CDB4DB;\n"
"color:black;\n"
"padding:6px;")
        self.daily_time.setObjectName("daily_time")
        self.horizontalLayout_6.addWidget(self.daily_time)
        self.daily_text = QtWidgets.QTextEdit(self.widget_14)
        self.daily_text.setStyleSheet("background-color:#CDB4DB;\n"
"color:black;\n"
"padding-left:10px;\n"
"border:1px solid #9D4EDD;")
        self.daily_text.setObjectName("daily_text")
        self.horizontalLayout_6.addWidget(self.daily_text)
        self.verticalLayout_9.addWidget(self.widget_14)
        self.daily_button = QtWidgets.QPushButton(self.widget_13)
        self.daily_button.setMinimumSize(QtCore.QSize(0, 40))
        self.daily_button.setMaximumSize(QtCore.QSize(120, 40))
        self.daily_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.daily_button.setStyleSheet("QPushButton {\n"
"    font-size: 14px;\n"
"    background-color:#A2D2FF;\n"
"    border:none;\n"
"    color:black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 16px;\n"
"}")
        self.daily_button.setObjectName("daily_button")
        self.verticalLayout_9.addWidget(self.daily_button)
        self.verticalLayout_6.addWidget(self.widget_13)
        self.verticalLayout.addWidget(self.widget_8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Settings"))
        self.save_button.setText(_translate("Form", "Save Changes"))
        self.label.setText(_translate("Form", "Select Music Folder Path"))
        self.path_label.setText(_translate("Form", "..."))
        self.select_button.setText(_translate("Form", "Select Folder"))
        self.label_3.setText(_translate("Form", "Change wake word(Information about feature here)"))
        self.wake_word_label.setText(_translate("Form", "Ruby"))
        self.wake_button.setText(_translate("Form", "Submit"))
        self.default_wake_button.setText(_translate("Form", "Default"))
        self.label_4.setText(_translate("Form", "Keep Running?"))
        self.tray_check_box.setText(_translate("Form", "Keep running in background"))
        self.label_6.setText(_translate("Form", "Change Audio Input"))
        self.audio_device.setCurrentText(_translate("Form", "First"))
        self.audio_device.setItemText(0, _translate("Form", "First"))
        self.audio_device.setItemText(1, _translate("Form", "Second"))
        self.audio_device.setItemText(2, _translate("Form", "Third"))
        self.audio_device.setItemText(3, _translate("Form", "Fourth"))
        self.label_2.setText(_translate("Form", "Add Reminder"))
        self.label_7.setText(_translate("Form", "Set a weekly reminder"))
        self.day_combo.setItemText(0, _translate("Form", "Sunday"))
        self.day_combo.setItemText(1, _translate("Form", "Monday"))
        self.day_combo.setItemText(2, _translate("Form", "Tuesday"))
        self.day_combo.setItemText(3, _translate("Form", "Wednesday"))
        self.day_combo.setItemText(4, _translate("Form", "Thursday"))
        self.day_combo.setItemText(5, _translate("Form", "Friday"))
        self.day_combo.setItemText(6, _translate("Form", "Saturday"))
        self.day_time.setDisplayFormat(_translate("Form", "hh:mm"))
        self.day_button.setText(_translate("Form", "Submit"))
        self.label_8.setText(_translate("Form", "Set one time reminder"))
        self.one_day_time.setDisplayFormat(_translate("Form", "hh:mm"))
        self.one_day_button.setText(_translate("Form", "Submit"))
        self.label_9.setText(_translate("Form", "Set a daily reminder"))
        self.daily_time.setDisplayFormat(_translate("Form", "hh:mm"))
        self.daily_button.setText(_translate("Form", "Submit"))
