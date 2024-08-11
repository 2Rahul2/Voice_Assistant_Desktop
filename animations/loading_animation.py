import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QTimer, Qt
from pyqtspinner.spinner import WaitingSpinner

class LoadingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loading Spinner Example")
        self.setGeometry(0, 0, 40, 40)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)
        self.spinner = WaitingSpinner(self ,line_width=10 ,lines=7 ,radius=10)
        self.start_loading()
    def start_loading(self):
        self.spinner.start()
        # self.label.setText("Loading...")
    def stop_loading(self):
        self.spinner.stop()
        # Simulate a long-running task
        # QTimer.singleShot(3000, self.stop_loading)  # Stop loading after 3 seconds

    # def stop_loading(self):
        # self.spinner.stop()
        # self.label.setText("Loading complete. Click the button to start again.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoadingWindow()
    window.show()
    sys.exit(app.exec_())
