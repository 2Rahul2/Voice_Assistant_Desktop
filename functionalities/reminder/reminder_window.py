
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout , QDesktopWidget
from PyQt5.QtCore import Qt ,QTimer ,pyqtSignal , QObject ,pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush ,QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QSound

from reminder import Reminder
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
# from functionalities.features.resource_path import resourcepath
class FloatingReminder(QWidget):
    def __init__(self ):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Popup)
        self.setWindowTitle("Floating Window")
        screen = QDesktopWidget().screenGeometry()
        screen_height = int(screen.height() * 0.20)
        screen_width_20_percent = int(screen.width() * 0.25)
        self.setFixedSize(screen_width_20_percent, screen_height) #240 130
        layout = QVBoxLayout()
        # label = QLabel("This is a floating window.")
        # layout.addWidget(label)
        layout.setContentsMargins(0 ,0 ,0 ,0)
        self.button = Reminder()
        
        layout.addWidget(self.button)
        self.setLayout(layout)
        # Set up the timer to close the window after 5 seconds
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.close_after_timeout)
        self.timer.start(5000)  # 5000 milliseconds = 5 seconds

    @pyqtSlot(str)
    def show_floating_window(self ,text):
        print("showingggg")
        self.button.reminder_text.setText(text)

        screen_geometry = QDesktopWidget().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        window_width = self.frameGeometry().width()
        window_height = self.frameGeometry().height()
        bottom_right_x = screen_width - window_width
        bottom_right_y = screen_height - window_height
        self.sound = QSound(resourcepath("audio/reminder_notification.wav"))
        self.sound.play()
        self.show()
        print("showing reminder now")
        self.move(bottom_right_x, bottom_right_y)
    def close_after_timeout(self):
        self.close()
        # QApplication.quit() 


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = FloatingReminder()
    main_window.show_floating_window("hah")
    sys.exit(app.exec_())