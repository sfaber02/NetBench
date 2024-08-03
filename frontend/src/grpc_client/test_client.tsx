// import * as grpc from '@grpc/grpc-js';
// import * as protoLoader from '@grpc/proto-loader';
// import * as path from 'path';
//
// // Load the protobuf
// const PROTO_PATH = path.join(__dirname, 'backend/src/proto/netbench.proto');
// const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
//   keepCase: true,
//   longs: String,
//   enums: String,
//   defaults: true,
//   oneofs: true
// });
// const netbenchProto = grpc.loadPackageDefinition(packageDefinition).netbench as any;
//
// // Create a client
// const client = new netbenchProto.Netbench('localhost:50051', grpc.credentials.createInsecure());
//
// // Function to call StartTest
// function startTest(): void {
//   const call = client.startTest({}, (error: grpc.ServiceError, response: any) => {
//     if (error) {
//       console.error('Error:', error);
//     } else {
//       console.log('Response:', response);
//     }
//   });
//
//   call.on('data', (data: any) => {
//     console.log('TestPacket:', data);
//   });
//
//   call.on('end', () => {
//     console.log('Stream ended.');
//   });
//
//   call.on('error', (error: grpc.ServiceError) => {
//     console.error('Stream error:', error);
//   });
//
//   call.on('status', (status: grpc.StatusObject) => {
//     console.log('Stream status:', status);
//   });
// }
//
// // Function to call SaveSettings
// function saveSettings(settings: any, callback: (error: grpc.ServiceError | null, response: any) => void): void {
//   client.saveSettings(settings, (error: grpc.ServiceError, response: any) => {
//     if (error) {
//       console.error('Error:', error);
//     } else {
//       console.log('SaveSettingsResponse:', response);
//     }
//     if (callback) callback(error, response);
//   });
// }
//
// // Function to call GetSettings
// function getSettings(callback: (error: grpc.ServiceError | null, response: any) => void): void {
//   client.getSettings({}, (error: grpc.ServiceError, response: any) => {
//     if (error) {
//       console.error('Error:', error);
//     } else {
//       console.log('TestSettings:', response);
//     }
//     if (callback) callback(error, response);
//   });
// }
//
// Example usage
// startTest();
// saveSettings({ title: 'Test', tags: ['example'], host: 'localhost', port: 8080, interval: 1.0, duration: 60 }, (err, res) => {
//   if (!err) {
//     getSettings((error, response) => {
//       if (!error) {
//         console.log('Settings:', response);
//       }
//     });
//   }
// });
//
//
// // Export the functions
// export { startTest, saveSettings, getSettings };

export {}
