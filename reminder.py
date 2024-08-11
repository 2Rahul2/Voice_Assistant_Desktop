import sys

from reminder_ui import Ui_Form as Ui_Reminder
from PyQt5.QtWidgets import QApplication, QWidget ,QFileDialog



class Reminder(QWidget ,Ui_Reminder):
    def __init__(self ,parent=None):
        super(Reminder, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    settings_window = Reminder()
    settings_window.show()
    sys.exit(app.exec_())