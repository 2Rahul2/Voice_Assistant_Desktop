
import json
import os
from pathlib import Path

# from test_files.getAppDataPath import get_app_data_directory
class GetJsonData:
    def __init__(self):
        self.json_file_path = self.get_directory() /'json_file.json'
        self.default_wake_word = "noodle"
        if not self.path_exists():
            self.create_directory()
        if not Path(self.json_file_path).is_file():
            try:
                print("creating json file")
                with open(self.json_file_path,'w') as f:
                    json.dump({'wake_word':'Nikki' ,'music_path':'' , 'start_index': 1, 'end_index': 0, 'reminder': [] ,'music_name':"" ,'is_system_tray':True ,'music_name':''}, f)
            except Exception as e:
                print("Error while creating json file: " ,e)
    def get_directory(self):
        return Path(os.getenv('APPDATA'))/'VoiceAssistant'
    def create_directory(self):
        directory = self.get_directory()
        if not os.path.exists(directory):
            os.mkdir(directory)
    def path_exists(self):
        if os.path.exists(self.get_directory()):
            return True
        return False
    
    
    # Get all json data / read json data
    def get_music_name(self):
        try:
            with open(self.json_file_path ,'r') as f:
                data = json.load(f)
                return data['music_name']
        except:
            return None
    def get_message_index(self):
        try:
            with open(self.json_file_path ,'r') as f:
                data = json.load(f)
                return data['start_index'] ,data['end_index']
        except:
            return 0 , 0
    def get_system_tray(self):
        try:
            with open(self.json_file_path ,'r') as f:
                data = json.load(f)
                return data['is_system_tray']
        except:
            return True
    def get_wake_word(self):
        try:
            with open(self.json_file_path ,'r') as f:
                data = json.load(f)
                return data['wake_word']
        except:
            return self.default_wake_word
        
    def get_music_path(self):
        try:        
            with open(self.json_file_path , 'r') as f:
                data = json.load(f)
                return data['music_path']
        except:
            return ""
    def input_audio_device_data(self):
        try:
            with open(self.json_file_path ,'r') as f:
                data = json.load(f)
                return data['input_audio_index']
        except:
            return 0

    # def music_name_data(self):
    #     try:
    #         with open(self.json_file_path ,'r') as f:
    #             data = json.load(f)
    #             return data['name']
    #     except:
    #         return ""

    def get_all_data(self):
        try:
            with open(self.json_file_path ,'r') as f:
                data = json.load(f)
                return data
        except:
            return
        
    def get_reminder_data(self):
        try:
            with open(self.json_file_path ,'r') as f:
                data = json.load(f)
                return data['reminder']
        except:
            return {}
        
    # write json data
    def write_music_name(self , index):
        try:
            with open(self.json_file_path ,"r") as f:
                data = json.load(f)
                print(data)
        except:
            data = {}
        try:
            with open(self.json_file_path ,'w') as f:
                data["music_name"] = index
                json.dump(data ,f)
        except Exception as e:
            print("could not save music name : " ,e)

    def write_reminder(self ,lst):
        try:
            with open(self.json_file_path ,"r") as f:
                data = json.load(f)
                print(data)
        except:
            data = {}
        try:
            with open(self.json_file_path ,'w') as f:
                data['reminder'] = lst
                json.dump(data ,f)
        except Exception as e:
            print("could not save reminder : " ,e)

    def write_reminder_data(self, job_id="",time="12:00:00" ,days = None , date = None ,message = "Unknown Reminder",every_day=None):
        try:
            with open(self.json_file_path ,"r") as f:
                data = json.load(f)
                print(data)
        except:
            data = {}
        try:
            with open(self.json_file_path ,'w') as f:
                # if not data['reminder']:
                # data['reminder'] = []
                    # json.dump(data ,f)

                data['reminder'].append({
                    "job_id":job_id,
                    "time":time,
                    'days':days,
                    'every_day':every_day,
                    'message':message,
                    'date':date
                })
                json.dump(data ,f)
        except Exception as e:
            print("could not save reminder : " ,e)
    def write_input_audio_device(self ,index):
        try:
            with open(self.json_file_path ,'r') as f:
                data = json.load(f)
        except:
            data = {}
        with open(self.json_file_path ,"w") as f:
            data['input_audio_index'] = index
            json.dump(data , f)
        
    # def write_music_name(self ,name):
    #     try:
    #         with open(self.json_file_path ,'r') as f:
    #             data = json.load(f)
    #     except:
    #         data = {}
    #     with open(self.json_file_path ,"w") as f:
    #         data['music_name'] = name
    #         json.dump(data , f)
    def write_music_path(self ,path):
        try:
            with open(self.json_file_path ,"r") as f:
                data = json.load(f)
        except:
            data = {}
        try:
            with open(self.json_file_path ,'w') as f:
                data['music_path'] = path
                json.dump(data ,f)
        except:
            pass

    def write_system_tray(self ,check):
        try:
            with open(self.json_file_path ,'r') as f:
                data = json.load(f)
        except:
            data = {}
        with open(self.json_file_path ,"w") as f:
            data['is_system_tray'] = check
            json.dump(data , f)
    def write_message_index(self ,start_index=1 , end_index=0):
        try:
            with open(self.json_file_path ,'r') as f:
                data = json.load(f)
        except:
            data = {}
        with open(self.json_file_path ,"w") as f:
            data['start_index'] = start_index
            data['end_index'] = end_index
            json.dump(data , f)
    def write_wake_word(self , word):
        try:
            with open(self.json_file_path , 'r') as f:
                data = json.load(f)
        except Exception as e: 
            data = {}
            print(e)
        try:
            with open(self.json_file_path , 'w') as f:
                data['wake_word'] = word
                json.dump(data, f)
                print("updated wake word")
        except Exception as e:
            print("Error while writting wake word : " ,e)
            
if __name__ == "__main__":
    object = GetJsonData()
    # object.write_input_audio_device(1)
    print(object.get_reminder_data())

