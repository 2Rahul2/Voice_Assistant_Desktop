
from PyQt5.QtWidgets import QApplication, QWidget ,QFileDialog , QLabel, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal



from chats_ui import Ui_Form as Ui_Chats
from animations.loading_animation import LoadingWindow
from functionalities.rw_json_data import GetJsonData
from functionalities.chat_json_data import ChatJsonData
from functionalities.get_summary import GetSummary
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
class Worker(QThread):
    result_ready = pyqtSignal(str ,QPushButton ,QLabel)
    def __init__(self, query,load ,label , parent=None):
        super().__init__(parent)
        self.query = query
        self.load = load
        self.label = label
        self.user_text = ""
        
    def run(self):
        get_summary_object = GetSummary()
        # get_url = get_summary_object.get_google_search_results(self.query)
        summary = get_summary_object.get_response(self.query)
        self.result_ready.emit(summary ,self.load , self.label) 
class Chats(QWidget ,Ui_Chats):
    def __init__(self ,parent=None):
        super(Chats, self).__init__(parent)
        self.setupUi(self)
        # self.load_previous_chat()
        self.scrollArea.verticalScrollBar().rangeChanged.connect(
            lambda min, max: self.scrollArea.verticalScrollBar().setValue(max)
        )
        # self.add_user_chat()
        self.send_button.clicked.connect(self.send_button_function)
        # self.add_assistant_chat()
    def delete_chats(self):
        while self.chat_layout.count():
            item = self.chat_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()
    def load_previous_chat(self):
        chat_json_object = ChatJsonData()
        # json_object = GetJsonData()
        # start , end = json_object.get_message_index()
        result = chat_json_object.read_chat()
        # for i in range(start-1 ,end):
        for chat in result:
            # print(chat)
            self.add_user_chat(chat['user'])
            self.add_assistant_chat(chat['assistant'],False)
    def send_button_function(self):
        self.user_text = self.get_query_text.toPlainText()
        self.get_query_text.clear()
        if self.user_text != "":
            self.add_user_chat(self.user_text)
            loading_button , chat_label = self.add_assistant_chat()
            # get_summary_object = GetSummary()
            self.worker = Worker(self.user_text ,loading_button ,chat_label)
            self.worker.result_ready.connect(self.on_result_ready)
            self.worker.start()
        print("clicked send button")
    def on_result_ready(self, result ,load , chat):
        chat.setText(result)
        load.stop_loading()
        load.deleteLater()
        # self.save_chats_json(self.user_text , result)
        self.save_chats_json(self.user_text ,result)
        # self.spinner.stop()
        # self.label.setText(result)
    def save_chats_json(self , user_text ,assistant_text):
        chat_object = ChatJsonData()
        chat_object.write_chat(user_text , assistant_text)
        print(chat_object.read_chat())
    def add_assistant_chat(self ,assisstantText="...", addLoading = True):
        _translate = QtCore.QCoreApplication.translate

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
        # loading animation

        self.loading_button = LoadingWindow()
        if addLoading:
            self.loading_button.setMinimumSize(QtCore.QSize(40, 40))
            self.loading_button.setLayoutDirection(QtCore.Qt.LeftToRight)
            # self.loading_button.setStyleSheet("")
            # self.loading_button.setText("")
            
            
            self.loading_button.setIconSize(QtCore.QSize(40, 40))
            # self.loading_button.setAutoDefault(False)
            # self.loading_button.setDefault(False)
            # self.loading_button.setFlat(False)
            self.loading_button.setObjectName("loading_button")
            self.assistant_layout.addWidget(self.loading_button, 0, QtCore.Qt.AlignTop)


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assistant_label.sizePolicy().hasHeightForWidth())
        self.assistant_label.setSizePolicy(sizePolicy)
        self.assistant_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))

        self.assistant_label.setStyleSheet("width:max-content;\n"
"background-color:#FFAFCC;\n"
"padding:8px;\n"
"\n"
"font: 9pt \"Microsoft YaHei\";")
        self.assistant_label.setScaledContents(True)
        self.assistant_label.setWordWrap(True)
        self.assistant_label.setObjectName("assistant_label")
        self.assistant_label.setText(_translate("Form", assisstantText))

        self.assistant_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)

        self.assistant_layout.addWidget(self.assistant_label)
        self.chat_layout.addWidget(self.assistant_widget, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        return self.loading_button , self.assistant_label
    def add_user_chat(self ,query_text):
        _translate = QtCore.QCoreApplication.translate

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
        self.sender_layout = QtWidgets.QHBoxLayout(self.sender_widget)
        self.sender_layout.setContentsMargins(-1, -1, -1, 11)
        self.sender_layout.setObjectName("sender_layout")
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
        self.sender_label.setText(_translate("Form", query_text))

        self.sender_layout.addWidget(self.sender_label)
        self.chat_layout.addWidget(self.sender_widget)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = Chats()
    main_window.show()
    # main_window.show_floating_window("hah")
    sys.exit(app.exec_())