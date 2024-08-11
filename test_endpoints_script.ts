import { startTest, saveSettings, getSettings } from './frontend/src/grpc_client/test_client';

// Test the StartTest endpoint
console.log('Testing StartTest endpoint...');
startTest();

// Test the SaveSettings endpoint
console.log('Testing SaveSettings endpoint...');
saveSettings({ title: 'Test', tags: ['example'], host: 'localhost', port: 8080, interval: 1.0, duration: 60 }, (err, res) => {
  if (!err) {
    console.log('SaveSettings response:', res);

    // Test the GetSettings endpoint
    console.log('Testing GetSettings endpoint...');
    getSettings((error, response) => {
      if (!error) {
        console.log('GetSettings response:', response);
      }
    });
  }
});
