import speech_recognition
import pyttsx3
import threading

from mic_icon_popup import FloatingWindow

# from functionalities.features.alarm import alarm
from functionalities.features.get_application_name import Application
from PyQt5.QtCore import pyqtSignal, QObject
from functionalities.reminder.trigger_reminder import TriggerReminder
from functionalities.features.change_volume import Volume
from functionalities.features.play_music import PlayMusic
from functionalities.rw_json_data import GetJsonData
from functionalities.features.power_options import PowerOptions
class VoiceListener(QObject):
    command_text = pyqtSignal(str)
    chat_command = pyqtSignal(str)
    wake_detected = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.recognizer = speech_recognition.Recognizer()
        self.wake_word_detected = False
        self.json_object = GetJsonData()
        self.wake_word = self.json_object.get_wake_word()
        self.wakeWord = [
            "okay Niki",
            "okay Nikki",
            "ok niki",
            "ok nikki",
        ]


        # perform application task
        self.open_action_keywords = ["open", "launch", "start", "run"]
        self.close_action_keywords = ['close' ,'exit' ,'quit' ,'abolish' ,'off']

        self.up_volume_keywords = ['increase volume' ,'upper volume']
        self.down_volume_keywords = ['decrease volume' ,'lower volume']

        self.play_songs_keywords = ['play music' ,'play song' ,'play random' ,'random song','random music']
        self.play_next_keywords = ['play next music' ,'play next song' ,'next music' ,'next song' ,'next']
        self.play_previous_keywords = ['play previous music' ,'play previous song' ,'previous music' ,'previous song' ,'previous']
        self.pause_play_keywords = ['play' ,'resume','stop' ,'pause']

        self.signout_keywords = ["sign out" ,"signout"]
        self.shutdown_keywords = ["shutdown" ,"shut down"]

        
    def contains_wake_word(self ,text):
        print(f"text is {text}")
        if not text.strip():
            return False
        if text.lower() in self.wake_word.lower():
            self.wake_detected.emit()
            return True
        
        # if self.default_word:
        for word in self.wakeWord:
            if text in word:
                # print(text , True)
                self.wake_detected.emit()
                return True
        return False

    def listen_for_wake_word(self):
        with speech_recognition.Microphone() as mic:
            self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening for wake word...")
            audio = self.recognizer.listen(mic)
            
            try:
                text = self.recognizer.recognize_google(audio).lower()
                return text
            except speech_recognition.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except speech_recognition.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
        

    def listen_for_command(self):
        # self.floating_window = FloatingWindow()
        # self.floating_window.show_floating_window()
        with speech_recognition.Microphone() as mic:
            self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening for command...")
            audio = self.recognizer.listen(mic)
            
            try:
                text = self.recognizer.recognize_google(audio).lower()
                return text
            except speech_recognition.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except speech_recognition.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
    def run_voice(self):
        while True:
            self.wake_word_detected = False
            wake_word_text = ""
            while not self.wake_word_detected:
                wake_word_text = self.listen_for_wake_word()
                self.wake_word_detected = self.contains_wake_word(wake_word_text)
                
            
            
            print(f"Wake word detected: {wake_word_text}")
            # Listen for command
            voice_command_text = self.listen_for_command()
            self.command_text.emit(voice_command_text)
            print(f"Command: {voice_command_text}")
            
    def run_commands(self , command_text=""):
            # Process the command
            # Add your command processing logic here
            if 'set reminder' in command_text:
                reminder_object = TriggerReminder()
                reminder_object.get_reminder_voice(command_text)
                # alarm_object = alarm()
                # timeObject = alarm_object.extract_time(command_text)
                # if timeObject is None:
                #     print("At what Time?")
                #     alarm_text = self.listen_for_command()
                #     # print(f"alarm time is :{alarm_text}")
                #     timeObject = alarm_object.extract_time(alarm_text)
                #     print(timeObject)
                    
            elif any(word in command_text for word in self.open_action_keywords):
                # open application
                app_name = Application()
                app_name.open_application(command_text)
            elif any(word in command_text for word in self.close_action_keywords):
                # close application
                app_name = Application()
                app_name.close_application(command_text)
            elif any(word in command_text for word in self.up_volume_keywords):
                volume = Volume()
                volume.increase_volume()
            elif any(word in command_text for word in self.down_volume_keywords):
                volume = Volume()
                volume.lower_volume()
            elif "set volume" in command_text.lower():
                volume = Volume()
                volume.extract_numbers(command_text)
            elif "search" in command_text:
                self.chat_command.emit(command_text.replace("search" ,""))
            elif any(word in command_text for word in self.play_songs_keywords):
                music = PlayMusic()
                music.random_music()
            elif any(word in command_text for word in self.play_next_keywords):
                music = PlayMusic()
                music.forward()
            elif any(word in command_text for word in self.play_previous_keywords):
                music = PlayMusic()
                music.previous()
            elif any(word in command_text for word in self.pause_play_keywords):
                music = PlayMusic()
                music.pause_play()
            elif "sleep" in command_text:
                power_options = PowerOptions()
                power_options.sleep()
            elif any(word in command_text for word in self.shutdown_keywords):
                power_options = PowerOptions()
                power_options.shutdown()
            elif any(word in command_text for word in self.signout_keywords):
                power_options = PowerOptions()
                power_options.signout()
            elif "exit" in command_text:
                print("Exiting...")
                
            
            # Reset wake_word_detected to False to listen for the wake word again
            self.wake_word_detected = False
            print("end")

if __name__ == "__main__":
    object = VoiceListener()
    object.run_voice()