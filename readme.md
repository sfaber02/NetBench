# NetBench v 0.1
A tool to run network speed benchmarks and create graphs of the results.


## Installation
1. Install python 3.11
2. Install PIP then pipenv
4. Run `pipenv install` from root of project


## Run

### Host
1. Start `iperf3` server on host machine with `iperf3 -s`
### Client
1. Enter pipenv shell `pipenv shell` must be python > 3.11
2. Start testing with `start-test.sh` from root of project


## Build
Currently the iperf c library is compiled for arm macs.  
You can build an executable on mac by installing `pyinstaller`
And running `pyinstaller netbench.spec` from the root of the project


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
