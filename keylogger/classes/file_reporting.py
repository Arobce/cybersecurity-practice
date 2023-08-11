class FileReporting:
    filename = ""

    def update_filename(self, start_date, end_date):
        # filename by start and end datetimes
        start_date = str(start_date)[:-7].replace(" ", "-").replace(":", "")
        end_date = str(end_date)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_date}_{end_date}"

    def report(self, start_date, end_date, message):
        self.update_filename(start_date, end_date)

        # Creates a log file in the current directory
        with open(f"{self.filename}.txt", "w") as f:
            print(message, file=f)

        print(f"[{self.filename}] - {message}")

        print(f"[+] Saved {self.filename}.txt")
