from iperf import Iperf_Client
from plotting import plot
import iperf3
import subprocess
from dotenv import load_dotenv
import os
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure

HOST = os.getenv("IPERF_SERVER_ADDRESS")
PORT = os.getenv("IPERF_PORT")

# Create column data source for plot
source = ColumnDataSource(dict(x=[], y=[]))
#Create plot
p = figure(title="Network Speed vs. Time", x_axis_label="Time in Seconds", y_axis_label="Mbits / sec")
p.line(x="x", y="y", source=source)

#store subprocess
process = None
count = 0

def main():
    load_dotenv()
    print(f"Testing on host {HOST}, port {PORT}")

    curdoc().add_root(p)
    curdoc().add_periodic_callback(update, 100)


def update():
    global process
    global count
    try: 
        if process is None:
            command = [
                "iperf3",
                "-c",
                HOST,
                "-p",
                PORT,
                "-i",
                "0.5",
                "-t",
                "10",
                "--forceflush"
            ]
            process = subprocess.Popen(command, stdout=subprocess.PIPE)
        line = process.stdout.readline().decode().strip()
        #parse data here
        print(line)
        print (f"count = {count}")
        data_x = count
        data_y = count
        count += 1
        source.stream(dict(x=[data_x], y=[data_y]))
    except Exception as e:
        print (f"Exception {e}")



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
