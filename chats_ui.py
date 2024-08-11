# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chats.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os 
import sys
def resourcepath(relative_path):
    """ Get the absolute path to a resource, works for development and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    except AttributeError:
        # Frozen package or normal Python execution
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(878, 719)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("background-color:rgb(225, 223, 216);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#F26419;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setStyleSheet("border:none;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 835, 767))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chat_area = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat_area.sizePolicy().hasHeightForWidth())
        self.chat_area.setSizePolicy(sizePolicy)
        self.chat_area.setStyleSheet("padding:none;")
        self.chat_area.setObjectName("chat_area")
        self.chat_layout = QtWidgets.QVBoxLayout(self.chat_area)
        self.chat_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.chat_layout.setContentsMargins(-1, 1, -1, 1)
        self.chat_layout.setSpacing(7)
        self.chat_layout.setObjectName("chat_layout")
        self.sender_widget = QtWidgets.QWidget(self.chat_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sender_widget.sizePolicy().hasHeightForWidth())
        self.sender_widget.setSizePolicy(sizePolicy)
        self.sender_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.sender_widget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sender_widget.setStyleSheet("border-radius: 20px 20px 20px 20px;")
        self.sender_widget.setObjectName("sender_widget")
        self.s = QtWidgets.QHBoxLayout(self.sender_widget)
        self.s.setContentsMargins(-1, -1, -1, 11)
        self.s.setObjectName("s")
        self.sender_label = QtWidgets.QLabel(self.sender_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sender_label.sizePolicy().hasHeightForWidth())
        self.sender_label.setSizePolicy(sizePolicy)
        self.sender_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.sender_label.setMouseTracking(False)
        self.sender_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sender_label.setAutoFillBackground(False)
        self.sender_label.setStyleSheet("width:max-content;\n"
"background-color:#CDB4DB;\n"
"padding:8px;\n"
"color:black;\n"
"font: 9pt \"Microsoft YaHei\";")
        self.sender_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sender_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sender_label.setTextFormat(QtCore.Qt.AutoText)
        self.sender_label.setScaledContents(True)
        self.sender_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sender_label.setWordWrap(True)
        self.sender_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.sender_label.setObjectName("sender_label")
        self.s.addWidget(self.sender_label)
        self.chat_layout.addWidget(self.sender_widget)
        self.assistant_widget = QtWidgets.QWidget(self.chat_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assistant_widget.sizePolicy().hasHeightForWidth())
        self.assistant_widget.setSizePolicy(sizePolicy)
        self.assistant_widget.setAcceptDrops(False)
        self.assistant_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.assistant_widget.setStyleSheet("border-radius: 20px 20px 20px 20px;")
        self.assistant_widget.setObjectName("assistant_widget")
        self.assistant_layout = QtWidgets.QHBoxLayout(self.assistant_widget)
        self.assistant_layout.setContentsMargins(-1, 11, -1, -1)
        self.assistant_layout.setSpacing(7)
        self.assistant_layout.setObjectName("assistant_layout")
        self.assistant_logo_button = QtWidgets.QPushButton(self.assistant_widget)
        self.assistant_logo_button.setMaximumSize(QtCore.QSize(40, 40))
        self.assistant_logo_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.assistant_logo_button.setStyleSheet("")
        self.assistant_logo_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resourcepath("icons/chatbot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.assistant_logo_button.setIcon(icon)
        self.assistant_logo_button.setIconSize(QtCore.QSize(40, 40))
        self.assistant_logo_button.setAutoDefault(False)
        self.assistant_logo_button.setDefault(False)
        self.assistant_logo_button.setFlat(False)
        self.assistant_logo_button.setObjectName("assistant_logo_button")
        self.assistant_layout.addWidget(self.assistant_logo_button, 0, QtCore.Qt.AlignTop)
        self.assistant_label = QtWidgets.QLabel(self.assistant_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assistant_label.sizePolicy().hasHeightForWidth())
        self.assistant_label.setSizePolicy(sizePolicy)
        self.assistant_label.setStyleSheet("width:max-content;\n"
"background-color:#FFAFCC;\n"
"padding:8px;\n"
"\n"
"font: 9pt \"Microsoft YaHei\";")
        self.assistant_label.setScaledContents(True)
        self.assistant_label.setWordWrap(True)
        self.assistant_label.setObjectName("assistant_label")
        self.assistant_layout.addWidget(self.assistant_label)
        self.chat_layout.addWidget(self.assistant_widget, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.chat_area)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.widget_2 = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(50, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, -1, 0, 5)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.get_query_text = QtWidgets.QPlainTextEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_query_text.sizePolicy().hasHeightForWidth())
        self.get_query_text.setSizePolicy(sizePolicy)
        self.get_query_text.setMinimumSize(QtCore.QSize(100, 50))
        self.get_query_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.get_query_text.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.get_query_text.setFont(font)
        self.get_query_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.get_query_text.setStyleSheet("background-color:#48CAE4;\n"
"border-radius:10px;")
        self.get_query_text.setObjectName("get_query_text")
        self.horizontalLayout.addWidget(self.get_query_text)
        self.send_button = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy)
        self.send_button.setMinimumSize(QtCore.QSize(0, 0))
        self.send_button.setMaximumSize(QtCore.QSize(40, 40))
        self.send_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.send_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.send_button.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"")
        self.send_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resourcepath("icons/send.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_button.setIcon(icon1)
        self.send_button.setIconSize(QtCore.QSize(40, 40))
        self.send_button.setObjectName("send_button")
        self.horizontalLayout.addWidget(self.send_button)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Chats"))
        self.sender_label.setText(_translate("Form", "Auctor elit sed vulputate mi sit amet mauris commodo. Faucibus nisl tincidunt eget nullam non nisi est sit. Diam in arcu cursus euismod quis. Enim diam vulputate ut pharetra sit amet aliquam id diam. Vitae ultricies leo integer malesuada nunc vel risus commodo viverra. Felis eget nunc lobortis mattis. Amet mattis vulputate enim nulla aliquet porttitor. Neque vitae tempus quam pellentesque nec nam aliquam. Nec tincidunt praesent semper feugiat nibh sed. Fermentum iaculis eu non diam phasellus vestibulum lorem sed risus. Pharetra diam sit amet nisl suscipit adipiscing bibendum est. Sodales neque sodales ut etiam sit amet nisl purus. Morbi non arcu risus quis."))
        self.assistant_label.setText(_translate("Form", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Imperdiet proin fermentum leo vel orci. Risus commodo viverra maecenas accumsan lacus vel facilisis volutpat. In nibh mauris cursus mattis molestie a iaculis at. Tellus elementum sagittis vitae et leo duis ut diam. Nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper. Dignissim enim sit amet venenatis. Tempus egestas sed sed risus pretium quam vulputate. Quisque non tellus orci ac auctor augue mauris augue neque. Nisl condimentum id venenatis a condimentum vitae sapien pellentesque habitant. Accumsan lacus vel facilisis volutpat est velit egestas. Elementum integer enim neque volutpat.\n"
"\n"
"Tortor id aliquet lectus proin nibh nisl condimentum id. Diam ut venenatis tellus in metus vulputate eu scelerisque. Mus mauris vitae ultricies leo integer malesuada nunc vel risus. Venenatis lectus magna fringilla urna porttitor rhoncus dolor purus. Risus viverra adipiscing at in tellus integer feugiat. Sit amet massa vitae tortor. Mattis nunc sed blandit libero volutpat sed cras ornare arcu. Sit amet volutpat consequat mauris nunc congue nisi. Condimentum mattis pellentesque id nibh tortor id. Dolor purus non enim praesent elementum facilisis leo. Parturient montes nascetur ridiculus mus mauris vitae. Eu ultrices vitae auctor eu augue. Egestas egestas fringilla phasellus faucibus scelerisque eleifend."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
