import time
from plyer import notification

import subprocess
import platform


def notify_on_mac(title, message):
    script = (
        f'display notification "{message}" with title "{title}" sound name "default"'
    )
    subprocess.run(["osascript", "-e", script])


def notify_on_windows(title, message):
    notification.notify(title=title, message=message, timeout=10)  # duration in seconds


def countdown(seconds):
    while seconds:
        hrs = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60

        timer = f"{hrs:02d}:{mins:02d}:{secs:02d}"
        print(f"\rNext reminder in: {timer}", end="")  # overwrite same line

        time.sleep(1)
        seconds -= 1
    print()  # move to next line after countdown finishes


# set your interval (e.g., 1 hour = 3600 seconds)
INTERVAL = 1800  # change to 3600 for 1 hour

try:
    # print("platform.system(): ", platform.system())
    title = "Drinking water Reminder"
    message = "Hey Jothi, Its time to drink water!"
    while True:
        if platform.system() == "Darwin":
            notify_on_mac(title, message)
        else:
            notify_on_windows(title, message)

        countdown(INTERVAL)

        # time.sleep(10)  # Sleep for 1 hour (3600 seconds)
except KeyboardInterrupt:
    print("\nStopped by user")
