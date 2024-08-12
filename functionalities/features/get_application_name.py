import psutil
from functionalities.features.check_similarity import similar
try:
    from AppOpener import open
except:
    pass

class Application:
    def __init__(self):
        self.action_keywords = ["open", "launch", "start", "run"]
        self.close_action_keywords = ['close' ,'exit' ,'quit' ,'abolish' ,'off']
        self.app_keywords = ["application", "app", "program", "software"]
        self.stop_words = ["the", "a", "an", "please"]

    def extract_application_name(self , text):
        try:
            concat_words = self.action_keywords+self.app_keywords+self.stop_words+self.close_action_keywords
            filtered_lst = []
            for word in text.split():
                if word not in concat_words:
                    filtered_lst.append(word)
            return " ".join(filtered_lst)
        except:
            pass
    
    def open_application(self,text):
        try:
            app_name = self.extract_application_name(text)
            open(app_name ,match_closest=True)
            print(f"opening application : {app_name.replace(' ' ,'')}.exe")
        except:
            pass
    def close_application(self , text):
        try:
            app_name = self.extract_application_name(text)
            similar_object = similar(app_name.lower())
            print(f"closing application : {app_name.replace(' ' ,'')}.exe")
            for proc in psutil.process_iter(['pid', 'name']):
                try:

                    is_similiar ,val = similar_object.checkSimilar(proc.info['name'].lower() ,0.75)
                    print(app_name.lower() , proc.info['name'].lower() ,val)
                    # Check if the process name matches the given application name
                    if is_similiar:
                    # if app_name.lower() in proc.info['name'].lower():
                        # Terminate the process
                        print(f"{proc.info['name'].lower()} (PID {proc.info['pid']}) terminated successfully.")
                        proc.terminate()
                except Exception as e:
                    print("cant find application" ,e)
                    pass
        except:
            pass

if __name__ == "__main__":
    app = Application()
    app.close_application("Hoyoplay.exe")

