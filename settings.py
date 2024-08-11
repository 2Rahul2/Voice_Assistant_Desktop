import uuid
from settings_ui import Ui_Form as Ui_Settings
from PyQt5.QtWidgets import QApplication, QWidget ,QFileDialog

from functionalities.get_audio_input_device import GetAudioDevice
from functionalities.reminder.schedule_reminder import ReminderScheduler

from functionalities.rw_json_data import GetJsonData
import sys
# from functionalities.reminder.test import Test

from functionalities.reminder.gloabal_scheduler import global_scheduler


class Settings(QWidget ,Ui_Settings):
    def __init__(self ,parent=None):
        super(Settings, self).__init__(parent)
        self.setupUi(self)
        self.save_button.clicked.connect(self.save_changes_function)
        self.select_button.clicked.connect(self.open_folder)
        self.wake_button.clicked.connect(self.submit_wake_word)
        self.one_day_button.clicked.connect(self.one_day_submit_button)
        self.day_button.clicked.connect(self.day_submit_button)
        self.daily_button.clicked.connect(self.daily_submit_button)
        self.default_wake_button.clicked.connect(self.default_wake_submit_button)
    def default_wake_submit_button(self):
        get_json_data_object = GetJsonData()
        get_json_data_object.write_wake_word("Nikki")
        self.wake_word_label.setText("Nikki")
    
    def daily_submit_button(self):
        scheduler = global_scheduler
        message = self.daily_text.toPlainText()
        # test = Test()
        # test.num += 1
        # print("TEST NUMBER:  " ,test.num)

        # test.send()
        if message != "":
            time = self.daily_time.time().toString('HH:mm') 
            get_json_data_object = GetJsonData()
            job_id = str(uuid.uuid4())
            get_json_data_object.write_reminder_data( job_id=job_id,message=message ,time=time ,every_day=True)
            scheduler.set_daily_reminder( job_id=job_id,time_str=time,action=scheduler.remind_text , message=message)
            scheduler.start()


    # every sepcific day reminder
    def one_day_submit_button(self):
        scheduler = global_scheduler

        message = self.one_day_text.toPlainText()
        time = self.one_day_time.time().toString('HH:mm') 
        date = self.one_day_date.date().toString('yyyy-MM-dd')
        if message != "":
            get_json_data_object = GetJsonData()
            job_id = str(uuid.uuid4())

            get_json_data_object.write_reminder_data(job_id=job_id , time=time ,date=date , message=message)
            scheduler.set_specific_date_reminder(job_id=job_id , time_str=time ,action=scheduler.remind_text ,date_str=date)
            scheduler.start()
            print("One day reminder set to : " ,message , time.toString('HH:mm') ,date.toString('yyyy-MM-dd'))
        # Start Timer
        
    # particular day reminder
    def day_submit_button(self):
        scheduler = global_scheduler

        message = self.day_text.toPlainText()
        if message != "":
            time = self.day_time.time().toString('HH:mm') 
            combo_date = self.day_combo.currentText()
            days_dict = {
                'Sunday':0,
                'Monday':1,
                'Tuesday':2,
                'Wednesday':3,
                'Thursday':4,
                'Friday':5,
                'Saturday':6
            }
            get_json_data_object = GetJsonData()
            job_id = str(uuid.uuid4())

            get_json_data_object.write_reminder_data( job_id=job_id,time=time ,message=message ,days=combo_date)
            scheduler.set_weekly_reminder( job_id=job_id,time_str=time ,message=message ,action=scheduler.remind_text ,day_of_week=combo_date)
            scheduler.start()
            
            print("Day reminder : " ,message , time ,combo_date)
    def submit_wake_word(self):
        wake_word = self.wake_word_label.text()
        get_json_data_object = GetJsonData()
        get_json_data_object.write_wake_word(wake_word)
        self.wake_word_label.setText(wake_word)
        print("saved")
    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(self ,"Select Folder")
        if folder:
             print(folder)
             json_data_object = GetJsonData()
             json_data_object.write_music_path(folder)
             self.path_label.setText(folder)
        else:
            print("Default Path")
    def save_changes_function(self):
        def get_key_by_value(d, value):
                for key, val in d.items():
                        if val == value:
                                return key
                return 0
        audio_name = self.audio_device.currentText()
        get_audio_input_object = GetAudioDevice()
        get_json_data_object = GetJsonData()
        audio_index = get_key_by_value(get_audio_input_object.get_devices() ,audio_name)
        get_json_data_object.write_input_audio_device(audio_index)

        if self.tray_check_box.isChecked():
             get_json_data_object.write_system_tray(True)
        else:
             get_json_data_object.write_system_tray(False)
        print(audio_name)
        print("saved")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    settings_window = Settings()
    settings_window.show()
    sys.exit(app.exec_())