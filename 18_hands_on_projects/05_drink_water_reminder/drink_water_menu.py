# pip install rumps


import rumps
import subprocess
import threading
import time

INTERVAL = 300  # seconds (1/2 hour)
paused = False


class WaterReminderApp(rumps.App):
    def __init__(self):
        APP_TITLE = "Drinking Water Reminder"
        super(WaterReminderApp, self).__init__(APP_TITLE)
        self.menu = ["Pause", "Snooze 10 min"]
        self.thread = threading.Thread(target=self.reminder_loop, daemon=True)
        self.thread.start()

    def notify(self, title, message):
        # macOS notification
        script = f'display notification "{message}" with title "{title}" sound name "default"'
        subprocess.run(["osascript", "-e", script])

    def reminder_loop(self):
        global paused
        while True:
            seconds = INTERVAL
            while seconds > 0:
                if not paused:
                    hrs = seconds // 3600
                    mins = (seconds % 3600) // 60
                    secs = seconds % 60
                    self.title = f"Next Reminder: {hrs:02d}:{mins:02d}:{secs:02d}"
                    time.sleep(1)
                    seconds -= 1
                else:
                    self.title = "Drink Water Reminder Paused ⏸"
                    time.sleep(1)
            if not paused:
                self.notify(
                    "Drinking water Reminder", "Hey Jothi, Its time to drink water!"
                )

    # Menu actions
    @rumps.clicked("Pause")
    def pause_toggle(self, sender):
        global paused
        paused = not paused
        sender.title = "Resume" if paused else "Pause"
        rumps.notification(
            "Drinking Water Reminder", "", "Paused" if paused else "Resumed"
        )
        # self.notify("Drinking Water Reminder", "Paused" if paused else "Resumed")

    def snooze(self):
        global INTERVAL
        if INTERVAL < 300:  # Check if time is below 5 minutes
            INTERVAL += 60  # Add 10 minutes (600 seconds)
            self.menu["Snooze 10 min"].set_callback(None)  # Disable snooze
            rumps.notification("Drinking Water Reminder", "", "Snoozed 10 minutes")

    @rumps.clicked("Quit")
    def quit_app(self, _):
        rumps.quit_application()


if __name__ == "__main__":
    WaterReminderApp().run()
