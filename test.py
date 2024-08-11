import subprocess

def toggle_bluetooth(state):
    try:
        if state == 'on':
            # First, check if the service is running
            result = subprocess.run(['powershell', '-Command', "(Get-Service bthserv).Status"], capture_output=True, text=True)
            if 'Running' not in result.stdout:
                # Start the service if it's not already running
                subprocess.run(['powershell', '-Command', "Start-Service bthserv"], check=True)
                print("Bluetooth service started.")
            else:
                print("Bluetooth service is already running.")
        elif state == 'off':
            # Stop the service
            subprocess.run(['powershell', '-Command', "Stop-Service bthserv"], check=True)
            print("Bluetooth service stopped.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to toggle Bluetooth service: {e}")

# Example usage:
toggle_bluetooth('on')
