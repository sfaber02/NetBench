from iperf import Client


def main():
    iperf_client = Client()
    iperf_client.server_hostname = "192.168.50.98"
    iperf_client.port = 5201
    iperf_client.duration = 6
    print(iperf_client)
    
    result = iperf_client.run()
    print(result)

main()
