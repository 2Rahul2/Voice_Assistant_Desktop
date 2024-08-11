import schedule
import time
import threading
from datetime import datetime

from PyQt5 import QtWidgets , uic


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout , QDesktopWidget
from PyQt5.QtCore import Qt ,QTimer ,pyqtSignal , QObject ,pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush ,QIcon
from PyQt5.QtCore import Qt ,QThread
from PyQt5.QtMultimedia import QSound
from reminder import Reminder
from chats import Chats
# from functionalities.reminder.reminder_window import FloatingReminder



# class FloatingReminder(QWidget):
#     def __init__(self ):
#         super().__init__()
#         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Popup)
#         self.setWindowTitle("Floating Window")
#         screen = QDesktopWidget().screenGeometry()
#         screen_height = int(screen.height() * 0.20)
#         screen_width_20_percent = int(screen.width() * 0.25)
#         self.setFixedSize(screen_width_20_percent, screen_height) #240 130
#         layout = QVBoxLayout()
#         # label = QLabel("This is a floating window.")
#         # layout.addWidget(label)
#         layout.setContentsMargins(0 ,0 ,0 ,0)
#         self.button = Reminder()
        
#         layout.addWidget(self.button)
#         self.setLayout(layout)
#         # Set up the timer to close the window after 5 seconds
#         # self.timer = QTimer(self)
#         # self.timer.setSingleShot(True)
#         # self.timer.timeout.connect(self.close_after_timeout)
#         # self.timer.start(5000)  # 5000 milliseconds = 5 seconds

#     @pyqtSlot(str)
#     def show_floating_window(self ,text="hahah"):
#         print("showingggg")
#         self.button.reminder_text.setText(text)

#         screen_geometry = QDesktopWidget().availableGeometry()
#         screen_width = screen_geometry.width()
#         screen_height = screen_geometry.height()

#         window_width = self.frameGeometry().width()
#         window_height = self.frameGeometry().height()
#         bottom_right_x = screen_width - window_width
#         bottom_right_y = screen_height - window_height
#         self.sound = QSound("audio/reminder_notification.wav")
#         self.sound.play()
#         self.show()
#         print("showing reminder now")
#         # self.move(bottom_right_x, bottom_right_y)
#     def close_after_timeout(self):
#         self.close()
class ReminderScheduler(QObject):
    trigger_reminder_text = pyqtSignal(str)
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(ReminderScheduler, cls).__new__(cls)
            cls._instance._init()
        return cls._instance

    
    def _init(self):
        super().__init__()
        self.jobs = {}
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self.scheduler_thread = threading.Thread(target=self.run_schedule)
            self.scheduler_thread.daemon = True
            self.scheduler_thread.start()

    def remind_text(self, text=""):
        print("Hey!! Reminder:", text)
        self.trigger_reminder_text.emit(text)

    def run_schedule(self):
        while self.running:
            schedule.run_pending()
            time.sleep(1)

    def stop(self):
        self.running = False

    def set_daily_reminder(self, job_id, time_str, action, message):
        job = schedule.every().day.at(time_str).do(action, message)
        self.jobs[job_id] = job
        # return job_id

    def set_weekly_reminder(self, job_id, time_str, action, message, day_of_week):
        job = getattr(schedule.every(), day_of_week.lower()).at(time_str).do(action, message)
        self.jobs[job_id] = job
        # return job_id

    def set_specific_date_reminder(self, job_id, date_str, time_str, action, message):
        job = schedule.every().day.at(time_str).do(self.check_specific_date, date_str, action, message)
        self.jobs[job_id] = job
        # return job_id

    def check_specific_date(self, date_str, action, message):
        today_date = datetime.now().strftime('%d-%m-%Y')
        if today_date == date_str:
            action(message)

    def cancel_job(self, job_id):
        job = self.jobs.pop(job_id, None)
        if job:
            schedule.cancel_job(job)
        else:
            print("Job not found")


if __name__ == "__main__":
    pass