from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from tornado.ioloop import IOLoop

# from colorama import Fore
from .iperf import Client
from .settings import Settings
import threading
from threading import Thread
from multiprocessing import Pipe
import os
import json
from collections import deque
import time
from typing import Union, Tuple, Dict


class Netbench(Client):
    def __init__(self, settings, web=False):
        # iperf python client base class
        super().__init__()

        #flag for web / terminal mode
        self.web = web

        self.server_hostname = settings["Host"]
        self.port = settings["Port"]
        self.duration = int(settings["Test Length"])
        self.test_reporter_interval = float(settings["Interval"])
        self.test_stats_interval = float(settings["Interval"])
        self.json_output = True
        self.json_stream_output = 1

        # pipe for json stream test data from iperf
        self.input_data_pipe, self.output_data_pipe = Pipe()
        # thread to run test
        self.worker_thread: Thread
        # thread to read pipe
        self.pipe_thread: Thread
        # thread for bokeh server
        self.bokeh_thread: Thread
        # store original stdout for later
        self._stdout_fd = os.dup(1)
        self._stderr_fd = os.dup(2)
        # redirect stdout
        os.dup2(self._pipe_in, 1, inheritable=True)
        # os.dup2(self._pipe_in, 2)  # stderr

        # column data for bokeh
        #todo move to separate class or method
        self.column_data = ColumnDataSource(dict(x=[], y=[]))
        self.plot_queue: deque = deque()
        self.plot = figure(
            title=settings["Title"],
            x_axis_label=settings["X Axis Label"],
            y_axis_label="Mbits / sec",
        )
        self.plot.width = int(settings["Width"])
        self.plot.height = int(settings["Height"])
        self.theme = settings["Theme"]
        self.plot.line(
            x="x",
            y="y",
            source=self.column_data,
            line_color=settings["Line Color"],
        )
        self.bokeh_server: Server

    def start_test_threads(self) -> None:
        # start iperf test
        self.worker_thread = Thread(target=self.run)
        self.worker_thread.start()
        # start pipe worker
        self.pipe_thread = Thread(target=self.pipe_reader)
        self.pipe_thread.start()

        # don't start bokeh server if web flag is set
        if not self.web:
            # Initialize Bokeh server and start it in a new Thread.
            self.start_bokeh_server
            self.bokeh_server = Server(
                {"/netbench": Application(FunctionHandler(self.modify_doc))},
                io_loop=IOLoop(),
                address="localhost",
                port=8000,
                allow_websocket_origin=["localhost:8000"],
            )
            self.bokeh_thread = Thread(target=self.start_bokeh_server)
            self.bokeh_thread.daemon = True
            self.bokeh_thread.start()


        self.force_print("************")
        self.force_print("************")
        self.force_print("All Threads Started! Commencing Test")
        if not self.web:
            self.force_print("Navigate to localhost:8000/netbench in browser to see graph")
        self.force_print("************")
        self.force_print("************")

    def start_bokeh_server(self):
        self.bokeh_server.start()
        try:
            self.bokeh_server.io_loop.start()
        except RuntimeError:
            pass

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
        self.bokeh_server.io_loop.stop()
        self.bokeh_server.stop()
        os.close(self._pipe_in)
        os.close(self._pipe_out)
        self.force_print("Test Complete!")

    def update_graph(self):
        try:
            x, y = self.plot_queue.popleft()
            self.column_data.stream(dict(x=[x], y=[y]))
        except IndexError:
            if not self.worker_thread.is_alive():
                if self.graph_callback:
                    curdoc().remove_periodic_callback(self.graph_callback)

    def pop_plot_queue(self) -> Tuple[float, float]:
        try:
            seconds, bits_per_second = self.plot_queue.popleft()
            return float(seconds), float(bits_per_second)
        except IndexError:
            #todo remove this for testing
            return 0.0, 0.0


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

                return end_time, bits_per_second / 1000000
        except (KeyError, IndexError):
            return None

    def modify_doc(self, doc):
        doc.add_root(self.plot)
        doc.theme = self.theme
        self.graph_callback = doc.add_periodic_callback(self.update_graph, 0.2)

    def force_print(self, message):
        message = message + "\n"
        os.write(self._stdout_fd, message.encode())


