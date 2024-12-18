from concurrent import futures
import grpc
from typing import Iterator
from src.proto.generated import netbench_pb2_grpc, netbench_pb2
from grpc_reflection.v1alpha import reflection
from netbench_service import NetbenchService
from src.netbench.settings import Settings
import time


class NetbenchServer(NetbenchService, netbench_pb2_grpc.NetbenchServicer):
    def __init__(self):
        super().__init__()


    def StartTest(self, request: netbench_pb2.EmptyRequest, context: grpc.ServicerContext) -> Iterator[netbench_pb2.TestPacket]:
        return NetbenchService.run_test(self)


    def SaveSettings(self, request: netbench_pb2.TestSettings, context: grpc.ServicerContext) -> netbench_pb2.SaveSettingsResponse:
        # mock  Implementation of SaveSettings
        return netbench_pb2.SaveSettingsResponse(success=True)

    def GetSettings(self, request: netbench_pb2.EmptyRequest, context: grpc.ServicerContext) -> netbench_pb2.TestSettings:
        return NetbenchService.get_settings(self)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    netbench_pb2_grpc.add_NetbenchServicer_to_server(NetbenchServer(), server)
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
