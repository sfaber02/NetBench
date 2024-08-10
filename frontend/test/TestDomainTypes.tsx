import { DomainTestSettings, DomainTestPacket } from '../src/types/DomainTypes';
import { TestSettings, TestPacket } from '../src/grpc_client/proto/generated/netbench_pb';
import {genericTestSettings} from "../src/grpc_client/BaseTestSettings";

describe('DomainTestSettings', () => {
    it('should correctly initialize with genericTestSettings values', () => {
        const domainTestSettings = new DomainTestSettings();

        expect(domainTestSettings.title).toBe(genericTestSettings.getTitle());
        expect(domainTestSettings.tags).toEqual(genericTestSettings.getTagsList());
        expect(domainTestSettings.host).toBe(genericTestSettings.getHost());
        expect(domainTestSettings.port).toBe(genericTestSettings.getPort());
        expect(domainTestSettings.interval).toBe(genericTestSettings.getInterval());
        expect(domainTestSettings.duration).toBe(genericTestSettings.getDuration());
    });

    it('should correctly convert from proto', () => {
        const proto = new TestSettings();
        proto.setTitle('Test Title');
        proto.setTagsList(['tag1', 'tag2']);
        proto.setHost('localhost');
        proto.setPort(8080);
        proto.setInterval(10);
        proto.setDuration(60);

        const domainTestSettings = new DomainTestSettings().fromProto(proto);

        expect(domainTestSettings.title).toBe('Test Title');
        expect(domainTestSettings.tags).toEqual(['tag1', 'tag2']);
        expect(domainTestSettings.host).toBe('localhost');
        expect(domainTestSettings.port).toBe(8080);
        expect(domainTestSettings.interval).toBe(10);
        expect(domainTestSettings.duration).toBe(60);
    });

    it('should correctly convert to proto', () => {
        const domainTestSettings = new DomainTestSettings();
        domainTestSettings.title = 'Test Title';
        domainTestSettings.tags = ['tag1', 'tag2'];
        domainTestSettings.host = 'localhost';
        domainTestSettings.port = 8080;
        domainTestSettings.interval = 10;
        domainTestSettings.duration = 60;

        const proto = domainTestSettings.toProto(domainTestSettings);

        expect(proto.getTitle()).toBe('Test Title');
        expect(proto.getTagsList()).toEqual(['tag1', 'tag2']);
        expect(proto.getHost()).toBe('localhost');
        expect(proto.getPort()).toBe(8080);
        expect(proto.getInterval()).toBe(10);
        expect(proto.getDuration()).toBe(60);
    });
});

describe('DomainTestPacket', () => {
    it('should correctly convert from proto', () => {
        const proto = new TestPacket();
        proto.setTime(123456789);
        proto.setBitspersecond(1000);

        const domainTestPacket = new DomainTestPacket().fromProto(proto);

        expect(domainTestPacket.time).toBe(123456789);
        expect(domainTestPacket.bitsPerSecond).toBe(1000);
    });

    it('should correctly convert to proto', () => {
        const domainTestPacket = new DomainTestPacket();
        domainTestPacket.time = 123456789;
        domainTestPacket.bitsPerSecond = 1000;

        const proto = domainTestPacket.toProto(domainTestPacket);

        expect(proto.getTime()).toBe(123456789);
        expect(proto.getBitspersecond()).toBe(1000);
    });
});
