import subprocess
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
import re
from settings import get_user_inputs, get_settings_from_disk
from datetime import datetime
import logging

# store subprocess
process = None
# Create column data source for plot
source = ColumnDataSource(dict(x=[], y=[]))
# store settings
settings = get_settings_from_disk()

# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
    
logger=logging.getLogger()
logger.setLevel(logging.CRITICAL)



def start():
    global settings

    change_user_inputs = input("Change Test Settings? (Y or N)")
    if change_user_inputs == "y" or change_user_inputs == "Y":
        settings = get_user_inputs()

    print(f"\033[32mTesting on host {settings['Host']}, port {settings['Port']}")

    #get current timestamp
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #combine timestamp with title
    title_with_timestamp = f"{settings['Title']} - {current_timestamp}"

    # Create plot
    plot = figure(
        title=title_with_timestamp,
        x_axis_label=settings["X Axis Label"],
        y_axis_label="Mbits / sec",
    )
    plot.width = int(settings["Width"])
    plot.height = int(settings["Height"])
    plot.line(x="x", y="y", source=source, line_color=settings["Line Color"])

    curdoc().theme = settings["Theme"]
    curdoc().add_root(plot)
    curdoc().add_periodic_callback(update, 0.5)


def update():
    global settings
    global process
    global source
    try:
        if process is None:
            command = [
                "iperf3",
                "-c",
                settings["Host"],
                "-p",
                settings["Port"],
                "-i",
                settings["Interval"],
                "-t",
                settings["Test Length"],
                "-f",
                "m",
                "--forceflush",
            ]
            process = subprocess.Popen(command, stdout=subprocess.PIPE)
        line = process.stdout.readline().decode().strip()
        # parse data here
        data_x, data_y = parse_line(line)
        source.stream(dict(x=[data_x], y=[data_y]))
    except ParseException as e:
        logger.debug(f"{e.message}, line={e.line}")
    except UnboundLocalError as e:
        logger.error(f"{e.message}, line={e.line}")
    except UnboundLocalError:
        logger.error(f"{e.message}, line={e.line}")
    except UnboundLocalError:
        logger.error("Unbound Local Error - line has no value")


def parse_line(line):
    # Regular expression to match time and speed
    # maybe new regex r"\[\s*\d+\]\s*([\d.]+)-([\d.]+)\s*sec.*\s*([\d.]+)\s*M?bits/sec"
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
