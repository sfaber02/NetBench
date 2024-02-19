import subprocess
# from bokeh.models import ColumnDataSource
# from bokeh.plotting import curdoc, figure
import re
# from colorama import Fore
from settings import get_user_inputs, get_settings_from_disk
from datetime import datetime
from iperf import Client
from threading import Thread
import sys


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

class NetBench(Client):
    def __init__(self):
        super().__init__()
        self.worker_thread: Thread = Thread(
            target=self.run())

    def start_test(self):
        self.worker_thread.start()


def main():
    netbench = NetBench()
    netbench.server_hostname = "192.168.50.98"
    netbench.port = 5201
    netbench.duration = 60
    netbench.test_reporter_interval = 0.1
    netbench.test_stats_interval = 0.1 
    netbench.json_output = True 
    netbench.json_stream_output = 1

    netbench.start_test()








main()
