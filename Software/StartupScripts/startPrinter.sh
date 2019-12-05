#!/bin/bash

# Start braille printer script
cd /home/pi/Desktop/braille-printer/Software/
python3 bp_runner.py &
pid[0]=$!

# Start website code
cd WebInterface
python3 main.py &
pid[1]=$!


trap "kill ${pid[0]} ${pid[1]}; exit 1" INT
wait

# trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT
