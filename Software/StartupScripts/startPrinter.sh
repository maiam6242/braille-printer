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

    if ! ps -p pid[0] > /dev/null
    then
        cd /home/pi/Desktop/braille-printer/Software/
        python3 bp_runner.py &
        pid[0]=$!
    fi

    if ! ps -p pid[1] > /dev/null
    then
        cd /home/pi/Desktop/braille-printer/Software/WebInterface
        python3 main.py &
        pid[1]=$!
    fi

    # Kill the subprocesses at exit
    trap "kill ${pid[0]} ${pid[1]}; exit 1" INT

done

wait

