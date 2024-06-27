# NetBench v 0.1
A tool to run network speed benchmarks and create graphs of the results.


## Installation
1. Install python 3.11
2. Install PIP then pipenv
4. Run `pipenv install` from root of project


## Run

### Server
1. On server machine download iperf3 from [here](https://iperf.fr/iperf-download.php)
2. Start `iperf3` in server mode with `iperf3 -s` taking note of ip and port the server is running on.
### Client
1. Enter pipenv shell `pipenv shell` must be python > 3.11
2. Install bokeh graphing library with `pip install bokeh`
3. Start testing with `start-test.sh` from root of project and follow terminal instructions.


## Build
Alternately you can compile an executeable for arm macs.  Presently there is only an executeable for the client, not the server.  We have plans to cross compile client / server binaries for all platforms in the future.

You can build an executable by installing `pyinstaller`
And running `pyinstaller netbench.spec` from the root of the project

## Example of a test graph.
![screenshot of netbench graph](<Screenshot 2024-06-24 at 8.47.41 PM.png>)


## Ideas
- user inputs
    - save to file and load last inputs as defaults
- error / no data count
- implements tags
- add timestamp to each graph
- create default filename for saving
- make y axis lable dynamic based on units Mbits Mbytes etc
- change iperf settings to use json and eliminate parsing
- gracefully end test and graphing
