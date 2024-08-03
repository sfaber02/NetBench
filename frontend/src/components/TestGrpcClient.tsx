import {Component} from "react";
import {NetbenchClientWrapper} from "../grpc_client/NetbenchClientWrapper";
import {ServiceError} from '@grpc/grpc-js';
// import {grpcDataTypes} from "../types/GrpcTypes";
import {EmptyRequest, TestSettings, SaveSettingsResponse} from "../grpc_client/proto/generated/netbench_pb";


type State = {
    settings: TestSettings
}


class TestGrpcClientComponent extends Component<{}, State> {
    // private client: NetbenchClientWrapper;

    // constructor(props: {}) {
    //     super(props);
    //     this.state = { settings: null };
    //     this.client = new NetbenchClientWrapper();
    // }
    //
    // fetchSettings = () => {
    //     const request = new EmptyRequest()
    //
    //     this.client.getSettings((error: ServiceError | null, response: TestSettings) => {
    //         if (error) {
    //             console.error('Error:', error);
    //         } else {
    //             this.setState({ settings: response });
    //             console.log('TestSettings:', response.toObject());
    //         }
    //     })
    // }





    render() {
        return (
            // <div>
            //     <h1>Test gRPC Client</h1>
            //     <button onClick={this.fetchSettings}>Fetch Settings</button>
            //     {this.state.settings && (
            //         <div>
            //             <h2>Settings</h2>
            //             <pre>{JSON.stringify(this.state.settings.toObject(), null, 2)}</pre>
            //         </div>
            //     )}
            // </div>
            <div>
                <h1>Test gRPC Client</h1>
            </div>
        );
    }
}








export {TestGrpcClientComponent}
