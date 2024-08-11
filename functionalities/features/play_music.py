import os
import subprocess

from pywinauto.application import Application
from functionalities.rw_json_data import GetJsonData
import random

from functionalities.features.check_similarity import similar
# from create_music_json_file import JsonPath
class PlayMusic:
    def __init__(self):
        self.json_object = GetJsonData()
        self.music_folder_path = self.json_object.get_music_path()

    def pause_play(self):
        try:
            app = Application().connect(title="Groove Music" ,found_index =0)
            groove_music = app.window_()
            groove_music.type_keys('{SPACE}')
        except:
            print("Could not play/resume music")
            pass
        # groove_music.set_focus()
        # time.sleep(1)
        # pyautogui.press('space')  
    def get_current_music_index(self):
        json_object = GetJsonData()
        if os.path.exists(self.music_folder_path):
            current_name = json_object.get_music_name()
            music_files = os.listdir(self.music_folder_path)
            current_index = music_files.index(current_name)
            return current_index
        # else:
        #     json_object.create_directory() 
        #     music_files = os.listdir(self.music_folder_path)
        #     current_index = music_files.index(current_name)
            # next_index = current_index + 1 % len(music_files)
            # json_object.create_update_json({'name':music_files[next_index]})

        return None
            # json_object.create_update_json({"name":"current_music.mp3"})
    def forward(self):
        json_object = GetJsonData()
        current_index = self.get_current_music_index()
        if current_index:
            print("nxt music")
            music_files = os.listdir(self.music_folder_path)
            next_index = current_index - 1 % len(music_files)
            self.play_music_with_default_player(music_files[next_index])
            json_object.write_music_name(music_files[next_index])
        else:
            print("playing random music")
            self.random_music()
            # play random song
    def previous(self):
        json_object = GetJsonData()
        current_index = self.get_current_music_index()
        if current_index:
            music_files = os.listdir(self.music_folder_path)
            next_index = current_index + 1 % len(music_files)
            self.play_music_with_default_player(music_files[next_index])
            json_object.write_music_name(music_files[next_index])
        else:
            self.random_music()
    def random_music(self):
        json_object = GetJsonData()
        if os.path.exists(self.music_folder_path):
            music_files = os.listdir(self.music_folder_path)
            index = random.randint(0 ,len(music_files)-1)
            self.play_music_with_default_player(music_files[index])
            json_object.write_music_name(music_files[index])

    def play_music_with_default_player(self  ,music_name):
        # Get a list of all files in the folder
        higherPriority = 0
        files = os.listdir(self.music_folder_path)
        similar_object = similar(music_name)
        music_file = ""
        for file in files:
            print(file)
            is_similar , similar_value = similar_object.checkSimilar(file , 0.80)
            if is_similar:
                if similar_value > higherPriority:
                    music_file = file
                    higherPriority = similar_value
        # Filter out non-music files (assuming you have .mp3 files)
        music_files = [file for file in files if file.endswith('.mp3')]
        if music_file == "":
            print("No music files found in the specified folder.")
            return
        music_path = os.path.join(self.music_folder_path, music_file)

            # Open the music file with the default player
        try:
            subprocess.run(['start', music_path], shell=True)
        except:
            print("can't runt the audio")

if __name__ == "__main__":
    # Replace 'your/music/folder/path' with the actual path to your music folder
    folder_path = 'F:\music'

    # s = similar('ambient.mp3')
    # print(s.checkSimilar('ambient2.mp3' ,0.8))
    obj = PlayMusic()
    obj.random_music()
    # obj.play_music_with_default_player("ambent2.mp3")
