from iperf import Client
import sys


class MyStream:
    def write(self, text):
        # This is where we can parse the output and do what we need with it.
        intercepted_text = f"Intercepted text: {text}"
        sys.__stdout__.write(intercepted_text)

    def flush(self):
        # Redirect to the original standard output
        return sys.__stdout__.flush()


sys.stdout = MyStream()


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
