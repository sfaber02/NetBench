# from src.netbench.netbench import Netbench
from src.netbench.netbench import Netbench
from src.netbench.settings import Settings
import src.api.utils.api_utils as utils
from src.proto.generated import netbench_pb2


class NetbenchService(Netbench):
    def __init__(self):
        self.settings = Settings().settings
        print (self.settings)
        super().__init__(self.settings)


    def start_test(self):
        return self.netbench.get()

    def save_settings(self, data):
        return self.netbench.post(data)

    def get_settings(self) -> netbench_pb2.TestSettings:
        return utils.convert_netbench_settings_to_grpc_settings(self.settings)
