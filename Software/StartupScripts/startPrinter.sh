#!/bin/bash

# Start braille printer script
cd /home/pi/Desktop/braille-printer/Software/
python3 bp_runner.py &

# Start website code
cd WebInterface
python3 main.py &

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT