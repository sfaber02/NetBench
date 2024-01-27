from iperf import Iperf_Client
# import iperf3
from dotenv import load_dotenv
import os
    
HOST = os.getenv('IPERF_SERVER_ADDRESS')
PORT = os.getenv('IPERF_PORT')

def main():
    load_dotenv()

    # client = iperf3.Client()
    iperf_client = Iperf_Client(HOST, PORT)
    print (iperf_client)
    print ("YAY")



main()