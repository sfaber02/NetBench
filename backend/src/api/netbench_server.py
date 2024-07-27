from concurrent import futures
import grpc
from typing import Iterator
from src.proto.generated import netbench_pb2_grpc, netbench_pb2
from grpc_reflection.v1alpha import reflection
from netbench_service import NetbenchService
from src.netbench.settings import Settings



class NetbenchServicer(netbench_pb2_grpc.NetbenchServicer, NetbenchService):
    def __init__(self):
        settings = Settings().settings
        super().__init__(settings)

    def StartTest(self, request: netbench_pb2.EmptyRequest, context: grpc.ServicerContext) -> Iterator[netbench_pb2.TestPacket]:
        # Implementation of StartTest
        for i in range(10):
            yield netbench_pb2.TestPacket(time=i, bitsPerSecond=1000.0 * i)

    def SaveSettings(self, request: netbench_pb2.TestSettings, context: grpc.ServicerContext) -> netbench_pb2.SaveSettingsResponse:
        # Implementation of SaveSettings
        return netbench_pb2.SaveSettingsResponse(success=True)

    def GetSettings(self, request: netbench_pb2.EmptyRequest, context: grpc.ServicerContext) -> netbench_pb2.TestSettings:
        # Implementation of GetSettings
        return netbench_pb2.TestSettings(
            title="Network Benchmark",
            tags=["example", "test"],
            host="localhost",
            port=5201,
            interval=1.0,
            duration=10
        )

def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    netbench_pb2_grpc.add_NetbenchServicer_to_server(NetbenchServicer(), server)
    server.add_insecure_port('[::]:50051')

    # Enable reflection
    SERVICE_NAMES = (
        netbench_pb2.DESCRIPTOR.services_by_name['Netbench'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)


    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
