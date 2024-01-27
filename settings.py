import json

saved_settings = {}

def get_user_inputs():
    global saved_settings
    get_settings_from_disk()

    print(
        "Input Test Settings - No User Input Will Use Last Known Value or Default Value"
    )
    get_input("Title")
    get_input("X Axis Label")
    get_input("Width")
    get_input("Height")
    get_input("Line Color")
    get_input("Theme")
    get_input("Tags")
    get_input("Host")
    get_input("Port")
    get_input("Interval")
    get_input("Test Length")

    return saved_settings


def get_input(field):
    global saved_settings
    saved_settings = get_settings_from_disk()
    new_val = input(f"{field} (Current: {saved_settings[field]}): ")
    if len(new_val) > 0:
        saved_settings[field] = new_val
        save_settings_to_disk()


def save_settings_to_disk():
    global saved_settings
    try:
        with open("./test_settings.json", "w") as saved_settings_file:
            json.dump(saved_settings, saved_settings_file)
    except FileNotFoundError as e:
        print (f"File Not Found {e}")

def get_settings_from_disk():
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
