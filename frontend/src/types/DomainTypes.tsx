import {TestSettings, TestPacket, EmptyRequest} from "../grpc_client/proto/generated/netbench_pb";


class DomainTestSettings {
    public title!: string;
    public tags!: string[];
    public host!: string;
    public port!: number;
    public interval!: number;
    public duration!: number;

    public fromProto = (proto: TestSettings): DomainTestSettings => {
        const instance = new DomainTestSettings();
        instance.title = proto.getTitle();
        instance.tags = proto.getTagsList();
        instance.host = proto.getHost();
        instance.port = proto.getPort();
        instance.interval = proto.getInterval();
        instance.duration = proto.getDuration();
        return instance;
    }

    public toProto = (domainTestSettings: DomainTestSettings): TestSettings => {
        const proto = new TestSettings();
        proto.setTitle(domainTestSettings.title);
        proto.setTagsList(domainTestSettings.tags);
        proto.setHost(domainTestSettings.host);
        proto.setPort(domainTestSettings.port);
        proto.setInterval(domainTestSettings.interval);
        proto.setDuration(domainTestSettings.duration);
        return proto;
    }
}

class DomainTestPacket {
    public time!: number;
    public bitsPerSecond!: number;

    public fromProto = (proto: TestPacket): DomainTestPacket => {
        const instance = new DomainTestPacket();
        instance.time = proto.getTime();
        instance.bitsPerSecond = proto.getBitspersecond();
        return instance;
    }

    public toProto = (domainTestPacket: DomainTestPacket): TestPacket => {
        const proto = new TestPacket();
        proto.setTime(domainTestPacket.time);
        proto.setBitspersecond(domainTestPacket.bitsPerSecond);
        return proto;
    }
}


export {DomainTestSettings, DomainTestPacket}
