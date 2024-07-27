# from src.netbench.netbench import Netbench
from src.netbench.netbench import Netbench
from src.netbench.settings import Settings
import src.api.utils.api_utils as utils
from src.proto.generated import netbench_pb2
import time


class NetbenchService(Netbench):
    def __init__(self):
        self.settings = Settings().settings
        print (self.settings)
        super().__init__(self.settings)


    def run_test(self):
        self.start_test_threads()
        test_length = int(self.settings["Test Length"])
        refresh_interval = float(self.settings["Interval"])
        time_remaining = test_length
        while time_remaining > 0:
            current_time, bits_per_second = self.pop_plot_queue()
            self.force_print(f"Time: {current_time}, Bits Per Second: {bits_per_second}")
            if time is not None and bits_per_second is not None:
                yield netbench_pb2.TestPacket(time=current_time, bitsPerSecond=bits_per_second)
            time.sleep(refresh_interval)
            time_remaining -= refresh_interval

    def save_settings(self, data):
        pass

    def get_settings(self) -> netbench_pb2.TestSettings:
        return utils.convert_netbench_settings_to_grpc_settings(self.settings)
