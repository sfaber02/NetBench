import iperf3




class Iperf_Client(iperf3.Client):
    def __init__(self, hostname, port):
        super().__init__()
        self.hostname = hostname
        self.port = port
        
    # def set_duration(self, duration):
    #     self.duration = duration
    
    # def run(self):
    #     self.run()
