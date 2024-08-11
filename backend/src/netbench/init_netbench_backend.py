import json
import sys
from netbench import Netbench

def main():
    # Example settings, replace with actual settings as needed
    settings = {
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


    # Instantiate Netbench with the settings
    netbench_instance = Netbench(settings, web=True)

    netbench_instance.log("Netbench Initialized")


main()
