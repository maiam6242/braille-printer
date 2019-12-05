#!/bin/bash

# Start braille printer script
cd /home/pi/Desktop/braille-printer/Software/
python3 bp_runner.py &
pid[0]=$!

# Start website code
cd WebInterface
python3 main.py &
pid[1]=$!


while true; do 

    if ! kill -0 $(pid[0])
    then
        cd /home/pi/Desktop/braille-printer/Software/
        python3 bp_runner.py &
        pid[0]=$!
    fi

    if ! kill -0 $(pid[1])
    then
        cd /home/pi/Desktop/braille-printer/Software/WebInterface
        python3 main.py &
        pid[1]=$!
    fi

    # Kill the subprocesses at exit

done

trap "kill ${pid[0]} ${pid[1]}; exit 1" INT

wait

