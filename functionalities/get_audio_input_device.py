import pyaudio
import sounddevice as sd
class GetAudioDevice:
    def __ini__(self):
        pass
    def get_devices(self):
        audio_list = {}
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')

        for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                # print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
                audio_list[i] = p.get_device_info_by_host_api_device_index(0 ,i).get('name')

        return audio_list
    def get_deafult_device(self):
        default_input_device = sd.default.device[0]
        device_info = sd.query_devices(default_input_device ,'input')

        print("Default input device:")
        print(f"ID: {default_input_device}")
        print(f"Name: {device_info['name']}")


if __name__ =="__main__":
    object = GetAudioDevice()
    # print(object.get_devices())
    print(object.get_deafult_device())


