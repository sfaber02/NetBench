# from src.netbench.netbench import Netbench
from src.netbench.netbench import Netbench


class NetbenchService(Netbench):
    def __init__(self, settings):
        super().__init__(settings)


    def start_test(self):
        return self.netbench.get()

    def save_settings(self, data):
        return self.netbench.post(data)

    def get_settings(self, data):
        return self.netbench.delete(data)
