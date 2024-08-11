import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout , QSizePolicy, QDesktopWidget
from PyQt5.QtCore import Qt ,QDir
from PyQt5 import QtCore, QtGui , uic ,QtWidgets

from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush ,QIcon
from PyQt5.QtCore import Qt, QRect, QTimer ,QSize , QPropertyAnimation, QPoint

from ripple_buttin_ui import Ui_Form
from chats import Chats
class RingEffectButton(QPushButton):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.brush_color = QColor(137, 109, 207, 80)
        self.circles = []
        self.animation_timer = QTimer(self)
        self.animation_timer.setInterval(30)  # Adjust the interval for smoother animation
        self.animation_timer.timeout.connect(self.update_animation)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/microphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setSizePolicy(QSizePolicy.Policy.Expanding , QSizePolicy.Policy.Expanding)
        self.setIconSize(QtCore.QSize(80, 80))
        self.spawn_timer = QTimer(self)
        self.spawn_timer.setInterval(500)  # Adjust the interval for spawning new circles
        self.spawn_timer.timeout.connect(self.spawn_circle)

        self.animation_timer.start()
        self.spawn_timer.start()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for circle in self.circles:
            radius = circle['radius']
            opacity = circle['opacity']
            if radius > 0:
                painter.setBrush(QBrush(self.brush_color))
                painter.setPen(Qt.NoPen)
                rect = QRect(0, 0, 2 * radius, 2 * radius)
                rect.moveCenter(self.rect().center())
                painter.setOpacity(opacity)
                painter.drawEllipse(rect)

    def spawn_circle(self):
        self.circles.append({'radius': 30, 'opacity': 0.8})  # Add a new circle with starting radius 0 and opacity 1.0

    def update_animation(self):
        for circle in self.circles:
            circle['radius'] += 2  # Increment the radius
            circle['opacity'] -= 0.02  # Decrease the opacity
        self.circles = [circle for circle in self.circles if circle['opacity'] > 0]  # Remove circles with opacity <= 0
        self.update()

class FloatingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Popup)
        self.setWindowTitle("Floating Window")
        self.setFixedSize(240, 130)
        
        layout = QVBoxLayout()
        # layout.addWidget(label)
        layout.setContentsMargins(0 ,0 ,0 ,0)
        button = RingEffectButton('')
        button.setStyleSheet("background-color:#201f2e;border:none;")
        layout.addWidget(button)
        self.setLayout(layout)

        self.close_timer = QTimer(self)
        self.close_timer.setSingleShot(True)
        self.close_timer.timeout.connect(self.close_floating_window)
    def close_floating_window(self):
        self.close()
    def show_floating_window(self):
        screen_geometry = QDesktopWidget().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        window_width = self.frameGeometry().width()
        window_height = self.frameGeometry().height()
        bottom_right_x = screen_width - window_width
        bottom_right_y = screen_height - window_height
        self.show()
        self.move(bottom_right_x ,bottom_right_y)

        self.close_timer.start(5000)


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
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
