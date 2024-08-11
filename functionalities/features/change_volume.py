from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import re
# Function to set the volume
class Volume:
    def __init__(self):
        pass

    def extract_numbers(self ,text):
        numbers = re.findall(r'\d+', text)
        lst =  [int(num) for num in numbers]
        if len(lst)!=0:
            self.set_volume(lst[-1]/100)
    def set_volume(self ,volume):
        volume = max(0.0, min(volume, 1.0)) 
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_object = cast(interface, POINTER(IAudioEndpointVolume))
        volume_object.SetMasterVolumeLevelScalar(volume, None)
    def get_volume(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_object = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume_object.GetMasterVolumeLevelScalar()
        return current_volume
    def lower_volume(self):
        self.set_volume(self.get_volume()-0.1)
    def increase_volume(self):
        self.set_volume(self.get_volume()+0.1)

# Example usage (adjust volume to 50%)
if __name__ == "__main__":
    vol = Volume()
    text1 = "set volume to 15"
    vol.extract_numbers(text1)
