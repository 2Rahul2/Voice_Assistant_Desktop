import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout , QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush ,QIcon
from PyQt5.QtCore import Qt

from chats import Chats

class FloatingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Popup)
        self.setWindowTitle("Floating Window")
        screen = QDesktopWidget().screenGeometry()
        screen_height = int(screen.height() * 0.95)
        screen_width_20_percent = int(screen.width() * 0.45)
        self.setFixedSize(screen_width_20_percent, screen_height) #240 130
        
        layout = QVBoxLayout()
        label = QLabel("This is a floating window.")
        # layout.addWidget(label)
        layout.setContentsMargins(0 ,0 ,0 ,0)
        self.button = Chats()
        self.button.delete_chats()
        self.button.load_previous_chat()
        self.button.setStyleSheet("background-color:rgb(225, 223, 216);")
        
        layout.addWidget(self.button)
        self.setLayout(layout)
    def show_floating_window(self ,search_text):
        screen_geometry = QDesktopWidget().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        window_width = self.frameGeometry().width()
        window_height = self.frameGeometry().height()
        bottom_right_x = screen_width - window_width
        bottom_right_y = screen_height - window_height
        self.button.get_query_text.setPlainText(search_text)
        self.button.send_button_function()
        self.show()
        self.move(bottom_right_x ,bottom_right_y)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setFixedSize(300, 200)
        
        self.button = QPushButton("Show Floating Window", self)
        self.button.clicked.connect(self.show_floating_window)
        self.setCentralWidget(self.button)

        self.floating_window = FloatingWindow()

    def show_floating_window(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        window_width = self.floating_window.frameGeometry().width()
        window_height = self.floating_window.frameGeometry().height()
        bottom_right_x = screen_width - window_width
        bottom_right_y = screen_height - window_height
        self.floating_window.show()
        self.floating_window.move(bottom_right_x ,bottom_right_y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = FloatingWindow()
    main_window.show_floating_window()
    sys.exit(app.exec_())
