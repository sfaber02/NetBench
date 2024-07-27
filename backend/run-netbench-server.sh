#! /bin/bash

# Set the PYTHONPATH to the current directory
# Needs to be root of the project
export PYTHONPATH=./

# start server
python ./src/api/netbench_server.py
