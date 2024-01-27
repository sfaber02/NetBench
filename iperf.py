import iperf3




class Iperf_Client(iperf3.Client):
    def __init__(self, hostname, port):
        super().__init__()
        self.server_hostname = hostname
        self.port = port


    def set_duration(self, duration):
        self.duration = duration

    def set_interval(self, interval):
        self.fq_rate = interval

    def set_streams(self, streams):
        self.num_steams = streams
    

    def run_test(self):
        return super().run()
