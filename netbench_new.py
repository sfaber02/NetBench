from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure

# from colorama import Fore
from iperf import Client
from settings import Settings
from threading import Thread
from multiprocessing import Pipe
import os
import json
from collections import deque
import time
from typing import (Union, Tuple, Dict)


class NetBench(Client):
    def __init__(self):
        # iperf python client base class
        super().__init__()
        self.settings = Settings().settings

        self.server_hostname = self.settings["Host"]
        self.port = self.settings["Port"]
        self.duration = int(self.settings["Test Length"])
        self.test_reporter_interval = float(self.settings["Interval"])
        self.test_stats_interval = float(self.settings["Interval"])
        self.json_output = True
        self.json_stream_output = 1

        # pipe for json stream test data from iperf
        self.input_data_pipe, self.output_data_pipe = Pipe()
        # thread to run test
        self.worker_thread: Thread
        # thread to read pipe
        self.pipe_thread: Thread
        # thread to plot graph
        self.graph_thread: Thread
        # store original stdout for later
        self._stdout_fd = os.dup(
            1)
        self._stderr_fd = os.dup(2)
        # redirect stdout
        os.dup2(self._pipe_in, 1, inheritable=True)
        # os.dup2(self._pipe_in, 2)  # stderr

        # column data for bokeh
        self.column_data = ColumnDataSource(
            dict(x=[], y=[]))
        self.plot_queue: deque = deque()
        self.plot = figure(
            title=self.settings["Title"],
            x_axis_label=self.settings["X Axis Label"],
            y_axis_label="Mbits / sec",
        )
        self.plot.width = int(self.settings["Width"])
        self.plot.height = int(self.settings["Height"])
        self.plot.line(x="x", y="y", source=self.column_data)
        self.curdoc = curdoc()
        self.curdoc.theme = self.settings["Theme"]
        self.curdoc.add_root(self.plot)

    def start_test(self) -> None:
        # start iperf test
        self.worker_thread = Thread(target=self.run)
        self.worker_thread.start()
        # start pipe worker
        self.pipe_thread = Thread(target=self.pipe_reader)
        self.pipe_thread.start()
        # self.graph_reader()
        self.graph_thread = Thread(target=self.start_graph)
        self.graph_thread.start()

        self.force_print("All Threads Started! Commencing Test")

    def pipe_reader(self) -> None:
        while self.worker_thread.is_alive():
            try:
                msg: Union[str, bytes] = b""
                msg = os.read(self._pipe_out, 1024)
                if msg:
                    msg = msg.decode("utf-8")
                    data_tuple: Tuple[float, float] = self.parse_pipe_data(msg)
                    if data_tuple:
                        self.plot_queue.append(data_tuple)
                    # self.force_print(msg)
                else:
                    self.force_print("EMPTY MSG")
            except Exception:
                self.force_print("ERROR")
                break
            # slow down worker loop 50ms
            time.sleep(0.05)
        self.force_print("LOOP DEAD")
        self.curdoc.remove_periodic_callback(self.graph_callback)
        os.close(self._pipe_in)
        os.close(self._pipe_out)

    def update_graph(self):
        try:
            x, y = self.plot_queue.popleft()
            self.column_data.stream(dict(x=[x], y=[y]))
        except IndexError:
            pass

    def start_graph(self):
        self.graph_callback = self.curdoc.add_periodic_callback(self.update_graph, 0.2)

    def parse_pipe_data(self, data):
        try:
            data_dict = json.loads(data)
        except Exception:
            data_dict = {}
            return None  # self.force_print("bad json")

        try:
            data = data_dict.get("data", {})
            packet_sums = data.get("sum", {})
            if packet_sums:
                bits_per_second = packet_sums.get("bits_per_second", 0.0)
                end_time = packet_sums.get("end", 0.0)

                return (end_time, bits_per_second)
        except (KeyError, IndexError):
            return None

    def force_print(self, message):
        message = message + "\n"
        os.write(self._stdout_fd, message.encode())
