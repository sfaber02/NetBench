// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var netbench_pb = require('./netbench_pb.js');

function serialize_netbench_EmptyRequest(arg) {
  if (!(arg instanceof netbench_pb.EmptyRequest)) {
    throw new Error('Expected argument of type netbench.EmptyRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_netbench_EmptyRequest(buffer_arg) {
  return netbench_pb.EmptyRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_netbench_SaveSettingsResponse(arg) {
  if (!(arg instanceof netbench_pb.SaveSettingsResponse)) {
    throw new Error('Expected argument of type netbench.SaveSettingsResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_netbench_SaveSettingsResponse(buffer_arg) {
  return netbench_pb.SaveSettingsResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_netbench_TestPacket(arg) {
  if (!(arg instanceof netbench_pb.TestPacket)) {
    throw new Error('Expected argument of type netbench.TestPacket');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_netbench_TestPacket(buffer_arg) {
  return netbench_pb.TestPacket.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_netbench_TestSettings(arg) {
  if (!(arg instanceof netbench_pb.TestSettings)) {
    throw new Error('Expected argument of type netbench.TestSettings');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_netbench_TestSettings(buffer_arg) {
  return netbench_pb.TestSettings.deserializeBinary(new Uint8Array(buffer_arg));
}


var NetbenchService = exports.NetbenchService = {
  startTest: {
    path: '/netbench.Netbench/StartTest',
    requestStream: false,
    responseStream: true,
    requestType: netbench_pb.EmptyRequest,
    responseType: netbench_pb.TestPacket,
    requestSerialize: serialize_netbench_EmptyRequest,
    requestDeserialize: deserialize_netbench_EmptyRequest,
    responseSerialize: serialize_netbench_TestPacket,
    responseDeserialize: deserialize_netbench_TestPacket,
  },
  saveSettings: {
    path: '/netbench.Netbench/SaveSettings',
    requestStream: false,
    responseStream: false,
    requestType: netbench_pb.TestSettings,
    responseType: netbench_pb.SaveSettingsResponse,
    requestSerialize: serialize_netbench_TestSettings,
    requestDeserialize: deserialize_netbench_TestSettings,
    responseSerialize: serialize_netbench_SaveSettingsResponse,
    responseDeserialize: deserialize_netbench_SaveSettingsResponse,
  },
  getSettings: {
    path: '/netbench.Netbench/GetSettings',
    requestStream: false,
    responseStream: false,
    requestType: netbench_pb.EmptyRequest,
    responseType: netbench_pb.TestSettings,
    requestSerialize: serialize_netbench_EmptyRequest,
    requestDeserialize: deserialize_netbench_EmptyRequest,
    responseSerialize: serialize_netbench_TestSettings,
    responseDeserialize: deserialize_netbench_TestSettings,
  },
};

exports.NetbenchClient = grpc.makeGenericClientConstructor(NetbenchService);
