from iperf import Iperf_Client
import iperf3
import subprocess
from dotenv import load_dotenv
import os

HOST = os.getenv("IPERF_SERVER_ADDRESS")
PORT = os.getenv("IPERF_PORT")


def main():
    load_dotenv()
    print(f"Testing on host {HOST}, port {PORT}")

    command = [
        "gstdbuf",
        "-o0",
        "iperf3",
        "-c",
        HOST,
        "-p",
        PORT,
        "-i",
        "0.5",
        "-t",
        "10",
    ]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)

    for line in process.stdout:
        print(line.strip())


main()


"""
DUMP

    iperf_client = Iperf_Client(HOST, PORT)
    iperf_client.set_duration(5)
    iperf_client.set_streams(1)
    iperf_client.set_interval(0.5)
    
    result = iperf_client.run_test()

    print (result)

    print ("YAY")
"""
