# NetBench v 0.1
A tool to run netowrk speed benchmarks and create graphs of the results.


## Installation
1. Run `pipenv install` from root of project
2. Install python 3.11
3. Install iperf3 with `brew install iperf3`
2. May need to run <br> 
```export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/Cellar/iperf3/3.16/lib/:$DYLD_FALLBACK_LIBRARY_PATH``` <br>
on an ARM Apple Machine to probably link required lib.

## Run
1. Start `iperf3` server on host machine with `iperf3 -s`
2. Configure `.env` file on client with host IP and port of server
3. Enter python shell with `pipenv --python 3.11` followed by `pipenv shell`
4. run application with `python main.py` from root of project