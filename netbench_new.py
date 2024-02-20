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
import os
import select

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
        self._stdout_fd = os.dup(1)
        self._stderr_fd = os.dup(2)
        # redirect stdout
        os.dup2(self._pipe_in, 1 , inheritable=True)  # redirect stdout to pipe
        os.dup2(self._pipe_in, 2)  # stderr 

        self.output = []

    def start_test(self):
        print(f"TEST = {self._test}")
        self.worker_thread = Thread(
            target=self.run)
        self.worker_thread.start()
        self.force_print("BUTTTESS")
        self.pipe_reader()
        # self.worker_thread.join()
        # redirect pipe_in to stdout for visibility
        os.dup2(self._stdout_fd, 1)
        # os.dup2(stderr_fd, 2) # stdout

        print("ENDND")
        print(self.output) 

    def pipe_reader(self):
        self.force_print(f"WORKER THREAD ALIVE? {self.worker_thread.is_alive()}") 
        self.force_print(f"MORE DATA? {self.more_data()}")
        while self.worker_thread.is_alive():
            try:
                msg = b""
                # while self.more_data():
                msg = os.read(self._pipe_out, 1024) 
                msg = msg.decode('utf-8')
                self.output.append(msg)
                self.force_print(f"{msg}")
            except:
                self.force_print("ERROR")
                break
        self.force_print("LOOP DEAD")
        self.input_data_pipe.close() 

    def more_data(self):
        """Check if there is more data left on the pipe

        :param pipe_out: The os pipe_out
        :rtype: bool
        """
        r, _, _ = select.select([self._pipe_out], [], [], 0)
        return bool(r)

    def force_print(self, message):
        os.write(self._stdout_fd, message.encode())

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
