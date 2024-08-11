

from datetime import datetime, timedelta
import calendar
from PyQt5.QtCore import QTimer, QTime, QDateTime


class ReminderSingleton:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if self._instance is not None:
            raise Exception("This class is a singleton!")
        self.value = None
        self.reminders = []

    def set_reminder(self, time_str, action, days_of_week=None ,message = "text"):
        """
        Sets a reminder.
        :param time_str: Time string in the format 'HH:MM:SS'
        :param action: Function to execute when the reminder time is reached
        :param days_of_week: List of weekdays (0=Monday, 6=Sunday) when the reminder should recur
        """
        reminder_time = datetime.strptime(time_str, '%H:%M:%S').time()
        if days_of_week is None:
            days_of_week = []  # If no days are specified, it will be a one-time reminder
        self.reminders.append((reminder_time, action, days_of_week ,message))
        self.reminders.sort(key=lambda x: x[0])  # Ensure reminders are sorted by time
        self.set_next_timer()

    def set_next_timer(self):
        """
        Sets the timer for the next upcoming reminder.
        """
        next_reminder = self.get_next_reminder()
        if next_reminder:
            next_reminder_time, _, _ ,message = next_reminder
            current_time = QTime.currentTime()
            reminder_qtime = QTime(next_reminder_time.hour, next_reminder_time.minute, next_reminder_time.second)
            ms_until_next = current_time.msecsTo(reminder_qtime)
            if ms_until_next < 0:
                ms_until_next += 24 * 3600 * 1000  # Adjust for reminders past midnight
            self.timer.start(ms_until_next)
        else:
            self.timer.stop()  # No upcoming reminders, stop the timer

    def get_next_reminder(self):
        """
        Returns the next reminder that needs to be triggered.
        """
        current_date = datetime.now()
        current_weekday = current_date.weekday()
        current_time = current_date.time()

        for reminder_time, action, days_of_week ,message in self.reminders:
            if not days_of_week or current_weekday in days_of_week:
                if reminder_time > current_time or not days_of_week:
                    return reminder_time, action, days_of_week ,message

        # If no reminders are found for today, look ahead to the next day
        for days_ahead in range(1, 8):
            next_day = (current_weekday + days_ahead) % 7
            for reminder_time, action, days_of_week ,message in self.reminders:
                if next_day in days_of_week:
                    next_reminder_date = datetime.combine(datetime.now() + timedelta(days=days_ahead), reminder_time)
                    return next_reminder_date.time(), action, days_of_week ,message

        return None  # No reminders found

    def check_reminders(self):
        """
        Executes the next reminder action and sets the timer for the following reminder.
        """
        next_reminder = self.get_next_reminder()
        if next_reminder:
            next_reminder_time, action, days_of_week ,message= next_reminder
            action(message)  # Execute the action
            if days_of_week:
                # Reschedule the reminder for the next week
                next_week_reminder_time = datetime.combine(datetime.today(), next_reminder_time) + timedelta(days=7)
                self.reminders.append((next_week_reminder_time.time(), action, days_of_week ,message))
                self.reminders.sort(key=lambda x: x[0])
            self.set_next_timer()  # Set timer for the next reminder
