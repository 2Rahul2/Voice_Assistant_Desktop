import spacy
import re
from dateutil.parser import parse
from datetime import datetime


class GetReminderData:
    def __init__(self):
        pass
        # Load the spaCy model
        self.nlp = spacy.load('en_core_web_sm')

        # List of days of the week
        self.days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

        # List of recurring intervals
        self.recurring_intervals = ["daily", "weekly", "monthly"]

    def extract_date_time(self  ,text):
        doc = self.nlp(text)
        dates = []
        times = []
        days = []
        recurring = []
        message = None

        # Regex patterns for different time expressions
        time_patterns = [
            r'(\d{1,2}):(\d{2})\s*(am|pm)?',
            r'(\d{1,2})\s*o\'?clock\s*(am|pm)?',
        ]

        # Extract date and time using spaCy and dateutil
        for ent in doc.ents:
            if ent.label_ == 'DATE':
                try:
                    dt = parse(ent.text, fuzzy=True)
                    dates.append(dt.date())
                except Exception as e:
                    print(f"Could not parse date {ent.text}: {e}")
            elif ent.label_ == 'TIME':
                try:
                    dt = parse(ent.text, fuzzy=True)
                    times.append(dt.time())
                except Exception as e:
                    print(f"Could not parse time {ent.text}: {e}")

        # Manually handle time patterns
        for pattern in time_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                hour = int(match.group(1))
                minute = int(match.group(2)) if len(match.groups()) > 2 and match.group(2) else 0
                am_pm = match.group(3) if len(match.groups()) > 3 else None
                if am_pm:
                    if am_pm.lower() == 'pm' and hour != 12:
                        hour += 12
                    elif am_pm.lower() == 'am' and hour == 12:
                        hour = 0
                time_obj = datetime.strptime(f"{hour}:{minute}", "%H:%M").time()
                times.append(time_obj)

        # Extract days of the week
        for day in self.days_of_week:
            if re.search(r'\b' + day + r'\b', text, re.IGNORECASE):
                days.append(day.capitalize())

        # Extract recurring intervals
        for interval in self.recurring_intervals:
            if re.search(r'\b' + interval + r'\b', text, re.IGNORECASE):
                recurring.append(interval.capitalize())

        # Extract message
        message_match = re.search(r'for\s+(.+)', text, re.IGNORECASE)
        if message_match:
            message = message_match.group(1).strip()

        return dates, times, days, recurring, message

    def format_date_time(self ,dates, times, days, recurring, message):
        formatted_dates = [date.strftime("%Y-%m-%d") for date in dates]
        formatted_times = [time.strftime("%H:%M:%S") for time in times]
        return formatted_dates, formatted_times, days, recurring, message