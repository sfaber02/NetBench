from netbench_new import NetBench
from settings import Settings
from datetime import datetime


settings = Settings()
settings.get_user_inputs()
settings = settings.saved_settings

# test settings
netbench = NetBench(settings)
netbench.server_hostname = settings["Host"]
netbench.port = settings["Port"]
netbench.duration = int(settings["Test Length"])
netbench.test_reporter_interval = float(settings["Interval"])
netbench.test_stats_interval = float(settings["Interval"])
netbench.json_output = True 
netbench.json_stream_output = 1


# bokeh settings
netbench.plot.width = int(settings["Width"])
netbench.plot.height = int(settings["Height"])
netbench.curdoc.theme = settings["Theme"]

current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# title_with_timestamp = f"{settings['Title']} - {current_timestamp}"
    self.plot =  figure( title="title",
        x_axis_label="WHAT",
        y_axis_label="Mbits / sec",
    )



netbench.start_test()


