import json
from typing import Dict, Union, Optional, List
from datetime import datetime


class Settings:
    def __init__(self):
        self.settings: Dict[str, Union[str, int]] = self.get_settings_from_disk()
        self.get_user_inputs()

    def get_user_inputs(self) -> None:
        print(
            "Input Test Settings - No User Input Will Use Last Known Value or Default Value"
        )
        self.fields: List[str] = [
            "Title",
            "X Axis Label",
            "Width",
            "Height",
            "Line Color",
            "Theme",
            "Tags",
            "Host",
            "Port",
            "Interval",
            "Test Length",
        ]

        for field in self.fields:
            self.get_input(field)

    def get_input(self, field) -> None:
        new_val = input(f"{field} (Current: {self.settings[field]}): ")
        if len(new_val) > 0:
            self.settings[field] = new_val
            self.save_settings_to_disk()

    def save_settings_to_disk(self) -> None:
        try:
            with open("./test_settings.json", "w") as saved_settings_file:
                json.dump(self.settings, saved_settings_file)
        except FileNotFoundError as e:
            print(f"File Not Found {e}")

    def get_settings_from_disk(self) -> Dict[str, Union[str, int]]:
        try:
            with open("./test_settings.json", "r") as saved_settings_file:
                saved_settings = json.load(saved_settings_file)
        except FileNotFoundError:
            print("No settings file found, creating one with default settings.")
            saved_settings = {
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
                json.dump(saved_settings, saved_settings_file)

        return saved_settings

    def get_title(self, title) -> str:
        current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{title} - {current_timestamp}"
