from concurrent import futures
import grpc
import sys
from grpc_reflection.v1alpha import reflection

import sys
import time
from pathlib import Path

from src.proto.generated import test_pb2_grpc, test_pb2


# from src.proto.generated import test_pb2_grpc, test_pb2

class GreeterServicer(test_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return test_pb2.HelloReply(message='Hello, %s!' % request.name)

    def SayHelloStream(self, request, context):
        for i in range(10):
            print (f"Sending message {request}")
            yield test_pb2.HelloReply(message='Hello, %s! %d' % (request.name, i))
            time.sleep(1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')

    # Enable reflection
    SERVICE_NAMES = (
        test_pb2.DESCRIPTOR.services_by_name['Greeter'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
