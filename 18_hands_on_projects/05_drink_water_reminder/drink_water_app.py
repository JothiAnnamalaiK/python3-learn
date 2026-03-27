# pip install rumps


import rumps
import subprocess
import threading
import time

INTERVAL = 1800  # 1800 seconds (1/2 hour) # 360 for 6 mins

SNOOZE_DURATION = 600  # 10 minutes in seconds
snz_dur_mins = SNOOZE_DURATION / 60  # in min
SNOOZE_DUR_INMINS = (
    f"{int(snz_dur_mins)}" if snz_dur_mins.is_integer() else f"{snz_dur_mins:.1f}"
)


SNOOOZE_TRIGGER_THRESHOLD = 300  # 5 minutes in seconds
snz_threshold_mins = SNOOOZE_TRIGGER_THRESHOLD / 60  # in min

SNOOOZE_TRIGGER_THRESHOLD_INMINS = (
    f"{int(snz_threshold_mins)}"
    if snz_threshold_mins.is_integer()
    else f"{snz_dur_mins:.1f}"
)

paused = False


class WaterReminderApp(rumps.App):
    def __init__(self):
        APP_TITLE = "Drinking Water Reminder"
        super(WaterReminderApp, self).__init__(APP_TITLE)

        self.pause_item = rumps.MenuItem("Pause", callback=self.pause_toggle)
        self.snooze_item = rumps.MenuItem(
            # "Snooze 10 min", callback=self.snooze
            f"Snooze {SNOOZE_DUR_INMINS} min",
            callback=self.snooze,
        )
        # self.snooze_item.set_enabled(False)  # initially disabled
        self.quit_item = rumps.MenuItem("Quit", callback=self.quit_app)

        # Assign menu items
        self.menu = [self.pause_item, self.snooze_item, self.quit_item]

        # Keep track of remaining seconds in instance
        self.remaining_seconds = INTERVAL
        self.snoozed = False  # track if snooze was used

        self.thread = threading.Thread(target=self.reminder_loop, daemon=True)
        self.thread.start()

    def notify(self, title, message):
        # macOS notification
        script = f'display notification "{message}" with title "{title}" sound name "default"'
        subprocess.run(["osascript", "-e", script])

    def reminder_loop(self):
        global paused
        while True:
            # Use self.remaining_seconds directly
            while self.remaining_seconds > 0:
                if not paused:
                    hrs = self.remaining_seconds // 3600
                    mins = (self.remaining_seconds % 3600) // 60
                    secs = self.remaining_seconds % 60
                    self.title = f"Next Reminder: {hrs:02d}:{mins:02d}:{secs:02d}"

                    # Snooze is handled via self.remaining_seconds in snooze function
                    if (
                        self.remaining_seconds <= SNOOOZE_TRIGGER_THRESHOLD
                        and not self.snoozed
                    ):
                        self.snooze_item.title = f"Snooze {SNOOZE_DUR_INMINS} min"

                    elif self.snoozed:
                        self.snooze_item.title = "Snoozed ⏱"
                    else:
                        self.snooze_item.title = f"Snooze {SNOOZE_DUR_INMINS} min"

                    time.sleep(1)
                    self.remaining_seconds -= 1  # decrement countdown
                else:
                    self.title = "Drink Water Reminder Paused ⏸"
                    time.sleep(1)

            # Time is up → notify
            if not paused:
                self.notify(
                    "Drinking water Reminder", "Hey buddy, Its time to drink water!"
                )
                self.snoozed = False

            # Reset countdown for next interval
            self.remaining_seconds = INTERVAL

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

    def snooze(self, sender):
        if self.remaining_seconds <= SNOOOZE_TRIGGER_THRESHOLD:
            if not self.snoozed:
                self.remaining_seconds += SNOOZE_DURATION  # add 10 minutes
                self.snoozed = True
                sender.title = "Snoozed ⏱"
                rumps.notification(
                    "Drinking Water Reminder",
                    "",
                    f"Snoozed {SNOOZE_DUR_INMINS} minutes",
                )
            else:
                rumps.notification(
                    "Drinking Water Reminder",
                    "",
                    "Already Snoozed — can only snooze once per reminder!",
                )
        else:
            rumps.notification(
                "Drinking Water Reminder",
                "",
                f"Snooze only available < {SNOOOZE_TRIGGER_THRESHOLD_INMINS} minutes left",
            )

    @rumps.clicked("Quit")
    def quit_app(self, _):
        rumps.quit_application()


if __name__ == "__main__":
    WaterReminderApp().run()
