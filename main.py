from iperf import Iperf_Client
from dotenv import load_dotenv
import os
    
HOST = os.getenv('IPERF_SERVER_ADDRESS')
PORT = int(os.getenv('IPERF_PORT'))

def main():
    load_dotenv()

    print (f"Testing on host {HOST}, port {PORT}")

    iperf_client = Iperf_Client(HOST, PORT)
    iperf_client.set_duration(5)
    iperf_client.set_streams(1)
    iperf_client.set_interval(0.5)
    
    result = iperf_client.run_test()

    print (result)

    print ("YAY")



main()