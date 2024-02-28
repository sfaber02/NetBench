import subprocess
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
import re
from colorama import Fore
from settings import get_user_inputs, get_settings_from_disk
from iperf import Client
import threading
import sys
import json

# store subprocess
process = None
worker_thread = None
# Create column data source for plot
source = ColumnDataSource(dict(x=[], y=[]))
# store settings
settings = get_settings_from_disk()
iperf_client: Client


# Redirect stdout to our own stream.
class MyStream:
    def write(self, text):
        # This is where we can parse the output and do what we need with it.
        # print(f"Intercepted text: {text}", end="")
        # print(f"Intercepted text: {text}", end="", flush=True)
        message = "BUTTES"
        sys.__stdout__.write(message)
        # num_bytes = float(text["data"]["streams"]["bytes"], 0.0)
        # sys.__stdout__.write(f"djdsklfjdskf {num_bytes}")
        # dict(x=[data_x], y=[data_y])

    def flush(self):
        # Redirect to the original standard output
        return sys.__stdout__.flush()


sys.stdout = MyStream()


def start():
    global settings
    global iperf_client

    # change_user_inputs = input("Change Test Settings? (Y or N)")
    # if change_user_inputs == "y" or change_user_inputs == "Y":
    # settings = get_user_inputs()

    # print(f"\033[32mTesting on host {settings['Host']}, port {settings['Port']}")

    # #get current timestamp

    # #combine timestamp with title
    iperf_client = Client()
    iperf_client.server_hostname = "192.168.50.98"
    iperf_client.port = 5201
    iperf_client.duration = 60
    iperf_client.test_reporter_interval = 0.1

    iperf_client.test_stats_interval = 0.1
    # print(iperf_client)
    iperf_client.json_output = True
    iperf_client.json_stream_output = 1

    # Create plot
    plot = figure(
        title=title_with_timestamp,
        title="YAY",
        x_axis_label=settings["X Axis Label"],
        y_axis_label="Mbits / sec",
    )

    update()


def update():
    global settings
    global process
    global source
    global worker_thread
    global iperf_client
    try:
        if worker_thread is None:
            # command = [
            # "iperf3",
            # "-c",
            # settings["Host"],
            # "-p",
            # settings["Port"],
            # "-i",
            # settings["Interval"],
            # "-t",
            # settings["Test Length"],
            # "-f",
            # "m",
            # "--forceflush",
            # ]
            # process = subprocess.Popen(command, stdout=subprocess.PIPE)
            worker_thread = threading.Thread(target=iperf_client.run())
            worker_thread.start()
        # line = process.stdout.readline().decode().strip()
        # parse data here
        # data_x, data_y = parse_line(line)
        # source.stream(dict(x=[data_x], y=[data_y]))
    except ParseException as e:
        print(f"\033[31m{e.message}, line = {e.line}")
        print(Fore.GREEN)
    except UnboundLocalError as e:
        print(f"\033[31mUnbound Local Error- line has no value")
        print(Fore.GREEN)


def parse_line(line):
    # Regular expression to match time and speed
    # maybe new regex r"\[\s*\d+\]\s*([\d.]+)-([\d.]+)\s*sec.*\s*([\d.]+)\s*M?bits/sec"
    match = re.search(
        r"\[\s*\d+\]\s*([\d.]+)-([\d.]+)\s*sec.*\s([\d.]+)\s*Mbits/sec", line
    )

    if match:
        end_time = float(match.group(2))
        speed = float(match.group(3))

        return end_time, speed

    else:
        raise ParseException("Cannot Parse (probably start or end of data)", line)


class ParseException(Exception):
    def __init__(self, message, line):
        self.line = line
        self.message = message
        super().__init__(message)


start()
