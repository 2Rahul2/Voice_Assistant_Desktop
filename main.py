from PyQt5 import QtWidgets , uic
from main_ui import Ui_MainWindow
from PyQt5.QtWidgets import QSystemTrayIcon , QMenu, QAction, QWidget, QLabel, QVBoxLayout ,QDesktopWidget
from PyQt5.QtCore import QCoreApplication ,Qt ,QThread ,pyqtSlot
from PyQt5.QtGui import QIcon
# from chats_ui import Ui_Form  # The custom widget class
from ripple_buttin_ui import Ui_Form
from settings_ui import Ui_Form as Ui_Settings
from chats_ui import Ui_Form as Ui_Chats
from about_ui import Ui_Form as Ui_About
from how_ui import Ui_Form as Ui_How


from floating_chat import FloatingWindow as FloatingChatWindow
from settings import Settings
from chats import Chats
from music_animation import MusicVisualizer
from extras import Extras
from functionalities.get_audio_input_device import GetAudioDevice
from functionalities.rw_json_data import GetJsonData
from functionalities.reminder.trigger_reminder import TriggerReminder
from functionalities.reminder.reminder_window import FloatingReminder
# from functionalities.reminder.schedule_reminder import  ReminderScheduler
# from functionalities.reminder.reminder_window import FloatingReminder


from voice import VoiceListener


# from functionalities.reminder.test import Test
import os
import sys

def resourcepath(relative_path):
    """ Get the absolute path to a resource, works for development and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    except AttributeError:
        # Frozen package or normal Python execution
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

from functionalities.reminder.gloabal_scheduler import global_scheduler
from mic_icon_popup import FloatingWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi(resourcepath('main.ui'), self)  # Load the main UI
        self.setWindowTitle("Voice Assistant")
        self.setWindowIcon(QIcon(resourcepath('icons/chatbot_icon.ico')))
        self.setting_button.clicked.connect(self.loadSettings)
        self.chat_button.clicked.connect(self.loadChats)
        self.about_button.clicked.connect(self.loadAbout)
        self.how_button.clicked.connect(self.loadHow)
        self.extras_button.clicked.connect(self.loadExtras)

        self.schedule_thread = QThread()
        global_scheduler.moveToThread(self.schedule_thread)
        global_scheduler.trigger_reminder_text.connect(self.open_reminder_window)
        self.schedule_thread.start()
        global_scheduler.start()
        # Find the placeholder widget in the main window
        placeholder_widget = self.findChild(QtWidgets.QFrame, 'placeholderWidget')

        # Load the chats.ui file into a new QWidget
        self.sub_widget = QtWidgets.QWidget()
        self.stacked_widget = QtWidgets.QStackedWidget(self)

        self.music_animation_ui = MusicVisualizer()
        self.music_widget_2.addWidget(self.music_animation_ui)
        # self.music_widget_2.addColor
        # Create instances of the settings and chats UIs
        # self.settings_widget = QtWidgets.QWidget()
        self.settings_ui = Settings()

         # self.test = Test()
        # self.test_thread = QThread()
        # self.test.moveToThread(self.test_thread)
        # self.test.trigger_reminder_text.connect(self.open_reminder_window)
        # self.test_thread.start()
        self.extras_ui = Extras()
        self.extra_thread = QThread()
        self.extras_ui.moveToThread(self.extra_thread)
        self.extras_ui.ischange.connect(self.update_extra)
        self.extra_thread.start()
        # self.settings_ui.setupUi(self.settings_widget)

        # self.chats_widget = QtWidgets.QWidget()
        self.chats_ui = Chats()



        # self.chats_ui.setupUi(self.chats_widget)  

        self.about_widget = QtWidgets.QWidget()
        self.about_ui = Ui_About()
        self.about_ui.setupUi(self.about_widget)   

        self.how_widget = QtWidgets.QWidget()
        self.how_ui = Ui_How()
        self.how_ui.setupUi(self.how_widget)   

        self.stacked_widget.addWidget(self.about_widget)
        self.stacked_widget.addWidget(self.how_widget)

        self.stacked_widget.addWidget(self.settings_ui)
        self.stacked_widget.addWidget(self.chats_ui)
        self.stacked_widget.addWidget(self.extras_ui)
        # uic.loadUi('settings.ui', sub_widget)

        # Get the existing layout of the placeholder widget
        existing_layout = placeholder_widget.layout()
        
        if existing_layout is None:
            # If there's no existing layout, create a new layout
            self.layout = QtWidgets.QVBoxLayout(placeholder_widget)
        else:
            # If there is an existing layout, use it
            self.layout = existing_layout
        
        # Add the sub_widget to the layout
        self.layout.addWidget(self.stacked_widget)
        # Create the system tray icon
        self.tray_icon = QSystemTrayIcon(QIcon(resourcepath("icons/chatbot.png")), self)  # Use an appropriate icon
        self.tray_icon.setToolTip("Assistant")

        # Create a context menu for the tray icon
        tray_menu = QMenu()
        
        # Add 'Show' action
        show_action = QAction("Show", self)
        show_action.triggered.connect(self.show)
        tray_menu.addAction(show_action)
        
        # Add 'Exit' action
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(QCoreApplication.instance().quit)
        tray_menu.addAction(exit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.voice_listener_object = VoiceListener()
        self.voice_thread = QThread() 
        self.voice_listener_object.moveToThread(self.voice_thread)
        self.voice_listener_object.command_text.connect(lambda text : self.voice_listener_object.run_commands(text))
        self.voice_listener_object.wake_detected.connect(self.got_command)
        self.voice_listener_object.chat_command.connect(self.open_floating_chat)
        self.voice_thread.started.connect(self.voice_listener_object.run_voice)
        self.voice_thread.start()

        # self.trigger_thread = QThread()
        self.trigger_reminder_object = TriggerReminder()
        # self.trigger_reminder_object.moveToThread(self.trigger_thread)
        self.trigger_reminder_object.start_all_reminder()
        # self.trigger_thread.start()
        screen = QDesktopWidget().screenGeometry()
        screen_height = int(screen.height() * 0.60)
        screen_width_20_percent = int(screen.width() * 0.55)
        self.setFixedSize(screen_width_20_percent, screen_height)
        
        # self.test = Test()
        # self.test.num += 1
        # self.test_thread = QThread()
        # self.test.moveToThread(self.test_thread)
        # self.test.trigger_reminder_text.connect(self.open_reminder_window)
        # self.test_thread.start()
        # print("TEST NUMBER:  " ,self.test.num)

    @pyqtSlot()
    def update_extra(self):
        self.extras_ui.clear_widget()
        self.extras_ui.get_reminders()
    @pyqtSlot(str)
    def open_floating_chat(self ,text):
        self.floating_chat_window = FloatingChatWindow()
        self.floating_chat_window.show_floating_window(text)
    @pyqtSlot(str)
    def open_reminder_window(self ,text):
        print("works")
        self.floating_reminder = FloatingReminder()
        self.floating_reminder.show_floating_window(text)
    def got_command(self):
        self.floating_window = FloatingWindow()
        self.floating_window.show_floating_window()
        
        print("hehehehehheehhhe")
    def closeEvent(self, event):
        event.ignore()
        json_data_object = GetJsonData()
        if json_data_object.get_system_tray():
            self.hide()
        else:
            QCoreApplication.instance().quit()

        # Prevent the default close event behavior
        # Hide the window instead
    def loadExtras(self):
        self.stacked_widget.setCurrentWidget(self.extras_ui)
        self.extras_ui.ischange.emit()
        # self.extras_ui.clear_widget()
        # self.extras_ui.get_reminders()
    def loadHow(self):
        self.stacked_widget.setCurrentWidget(self.how_widget)
        # self.open_floating_chat()
        # self.test.send()
    def loadAbout(self):
        self.stacked_widget.setCurrentWidget(self.about_widget)
    def loadSettings(self):
        print("setttings clicked")
        audio_devices_object = GetAudioDevice()
        json_data_object = GetJsonData()
        audio_devices_dict = audio_devices_object.get_devices()
        self.settings_ui.audio_device.clear()
        for key , items in audio_devices_dict.items():
            print(key ,items)
            self.settings_ui.audio_device.addItem(items)
        self.settings_ui.audio_device.setCurrentIndex(json_data_object.input_audio_device_data())
        # self.settings_ui.wake_word_label.clear()
        self.settings_ui.wake_word_label.setText(json_data_object.get_wake_word())
        self.settings_ui.path_label.setText(json_data_object.get_music_path())
        self.stacked_widget.setCurrentWidget(self.settings_ui)
        if json_data_object.get_system_tray():
            self.settings_ui.tray_check_box.setChecked(True)
        else:
            self.settings_ui.tray_check_box.setChecked(False)

    def loadChats(self):
        self.chats_ui.delete_chats()
        self.chats_ui.load_previous_chat()
        self.stacked_widget.setCurrentWidget(self.chats_ui)
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
