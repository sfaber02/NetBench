import subprocess
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
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
import json
from collections import deque
import time


class NetBench(Client):
    def __init__(self):
        # iperf python client base class
        super().__init__()
        # pipe for json stream test data from iperf
        self.input_data_pipe, self.output_data_pipe = Pipe()
        # thread to run test
        self.worker_thread: Thread
        # thread to read pipe
        self.pipe_thread: Thread
        # thread to plot graph
        self.graph_thread: Thread
        # store original stdout for later
        self._stdout_fd = os.dup(1)
        self._stderr_fd = os.dup(2)
        # redirect stdout
        os.dup2(self._pipe_in, 1 , inheritable=True)
        # os.dup2(self._pipe_in, 2)  # stderr 



        # column data for bokeh
        self.column_data = ColumnDataSource(dict(x=[], y=[]))
        self.plot_queue = deque()
        self.plot =  figure(
            title="title",
            x_axis_label="WHAT",
            y_axis_label="Mbits / sec",
        )
        self.plot.width = 800 
        self.plot.height = 600
        self.plot.line(x="x", y="y", source=self.column_data)
        self.curdoc = curdoc()
        self.curdoc.add_root(self.plot)
 

    def start_test(self):
        # start iperf test 
        self.worker_thread = Thread(
            target=self.run)
        self.worker_thread.start()

        # start pipe worker
        self.pipe_thread = Thread(target=self.pipe_reader)
        self.pipe_thread.start()
        # self.graph_reader()
        self.graph_thread = Thread(target=self.start_graph)
        self.graph_thread.start()

        self.force_print("All Threads Started! Commencing Test")


    def pipe_reader(self):
        while self.worker_thread.is_alive():
            try:
                msg = b""
                msg = os.read(self._pipe_out, 1024) 
                if msg:
                    msg = msg.decode('utf-8')
                    data_tuple = self.parse_pipe_data(msg)
                    if data_tuple: self.plot_queue.append(data_tuple)               
                    # self.force_print(f"queue len = {len(self.plot_queue)}")
                else:
                    self.force_print("EMPTY MSG")
            except:
                self.force_print("ERROR")
                break
        self.force_print("LOOP DEAD")
        os.close(self._pipe_in)
        os.close(self._pipe_out)

    def update_graph(self):
        try:
            x, y = self.plot_queue.popleft()
            self.force_print(f"x = {x} y = {y}")
            self.column_data.stream(dict(x=[x], y=[y]))
        except IndexError as e:
            pass

    def start_graph(self):
        self.curdoc.add_periodic_callback(self.update_graph, 0.2)

    def parse_pipe_data(self, data):
        try:
            data_dict = json.loads(data)
        except:
            data_dict = {}
            return None             # self.force_print("bad json")

        try:
            data = data_dict.get("data", {})
            packet_sums = data.get("sum", {})
            if packet_sums:
                bits_per_second = packet_sums.get("bits_per_second", 0.0)
                end_time = packet_sums.get("end", 0.0)

                return (end_time, bits_per_second)
        except (KeyError, IndexError) as e:
            self.force_print(f"BAD THING {e}")
            return None

    def force_print(self, message):
        message = message + "\n"
        os.write(self._stdout_fd, message.encode())

    def get_type_string(self, input):
        try:
            msg_type = type(data_dict).__name__ if type(data_dict) else ""
            self.force_print(f"{msg_type}\n")                    
        except Exception as e:
            pass




def main():
    netbench = NetBench()
    netbench.server_hostname = "127.0.0.1"
    netbench.port = 5201
    netbench.duration = 10
    netbench.test_reporter_interval = 0.1
    netbench.test_stats_interval = 0.1 
    netbench.json_output = True 
    netbench.json_stream_output = 1
    # netbench.omit = 9

    netbench.start_test()
    # print(result)








main()
