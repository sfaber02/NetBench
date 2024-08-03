 #!/bin/bash

grpc_tools_node_protoc \
--proto_path=./src/grpc_client/proto \
--ts_out=grpc_js:./src/grpc_client/proto/generated \
--js_out=import_style=commonjs,binary:./src/grpc_client/proto/generated \
--grpc_out=generate_package_defintion:./src/grpc_client/proto/generated \
./src/grpc_client/proto/netbench.proto
