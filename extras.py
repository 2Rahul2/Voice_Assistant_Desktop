
from extras_ui import Ui_Form as Ui_Extras
from PyQt5.QtWidgets import QApplication, QWidget ,QFileDialog , QLabel, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt ,QTimer ,pyqtSignal ,QObject
from functionalities.rw_json_data import GetJsonData

from functionalities.reminder.gloabal_scheduler import global_scheduler

class Extras(QWidget ,Ui_Extras ,QObject):
    ischange = pyqtSignal()

    def __init__(self ,parent=None):
        super(Extras, self).__init__(parent)
        self.setupUi(self)  
        # self.add_reminders()
        # self.add_reminders()
        # self.add_reminders()

        # self.get_reminders()
    def get_reminders(self):
        print("Getting Data")
        json_object = GetJsonData()
        reminder_data = json_object.get_reminder_data()
        # self.clear_widget(self.verticalLayout_3)

        
        for index, reminder in enumerate(reminder_data):
            time = reminder['time']
            days = reminder['days']
            every_day = reminder['every_day']
            date = reminder['date']
            message = reminder['message']
            if every_day:
                # reminder everyday at mentioned time
                string = f"Every day at Time {time}"
                self.add_reminders(remind_text=message , time_text=string ,index=index)
            elif date == None:
                # reminder every week (eg: every wednesday)
                string = f"Every {days} at Time {time}"
                self.add_reminders(remind_text=message , time_text=string ,index=index)
            elif days == None:
                string = f"On {date} at Time {time}"
                self.add_reminders(remind_text=message , time_text=string ,index=index)


        print("reminder data : " ,reminder_data)
    def add_reminders(self ,remind_text = "" , time_text = "" ,index=0):
        # reminder_page = self.my_reminders
        self.reminder_widget = QtWidgets.QWidget(self.my_reminders)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reminder_widget.sizePolicy().hasHeightForWidth())
        self.reminder_widget.setSizePolicy(sizePolicy)
        self.reminder_widget.setMinimumSize(QtCore.QSize(0, 120))
        self.reminder_widget.setMaximumSize(QtCore.QSize(16777215, 120))
        self.reminder_widget.setStyleSheet("border: 1px solid black;\n"
"background-color:#F1FFE7;\n"
"border-radius:10px")
        self.reminder_widget.setObjectName("reminder_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.reminder_widget)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.reminder_label = QtWidgets.QLabel(self.reminder_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reminder_label.sizePolicy().hasHeightForWidth())
        self.reminder_label.setSizePolicy(sizePolicy)
        self.reminder_label.setMinimumSize(QtCore.QSize(250, 10))
        self.reminder_label.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.reminder_label.setFont(font)
        self.reminder_label.setStyleSheet("border:none;\n"
"color:#2F4858;")
        self.reminder_label.setObjectName("reminder_label")
        self.verticalLayout_2.addWidget(self.reminder_label)
        self.reminder_delete_button = QtWidgets.QPushButton(self.reminder_widget)
        self.reminder_delete_button.setMinimumSize(QtCore.QSize(120, 40))
        self.reminder_delete_button.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.reminder_delete_button.setFont(font)
        self.reminder_delete_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reminder_delete_button.setStyleSheet("QPushButton {\n"
"    font-size: 11pt;\n"
"    background-color:#eb4d62;\n"
"    border:none;\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size: 11pt;\n"
"    background-color:#f73650;\n"
"}")
        self.reminder_duration = QtWidgets.QLabel(self.reminder_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reminder_duration.sizePolicy().hasHeightForWidth())
        self.reminder_duration.setSizePolicy(sizePolicy)
        self.reminder_duration.setMinimumSize(QtCore.QSize(250, 0))
        self.reminder_duration.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.reminder_duration.setFont(font)
        self.reminder_duration.setStyleSheet("border:none;\n"
"color:#2F4858;")
        self.reminder_duration.setObjectName("reminder_duration")
        self.verticalLayout_2.addWidget(self.reminder_duration)
        self.reminder_delete_button.setObjectName("reminder_delete_button")
        self.reminder_delete_button.clicked.connect(lambda _, idx=index: self.delete_button(idx))
        self.verticalLayout_2.addWidget(self.reminder_delete_button)
        self.reminder_duration.setText(remind_text)
        self.reminder_label.setText(time_text)
        self.reminder_delete_button.setText("Delete")
        self.verticalLayout_3.addWidget(self.reminder_widget)



    def delete_button(self ,position):
        json_object = GetJsonData()
        reminder_data = json_object.get_reminder_data()
        jobID = reminder_data[position].get('job_id')
        scheduler = global_scheduler
        scheduler.cancel_job(jobID)
        reminder_data.pop(position)
        json_object.write_reminder(reminder_data)
        self.ischange.emit()
        print(position)

    def clear_widget(self):
        while self.verticalLayout_3.count():
            item = self.verticalLayout_3.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()