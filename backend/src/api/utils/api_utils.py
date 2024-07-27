from typing import Dict

from src.proto.generated import netbench_pb2


def convert_netbench_settings_to_grpc_settings(settings: Dict) -> netbench_pb2.TestSettings:
    #todo probably don't need all the tostrings, toints, etc
    return netbench_pb2.TestSettings(
        title=str(settings["Title"]),
        tags=list(settings["Tags"]),
        host=str(settings["Host"]),
        port=int(settings["Port"]),
        interval=float(settings["Interval"]),
        duration=int(settings["Test Length"]),
    )
