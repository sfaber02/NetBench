import subprocess
from dotenv import load_dotenv
import os
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
import re

HOST = os.getenv("IPERF_SERVER_ADDRESS")
PORT = os.getenv("IPERF_PORT")

# Create column data source for plot
source = ColumnDataSource(dict(x=[], y=[]))
# Create plot
p = figure(
    title="Wired Connection Test",
    x_axis_label="Time in Seconds",
    y_axis_label="Mbits / sec",
)
p.width=1200
p.height=720
p.line(x="x", y="y", source=source, line_color="white")

# store subprocess
process = None
first_point = True


def main():
    load_dotenv()
    print(f"Testing on host {HOST}, port {PORT}")

    curdoc().add_root(p)
    curdoc().add_periodic_callback(update, 0.5)
    curdoc().theme = "dark_minimal"


def update():
    global process
    global first_point
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
        if not first_point:
            line = process.stdout.readline().decode().strip()
        else:
            first_point = False
        # parse data here
        data_x, data_y = parse_line(line)
        source.stream(dict(x=[data_x], y=[data_y]))
    except ParseException as e:
        print(f"{e.message}, line = {e.line}")
    except UnboundLocalError as e:
        print (f"Unbound Local Error- line has no value")


def parse_line(line):
    # Regular expression to match time and speed
    match = re.search(
        r"\[\s*\d+\]\s*([\d.]+)-([\d.]+)\s*sec.*\s([\d.]+)\s*Mbits/sec", line
    )

    if match:
        # start_time = float(match.group(1))
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

main()


"""
DUMP

    iperf_client = Iperf_Client(HOST, PORT)
    iperf_client.set_duration(5)
    iperf_client.set_streams(1)
    iperf_client.set_interval(0.5)
    
    result = iperf_client.run_test()

    print (result)

    print ("YAY")
"""
