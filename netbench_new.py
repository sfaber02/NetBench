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


class NetBench(Client):
    def __init__(self):
        # iperf python client base class
        super().__init__()
        # pipe for json stream test data from iperf
        self.input_data_pipe, self.output_data_pipe = Pipe()
        # thrad to run test
        self.worker_thread: Thread
        # store original stdout for later
        self._stdout_fd = os.dup(1)
        self._stderr_fd = os.dup(2)
        # redirect stdout
        os.dup2(self._pipe_in, 1 , inheritable=True)
        # os.dup2(self._pipe_in, 2)  # stderr 



        # column data for bokeh
        self.column_data = ColumnDataSource(dict(x=[], y=[]))
        self.x_stream = []
        self.y_stream = []
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
        self.worker_thread = Thread(
            target=self.run)
        self.worker_thread.start()
        self.pipe_reader()
        self.curdoc.add_periodic_callback(self.update_graph, 0.5)


    def pipe_reader(self):
        while self.worker_thread.is_alive():
            try:
                msg = b""
                msg = os.read(self._pipe_out, 1024) 
                if msg:
                    msg = msg.decode('utf-8')
                    data_x, data_y = self.parse_pipe_data(msg)
                    # self.x_stream.append(data_x) 
                    # self.y_stream.append(data_y)

                    # self.columnx_data["x"] = data_x
                    # self.column_data["y"] = data_y
                else:
                    self.force_print("EMPTY MSG")
            except:
                self.force_print("ERROR")
                break
        self.force_print("LOOP DEAD")
        os.close(self._pipe_in)
        os.close(self._pipe_out)

    def update_graph(self):
        x = [self.x_stream[-1]] if len(self.x_stream) > 0 else []
        y = [self.y_stream[-1]] if len(self.y_stream) > 0 else []
        self.column_data.stream(dict(x=x, y=y))
        
        # if self.worker_thread.is_alive():
            # try:
                # msg = b""
                # msg = os.read(self._pipe_out, 1024) 
                # if msg:
                    # msg = msg.decode('utf-8')
                    # parsed_data = self.parse_pipe_data(msg)
                    # data_x, data_y =  source.stream(dict(x=[data_x], y=[data_y]))
                # else:
                    # self.force_print("EMPTY MSG")
            # except:
                # self.force_print("ERROR")



    def parse_pipe_data(self, data):
        try:
            data_dict = json.loads(data)
        except:
            data_dict = {}
            return 0, 0
            # self.force_print("bad json")

        try:
            data = data_dict.get("data", {})
            packet_sums = data.get("sum", {})
            # packet_info = streams[0] if len(streams) > 0 else {}
            if packet_sums:
                bits_per_second = packet_sums.get("bits_per_second", 0.0)
                end_time = packet_sums.get("end", 0.0)
                print_string = str(end_time)
                self.force_print(print_string)
                return end_time, bits_per_second
        except Exception as e:
            self.force_print(f"BAD THING {e}")
            return 0, 0


    def force_print(self, message):
        message = message + "\n"
        os.write(self._stdout_fd, message.encode())

    def get_type_string(self, input):
        try:
            msg_type = type(data_dict).__name__ if type(data_dict) else ""
            self.force_print(f"{msg_type}\n")                    
        except Exception as e:
            # print(f"Buttes {e}")
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

    netbench.start_test()
    # print(result)








main()
