import json
import os
from pathlib import Path
from functionalities.rw_json_data import GetJsonData
class ChatJsonData:
    def __init__(self):
        # from rw_json_data import GetJsonData
        self.json_file_path = self.get_directory() /'chat_json_file.json'
        # self.default_wake_word = "noodle"
        self.limit = 4
        if not self.path_exists():
            self.create_directory()
            try:
                with open(self.json_file_path,'w') as f:
                    json.dump({"reminder":[] , "message":[]} , f)
                # json_data_object = GetJsonData()
                # json_data_object.write_message_index(1 , 0)
            except:
                pass
        if not Path(self.json_file_path).is_file():
            try:
                print("creating chat json file")
                with open(self.json_file_path,'w') as f:
                    json.dump({"reminder":[]  , "message": []} , f)
                # json_data_object = GetJsonData()
                # json_data_object.write_message_index(1 , 0)
                
            except Exception as e:
                print("(file : chat_json_data.py : 29) Error while creating chat json file: " ,e)
                
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
    
    # read chats data
    def read_chat(self):
        try:
            with open(self.json_file_path ,'r') as f:
                data = json.load(f)
                # print(data)
            return data['message']
        except Exception as e:
            print("(file : chat_json_data.py : 50) Error while reading chats : " ,e)
        return []



    #write chats data
    def write_chat(self,user="..." , assistant="..."):
        try:
            with open(self.json_file_path ,'r') as f:
                data = json.load(f)
        except Exception as e:
            print("(file : chat_json_data.py : 61) reading chat error : " ,e)
            data = {}
        try:
            with open(self.json_file_path ,'w') as f:
                size = len(data['message'])
                if size > self.limit:
                    data['message'].pop(0)
                data['message'].append({"assistant":assistant,"user":user})
                json.dump(data ,f)
                # storing only 10 instances of chats
                # json_data_object = GetJsonData()
                # print("akjvbehvk")
                # start_index , end_index = json_data_object.get_message_index()
                # print("or here")
                # data[str(end_index%5)] = [user , assistant]
                # if end_index < start_index:
                    # start_index = (start_index+1)%5
                # end_index = (end_index+1)%5
                # json_data_object.write_message_index(start_index , end_index)
                # print(start_index , end_index)
                # print(data)
        except Exception as e:
            print(e)
if __name__ == "__main__":
    object = ChatJsonData()
    json_object = GetJsonData()
    data = object.read_chat()
    # object.write_chat("lol" ,"bhow")
    print(data)
    print(json_object.get_message_index())

    # for key ,value in data.items():

    # print(len(object.read_chat()))