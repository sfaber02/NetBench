from concurrent import futures
import grpc
import sys
from grpc_reflection.v1alpha import reflection

import sys
from pathlib import Path

from src.proto.generated import test_pb2_grpc, test_pb2

#
# # Calculate the absolute path to the 'proto/generated' directory
# proto_generated_path = str(Path(__file__).resolve().parents[2] / 'proto' / 'generated')
#
# # Add this path to sys.path
# if proto_generated_path not in sys.path:
#     sys.path.append(proto_generated_path)

print (f"******* {sys.path}")

# Now you can import your pb2 files directly




class GreeterServicer(test_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return test_pb2.HelloReply(message='Hello, %s!' % request.name)

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
