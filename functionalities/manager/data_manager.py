

class DataManager:
    def __init__(self):
        self.days = {
            'Sunday':0,
            'Monday':1,
            'Tuesday':2,
            'Wednesday':3,
            'Thursday':4,
            'Friday':5,
            'Saturday':6,
        }
    def get_days_int(self ,day):
        return self.days['day']