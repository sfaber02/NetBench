# NetBench v 0.1
A tool to run netowrk speed benchmarks and create graphs of the results.


## Installation
1. Install python 3.11
2. Install PIP then pipenv
3. Install Bokeh `brew install bokeh`
3. Install iperf3 with `brew install iperf3` on a the host and a server
4. Run `pipenv install` from root of project


## Run

### Host
1. Start `iperf3` server on host machine with `iperf3 -s`
### Client
1. Enter pipenv shell `pipenv shell` must be python > 3.11
2. Start testing with `bokeh serve --show netbench.py` from root of project

## Ideas
- user inputs
    - save to file and load last inputs as defaults
- error / no data count
- implements tags
- add timestamp to each graph
- create default filename for saving
- make y axis lable dynamic based on units Mbits Mbytes etc