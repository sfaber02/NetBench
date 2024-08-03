import { TestSettings } from './proto/generated/netbench_pb';

const genericTestSettings: TestSettings = new TestSettings();
genericTestSettings.setTitle('DefaultTest');
genericTestSettings.setTagsList(['default', 'test']);
genericTestSettings.setHost('localhost');
genericTestSettings.setPort(5201);
genericTestSettings.setInterval(0.1);
genericTestSettings.setDuration(60);

export { genericTestSettings };
