from netbench_new import NetBench
from settings import Settings
from datetime import datetime


settings = Settings()
settings.get_user_inputs()
settings = settings.saved_settings


netbench = NetBench()
netbench.server_hostname = settings["Host"]
netbench.port = settings["Port"]
netbench.duration = int(settings["Test Length"])
netbench.test_reporter_interval = float(settings["Interval"])
netbench.test_stats_interval = float(settings["Interval"])
netbench.json_output = True 
netbench.json_stream_output = 1



netbench.plot.width = int(settings["Width"])
netbench.plot.height = int(settings["Height"])
netbench.curdoc.theme = settings["Theme"]

current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
title_with_timestamp = f"{settings['Title']} - {current_timestamp}"



netbench.start_test()


