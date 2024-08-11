import sounddevice as sd
class SetAudioDevice:
    def __init__(self):
        pass

    def set_device(self , index):
        # sd.default.device = (index ,sd.default.device[1])
        pass


if __name__ == "__main__":
    object = SetAudioDevice()
    # object.set_device(2)
    current_default_input = sd.default.device[0]
    device_info = sd.query_devices(current_default_input, 'input')
    print("New default input device:")
    print(f"ID: {current_default_input}")
    print(f"Name: {device_info['name']}")