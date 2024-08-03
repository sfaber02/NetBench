// package: netbench
// file: netbench.proto

/* tslint:disable */
/* eslint-disable */

import * as grpc from "@grpc/grpc-js";
import * as netbench_pb from "./netbench_pb";

interface INetbenchService extends grpc.ServiceDefinition<grpc.UntypedServiceImplementation> {
    startTest: INetbenchService_IStartTest;
    saveSettings: INetbenchService_ISaveSettings;
    getSettings: INetbenchService_IGetSettings;
}

interface INetbenchService_IStartTest extends grpc.MethodDefinition<netbench_pb.EmptyRequest, netbench_pb.TestPacket> {
    path: "/netbench.Netbench/StartTest";
    requestStream: false;
    responseStream: true;
    requestSerialize: grpc.serialize<netbench_pb.EmptyRequest>;
    requestDeserialize: grpc.deserialize<netbench_pb.EmptyRequest>;
    responseSerialize: grpc.serialize<netbench_pb.TestPacket>;
    responseDeserialize: grpc.deserialize<netbench_pb.TestPacket>;
}
interface INetbenchService_ISaveSettings extends grpc.MethodDefinition<netbench_pb.TestSettings, netbench_pb.SaveSettingsResponse> {
    path: "/netbench.Netbench/SaveSettings";
    requestStream: false;
    responseStream: false;
    requestSerialize: grpc.serialize<netbench_pb.TestSettings>;
    requestDeserialize: grpc.deserialize<netbench_pb.TestSettings>;
    responseSerialize: grpc.serialize<netbench_pb.SaveSettingsResponse>;
    responseDeserialize: grpc.deserialize<netbench_pb.SaveSettingsResponse>;
}
interface INetbenchService_IGetSettings extends grpc.MethodDefinition<netbench_pb.EmptyRequest, netbench_pb.TestSettings> {
    path: "/netbench.Netbench/GetSettings";
    requestStream: false;
    responseStream: false;
    requestSerialize: grpc.serialize<netbench_pb.EmptyRequest>;
    requestDeserialize: grpc.deserialize<netbench_pb.EmptyRequest>;
    responseSerialize: grpc.serialize<netbench_pb.TestSettings>;
    responseDeserialize: grpc.deserialize<netbench_pb.TestSettings>;
}

export const NetbenchService: INetbenchService;

export interface INetbenchServer extends grpc.UntypedServiceImplementation {
    startTest: grpc.handleServerStreamingCall<netbench_pb.EmptyRequest, netbench_pb.TestPacket>;
    saveSettings: grpc.handleUnaryCall<netbench_pb.TestSettings, netbench_pb.SaveSettingsResponse>;
    getSettings: grpc.handleUnaryCall<netbench_pb.EmptyRequest, netbench_pb.TestSettings>;
}

export interface INetbenchClient {
    startTest(request: netbench_pb.EmptyRequest, options?: Partial<grpc.CallOptions>): grpc.ClientReadableStream<netbench_pb.TestPacket>;
    startTest(request: netbench_pb.EmptyRequest, metadata?: grpc.Metadata, options?: Partial<grpc.CallOptions>): grpc.ClientReadableStream<netbench_pb.TestPacket>;
    saveSettings(request: netbench_pb.TestSettings, callback: (error: grpc.ServiceError | null, response: netbench_pb.SaveSettingsResponse) => void): grpc.ClientUnaryCall;
    saveSettings(request: netbench_pb.TestSettings, metadata: grpc.Metadata, callback: (error: grpc.ServiceError | null, response: netbench_pb.SaveSettingsResponse) => void): grpc.ClientUnaryCall;
    saveSettings(request: netbench_pb.TestSettings, metadata: grpc.Metadata, options: Partial<grpc.CallOptions>, callback: (error: grpc.ServiceError | null, response: netbench_pb.SaveSettingsResponse) => void): grpc.ClientUnaryCall;
    getSettings(request: netbench_pb.EmptyRequest, callback: (error: grpc.ServiceError | null, response: netbench_pb.TestSettings) => void): grpc.ClientUnaryCall;
    getSettings(request: netbench_pb.EmptyRequest, metadata: grpc.Metadata, callback: (error: grpc.ServiceError | null, response: netbench_pb.TestSettings) => void): grpc.ClientUnaryCall;
    getSettings(request: netbench_pb.EmptyRequest, metadata: grpc.Metadata, options: Partial<grpc.CallOptions>, callback: (error: grpc.ServiceError | null, response: netbench_pb.TestSettings) => void): grpc.ClientUnaryCall;
}

export class NetbenchClient extends grpc.Client implements INetbenchClient {
    constructor(address: string, credentials: grpc.ChannelCredentials, options?: Partial<grpc.ClientOptions>);
    public startTest(request: netbench_pb.EmptyRequest, options?: Partial<grpc.CallOptions>): grpc.ClientReadableStream<netbench_pb.TestPacket>;
    public startTest(request: netbench_pb.EmptyRequest, metadata?: grpc.Metadata, options?: Partial<grpc.CallOptions>): grpc.ClientReadableStream<netbench_pb.TestPacket>;
    public saveSettings(request: netbench_pb.TestSettings, callback: (error: grpc.ServiceError | null, response: netbench_pb.SaveSettingsResponse) => void): grpc.ClientUnaryCall;
    public saveSettings(request: netbench_pb.TestSettings, metadata: grpc.Metadata, callback: (error: grpc.ServiceError | null, response: netbench_pb.SaveSettingsResponse) => void): grpc.ClientUnaryCall;
    public saveSettings(request: netbench_pb.TestSettings, metadata: grpc.Metadata, options: Partial<grpc.CallOptions>, callback: (error: grpc.ServiceError | null, response: netbench_pb.SaveSettingsResponse) => void): grpc.ClientUnaryCall;
    public getSettings(request: netbench_pb.EmptyRequest, callback: (error: grpc.ServiceError | null, response: netbench_pb.TestSettings) => void): grpc.ClientUnaryCall;
    public getSettings(request: netbench_pb.EmptyRequest, metadata: grpc.Metadata, callback: (error: grpc.ServiceError | null, response: netbench_pb.TestSettings) => void): grpc.ClientUnaryCall;
    public getSettings(request: netbench_pb.EmptyRequest, metadata: grpc.Metadata, options: Partial<grpc.CallOptions>, callback: (error: grpc.ServiceError | null, response: netbench_pb.TestSettings) => void): grpc.ClientUnaryCall;
}
