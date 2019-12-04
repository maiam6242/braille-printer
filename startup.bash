#!/bin/bash

# Please run me as an admin! If not, I won't be able to talk to you. That'd be sad for both of us :)

if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo:"
    echo "sudo $0 $*"
    exit 1
fi

cd 

# pip3 installs
pip3 install pyttsx3
pip3 install numpy
pip3 install gpiozero
pip3 install pyserial

#apt-get installs
apt-get install espeak
apt-get install flask

#github
cd Desktop
git clone https://github.com/maiam6242/braille-printer.git

