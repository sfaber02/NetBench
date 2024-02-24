import json

saved_settings = {}


class Settings:
    def __init__(self):
        self.get_settings_from_disk()

    def get_user_inputs(self):
        print(
            "Input Test Settings - No User Input Will Use Last Known Value or Default Value"
        )
        self.get_input("Title")
        self.get_input("X Axis Label")
        self.get_input("Width")
        self.get_input("Height")
        self.get_input("Line Color")
        self.get_input("Theme")
        self.get_input("Tags")
        self.get_input("Host")
        self.get_input("Port")
        self.get_input("Interval")
        self.get_input("Test Length")

        return saved_settings

    def get_input(self, field):
        new_val = input(f"{field} (Current: {self.saved_settings[field]}): ")
        if len(new_val) > 0:
            self.saved_settings[field] = new_val
            self.save_settings_to_disk()

    def save_settings_to_disk(self):
        try:
            with open("./test_settings.json", "w") as saved_settings_file:
                json.dump(self.saved_settings, saved_settings_file)
        except FileNotFoundError as e:
            print(f"File Not Found {e}")

    def get_settings_from_disk(self):
        try:
            with open("./test_settings.json", "r") as saved_settings_file:
                self.saved_settings = json.load(saved_settings_file)
        except FileNotFoundError:

            print("No settings file found, creating one with default settings.")
            self.saved_settings = {
                "Title": "Bandwidth vs Time",
                "X Axis Label": "Time in Seconds",
                "Width": 800,
                "Height": 600,
                "Line Color": "white",
                "Theme": "dark_minimal",
                "Tags": [],
                "Host": "127.0.0.1",
                "Port": "5201",
                "Interval": "0.1",
                "Test Length": "60",
            }
            with open("./test_settings.json", "w") as saved_settings_file:
                json.dump(self.saved_settings, saved_settings_file)
