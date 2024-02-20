import subprocess
# from bokeh.models import ColumnDataSource
# from bokeh.plotting import curdoc, figure
import re
# from colorama import Fore
from settings import get_user_inputs, get_settings_from_disk
from datetime import datetime
from iperf import Client, TestResult
from threading import Thread
import sys
from multiprocessing import Pipe

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
    # def flush(self):
        # # Redirect to the original standard output
        # return sys.__stdout__.flush()

# sys.stdout = MyStream()

class NetBench(Client):
    def __init__(self):
        super().__init__()
        self.input_data_pipe, self.output_data_pipe = Pipe()
        self.worker_thread: Thread

    def start_test(self):
        self.worker_thread = Thread(
            target=self.run()) # args=(self.input_data_pipe,))
        self.worker_thread.start()

        # self.worker_thread.join()
        
        # print(self.output_data_pipe.recv())

def main():
    netbench = NetBench()
    netbench.server_hostname = "192.168.50.98"
    netbench.port = 5201
    netbench.duration = 3
    netbench.test_reporter_interval = 0.1
    netbench.test_stats_interval = 0.1 
    netbench.json_output = True 
    netbench.json_stream_output = 1

    netbench.start_test()
    # print(result)








main()
