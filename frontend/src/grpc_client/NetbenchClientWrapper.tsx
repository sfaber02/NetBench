import * as grpc from '@grpc/grpc-js';
import { NetbenchClient } from './proto/generated/netbench_grpc_pb';
import { EmptyRequest, TestSettings, SaveSettingsResponse } from './proto/generated/netbench_pb';
import {genericTestSettings} from "./BaseTestSettings";


class NetbenchClientWrapper {
    private client: NetbenchClient;
    private serverAddress: string = 'localhost:50051';

    constructor() {
        this.client = new NetbenchClient(this.serverAddress, grpc.credentials.createInsecure());
    }

    public startTest(callback: (error: grpc.ServiceError | null, response: TestSettings) => void): void {
        const call = this.client.startTest(new EmptyRequest());

        call.on('data', (data: TestSettings) => {
            console.log('TestPacket:', data.toObject());
            if (callback) callback(null, data);
        });

        call.on('end', () => {
            console.log('Stream ended.');
        });

        call.on('error', (error: grpc.ServiceError) => {
            console.error('Stream error:', error);
            if (callback) callback(error, genericTestSettings);
        });

        call.on('status', (status: grpc.StatusObject) => {
            console.log('Stream status:', status);
        });
    }

    public saveSettings(settings: TestSettings, callback: (error: grpc.ServiceError | null, response: SaveSettingsResponse) => void): void {
        this.client.saveSettings(settings, (error, response) => {
            if (error) {
                console.error('Error:', error);
            } else {
                console.log('SaveSettingsResponse:', response.toObject());
            }
            if (callback) callback(error, response);
        });
    }

    public getSettings(callback: (error: grpc.ServiceError | null, response: TestSettings) => void): void {
        this.client.getSettings(new EmptyRequest(), (error, response) => {
            if (error) {
                console.error('Error:', error);
            } else {
                console.log('TestSettings:', response.toObject());
            }
            if (callback) callback(error, response);
        });
    }
}

export { NetbenchClientWrapper };
