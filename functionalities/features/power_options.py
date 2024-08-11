import os
class PowerOptions:
    def __init__(self):
        pass
    def shutdown(self):
        os.system("shutdown /s /t 1")
    def sleep(self):
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    def signout(self):
        os.system("shutdown /l")
if __name__ == "__main__":
    obj = PowerOptions()
    obj.sleep()