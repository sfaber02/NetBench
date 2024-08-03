// package: netbench
// file: netbench.proto

/* tslint:disable */
/* eslint-disable */

import * as jspb from "google-protobuf";

export class TestPacket extends jspb.Message { 
    getTime(): number;
    setTime(value: number): TestPacket;
    getBitspersecond(): number;
    setBitspersecond(value: number): TestPacket;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): TestPacket.AsObject;
    static toObject(includeInstance: boolean, msg: TestPacket): TestPacket.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: TestPacket, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): TestPacket;
    static deserializeBinaryFromReader(message: TestPacket, reader: jspb.BinaryReader): TestPacket;
}

export namespace TestPacket {
    export type AsObject = {
        time: number,
        bitspersecond: number,
    }
}

export class TestSettings extends jspb.Message { 
    getTitle(): string;
    setTitle(value: string): TestSettings;
    clearTagsList(): void;
    getTagsList(): Array<string>;
    setTagsList(value: Array<string>): TestSettings;
    addTags(value: string, index?: number): string;
    getHost(): string;
    setHost(value: string): TestSettings;
    getPort(): number;
    setPort(value: number): TestSettings;
    getInterval(): number;
    setInterval(value: number): TestSettings;
    getDuration(): number;
    setDuration(value: number): TestSettings;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): TestSettings.AsObject;
    static toObject(includeInstance: boolean, msg: TestSettings): TestSettings.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: TestSettings, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): TestSettings;
    static deserializeBinaryFromReader(message: TestSettings, reader: jspb.BinaryReader): TestSettings;
}

export namespace TestSettings {
    export type AsObject = {
        title: string,
        tagsList: Array<string>,
        host: string,
        port: number,
        interval: number,
        duration: number,
    }
}

export class SaveSettingsResponse extends jspb.Message { 
    getSuccess(): boolean;
    setSuccess(value: boolean): SaveSettingsResponse;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): SaveSettingsResponse.AsObject;
    static toObject(includeInstance: boolean, msg: SaveSettingsResponse): SaveSettingsResponse.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: SaveSettingsResponse, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): SaveSettingsResponse;
    static deserializeBinaryFromReader(message: SaveSettingsResponse, reader: jspb.BinaryReader): SaveSettingsResponse;
}

export namespace SaveSettingsResponse {
    export type AsObject = {
        success: boolean,
    }
}

export class EmptyRequest extends jspb.Message { 

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): EmptyRequest.AsObject;
    static toObject(includeInstance: boolean, msg: EmptyRequest): EmptyRequest.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: EmptyRequest, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): EmptyRequest;
    static deserializeBinaryFromReader(message: EmptyRequest, reader: jspb.BinaryReader): EmptyRequest;
}

export namespace EmptyRequest {
    export type AsObject = {
    }
}
