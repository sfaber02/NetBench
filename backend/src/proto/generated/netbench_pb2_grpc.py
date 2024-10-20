# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from src.proto.generated import netbench_pb2 as netbench__pb2

GRPC_GENERATED_VERSION = '1.65.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in netbench_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class NetbenchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartTest = channel.unary_stream(
                '/netbench.Netbench/StartTest',
                request_serializer=netbench__pb2.EmptyRequest.SerializeToString,
                response_deserializer=netbench__pb2.TestPacket.FromString,
                _registered_method=True)
        self.SaveSettings = channel.unary_unary(
                '/netbench.Netbench/SaveSettings',
                request_serializer=netbench__pb2.TestSettings.SerializeToString,
                response_deserializer=netbench__pb2.SaveSettingsResponse.FromString,
                _registered_method=True)
        self.GetSettings = channel.unary_unary(
                '/netbench.Netbench/GetSettings',
                request_serializer=netbench__pb2.EmptyRequest.SerializeToString,
                response_deserializer=netbench__pb2.TestSettings.FromString,
                _registered_method=True)


class NetbenchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartTest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NetbenchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartTest': grpc.unary_stream_rpc_method_handler(
                    servicer.StartTest,
                    request_deserializer=netbench__pb2.EmptyRequest.FromString,
                    response_serializer=netbench__pb2.TestPacket.SerializeToString,
            ),
            'SaveSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveSettings,
                    request_deserializer=netbench__pb2.TestSettings.FromString,
                    response_serializer=netbench__pb2.SaveSettingsResponse.SerializeToString,
            ),
            'GetSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSettings,
                    request_deserializer=netbench__pb2.EmptyRequest.FromString,
                    response_serializer=netbench__pb2.TestSettings.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'netbench.Netbench', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('netbench.Netbench', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Netbench(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartTest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/netbench.Netbench/StartTest',
            netbench__pb2.EmptyRequest.SerializeToString,
            netbench__pb2.TestPacket.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SaveSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/netbench.Netbench/SaveSettings',
            netbench__pb2.TestSettings.SerializeToString,
            netbench__pb2.SaveSettingsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/netbench.Netbench/GetSettings',
            netbench__pb2.EmptyRequest.SerializeToString,
            netbench__pb2.TestSettings.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
