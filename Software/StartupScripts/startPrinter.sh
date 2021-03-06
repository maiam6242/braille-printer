#!/bin/bash

sleep 10

# Start braille printer script
cd /home/pi/Desktop/braille-printer/Software/
python3 bp_runner.py &
pid[0]=$!

# Start website code
cd WebInterface
python3 main.py &
pid[1]=$!

# End all child scripts at exit
trap "kill ${pid[0]} ${pid[1]}; exit 1" INT

# Check if scripts are running and restart if they are not
while true; do 

    if ! kill -0 ${pid[0]};
    then
        cd /home/pi/Desktop/braille-printer/Software/
        python3 bp_runner.py &
        pid[0]=$!
    fi

    if ! kill -0 ${pid[1]};
    then
        cd /home/pi/Desktop/braille-printer/Software/WebInterface
        python3 main.py &
        pid[1]=$!
    fi

done

