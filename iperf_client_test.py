from iperf import Client


def main():
    iperf_client = Client()
    iperf_client.server_hostname = "192.168.50.98"
    iperf_client.port = 5201
    iperf_client.duration = 6
    iperf_client.test_reporter_interval = 0.1
    
    iperf_client.test_stats_interval = 0.1 
    # print(iperf_client)
    iperf_client.json_output = True 
    iperf_client.json_stream_output = 1
    
    result = iperf_client.run()
    print(result)

main()
