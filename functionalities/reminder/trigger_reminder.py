import uuid

from functionalities.rw_json_data import GetJsonData
# from functionalities.reminder.schedule_reminder import ReminderScheduler


from functionalities.reminder.gloabal_scheduler import global_scheduler

from functionalities.manager.data_manager import DataManager
from functionalities.extract_information.get_reminder_info import GetReminderData


from PyQt5.QtCore import Qt ,QTimer ,pyqtSignal , QObject

from PyQt5.QtCore import QCoreApplication ,Qt ,QThread ,pyqtSlot

class TriggerReminder(QObject):
    def __init__(self):
        super().__init__()
        self.scheduler = global_scheduler

    def store_and_start_reminder(self , job_id , every_day , time , date , days ,message):
        json_object = GetJsonData()
        if days!=None:
            date=None
        json_object.write_reminder_data(time=time ,date=date , message=message ,every_day=every_day ,days=days, job_id=job_id)
        if every_day:
            # daily reminder:
            self.scheduler.set_daily_reminder(job_id=job_id ,time_str=time,action=self.scheduler.remind_text , message=message)
        elif date == None:
            self.scheduler.set_weekly_reminder(job_id=job_id ,time_str=time ,message=message ,action=self.scheduler.remind_text ,day_of_week=days)
        elif days == None:
            self.scheduler.set_specific_date_reminder(job_id=job_id ,time_str=time ,action=self.scheduler.remind_text ,date_str=date)

    def get_reminder_voice(self ,voice_text):
        reminder_data_object = GetReminderData()
        dates, times, days, recurring, message = reminder_data_object.extract_date_time(voice_text)
        formatted_dates, formatted_times, formatted_days, formatted_recurring, formatted_message = reminder_data_object.format_date_time(dates, times, days, recurring, message)
        
        job_id = str(uuid.uuid4())
        every_day = True if len(formatted_recurring) >= 1 else False
        time = formatted_times[0] if len(formatted_times) >= 1 else None
        date = formatted_dates[0] if len(formatted_dates) >= 1 else None
        days = formatted_days[0] if len(formatted_days) >= 1 else None
        self.store_and_start_reminder(job_id , every_day, time , date , days ,formatted_message)

    def start_all_reminder(self):
        json_object = GetJsonData()
        reminder_data = json_object.get_reminder_data()
        # self.scheduler.start()
        for reminder in reminder_data:
            job_id = reminder['job_id']
            time = reminder['time']
            date = reminder['date']
            days = reminder['days']
            message = reminder['message']
            every_day = reminder['every_day']
            if every_day:
                # reminder everyday at mentioned time
                print(every_day , message , time)
                self.scheduler.set_daily_reminder(job_id=job_id ,time_str=time,action=self.scheduler.remind_text , message=message)
            elif date == None:
                # reminder every week (eg: every wednesday)
                print(days ,time ,message)
                self.scheduler.set_weekly_reminder(job_id=job_id ,time_str=time ,message=message ,action=self.scheduler.remind_text ,day_of_week=days)
            elif days == None:
                # reminder at a specific date
                print(message , date , time)
                self.scheduler.set_specific_date_reminder(job_id=job_id ,time_str=time ,action=self.scheduler.remind_text ,date_str=date)

if __name__ == "__main__":
    trigger = TriggerReminder()
    trigger.start_all_reminder()

