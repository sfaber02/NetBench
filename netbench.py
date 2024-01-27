import subprocess
import os
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
import re
from colorama import Fore

HOST = os.getenv("IPERF_SERVER_ADDRESS")
PORT = os.getenv("IPERF_PORT")

# store subprocess
process = None
# Create column data source for plot
source = ColumnDataSource(dict(x=[], y=[]))


def start():
    print(f"\033[32mTesting on host {HOST}, port {PORT}")

    

    # Create plot
    plot = figure(
        title="Wired Connection Test",
        x_axis_label="Time in Seconds",
        y_axis_label="Mbits / sec",
    )
    plot.width = 1200
    plot.height = 720
    plot.line(x="x", y="y", source=source, line_color="white")

    curdoc().theme = "dark_minimal"
    curdoc().add_root(plot)
    curdoc().add_periodic_callback(update, 0.5)


def update():
    global process
    global source

    try:
        if process is None:
            command = [
                "iperf3",
                "-c",
                HOST,
                "-p",
                PORT,
                "-i",
                "0.1",
                "-t",
                "1000",
                "--forceflush",
            ]
            process = subprocess.Popen(command, stdout=subprocess.PIPE)
        line = process.stdout.readline().decode().strip()
        # parse data here
        data_x, data_y = parse_line(line)
        source.stream(dict(x=[data_x], y=[data_y]))
    except ParseException as e:
        print(f"\033[31m{e.message}, line = {e.line}")
        print(Fore.GREEN)
    except UnboundLocalError as e:
        print(f"\033[31mUnbound Local Error- line has no value")
        print(Fore.GREEN)


def parse_line(line):
    # Regular expression to match time and speed
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
