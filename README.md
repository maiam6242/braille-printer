# Portabraille Printer by Team Dot Dot Dot

<img src="https://github.com/maiam6242/braille-printer/blob/master/README%20Resources/smileLogo2.JPG" alt="Team dot dot dot logo" width="250"/>

### The Portabraille Printer is a portable and accessible braille printer which enables users who are visually impaired to quickly and easily produce accurate, high quality braille.

## Table of Contents
- [Introduction](#Introduction "Introduction")
- [This Repository](#This-Repository "This Repository") 
- [Features](#Features "Features") 
- [Requirements](#Requirements "Requirements")
- [Installation](#Installation "Installation")  
- [Deployment](#Deployment "Deployment")
- [Feedback](#Feedback "Feedback") 
- [Team](#Team "Team")  
- [Acknowledgments](#Acknowledgments "Acknowledgments") 

## Introduction
The Portabraille Printer is a device that takes in an English text input, translates that text into (**SPECIFY CONTRACTED V UNCONTRACTED**) braille, then prints said braille text on braille paper. It is a low cost product that aims to allow people who are visually impaired to create braille quickly, with applications ranging from producing quick meeting notes to creating accessible promotional materials on the fly. (**CHECK THIS**) The printer is light, with a handle for easy transportation, and has an easy-to-use interface with both braille and English text, creating a user friendly experience for those who are visually impaired or blind.

## This Repository
**#TODO: Add to this**
This repository contains the vast majority of the files which we created over the course of this project. The [Text Side Folder](https://github.com/maiam6242/braille-printer/tree/master/Text%20Side "Text Side Folder") has software that takes a text input, converts it to a braille output and sends it to the firmware. All of this is written in Python. The firmware that controls the way paper is loaded and how solenoids act is in the [Arduino Firmware Folder](https://github.com/maiam6242/braille-printer/tree/master/ArduinoFirmware "Arduino Firmware Folder"). All of our firmware is written in C++. The [Interface Folder](https://github.com/maiam6242/braille-printer/tree/master/Interface "Interface Folder") contains software written in Python and designs created in Illustrator which relate to the user interface on our printer. The [PCB Folder](https://github.com/maiam6242/braille-printer/tree/master/PCB "PCB Folder") contains all of the artifacts from our PCB design and the [README Resources Folder](https://github.com/maiam6242/braille-printer/tree/master/README%20Resources "README Resources Folder") contains all of the files referenced in this document.

## Features 


## Requirements

- Python 3.6 **CHECK THESE**
- Raspberry Pi ?? (running raspbian blah blah blah)

## Installation
The software that runs on the Portabraille Printer has a variety of dependencies. The [startup bash script](https://github.com/maiam6242/braille-printer/blob/master/startup.bash "Startup Bash Script") automatically installs all of the dependencies from all components of our firmware and software. Instructions and code samples for installing these dependencies individually are below. 

**#TODO: Add to and edit this**
#### Python Text to Speech
The following bash command installs pyttsx3, a text to speech library for Python. 
``` bash
pip3 install pyttsx3
```

#### NumPy
The following bash command installs NumPy, a package for computing with Python. 
``` bash
pip3 install numpy
```

#### GPIO Zero
The following bash command installs GPIO Zero, a library for interfacing GPIO devices with Raspberry Pi.
``` bash
pip3 install gpiozero
```

#### PySerial
The following bash command installs pySerial, a module for accessing the serial port.
``` bash
pip3 install pyserial
```

#### eSpeak
The following bash command installs eSpeak, an open source speech synthesizer for Linux and Windows.
```bash
sudo apt-get install espeak
```

#### Flask
The following bash command installs Flask, a microweb framework.
```bash
pip3 install Flask
```

## Deployment


## Feedback
We would love to hear feedback on this project! Feel free to [email us](mailto:mmaterman@olin.edu "mmaterman@olin.edu") or [submit an issue](https://github.com/maiam6242/braille-printer/issues/new "New Issue Request"). If you are interested in contributing to this project or chatting about it in general, please don't hesitate to [email us](mailto:mmaterman@olin.edu "mmaterman@olin.edu") here!

## Team
Annie Tor [@ator1](https://github.com/ator1 "Annie's GitHub")   
Colin Snow [@colinmsnow](https://github.com/colinmsnow "Colin's GitHub")  
Maia Materman [@maiam6242](https://github.com/maiam6242 "Maia's GitHub")  
Megan Ku [@megku4u](https://github.com/megku4u "Megan's GitHub")  
Nathan Weil [@NWeil](https://github.com/NWeil "Nathan's GitHub")  

## Acknowledgments
Thanks to the Fall 2019 Principles of Engineering Teaching Team, Professors Aaron Hoover, Amon Millner, Siddhartan Govindasamy and Stan Reifel for their support and assistance throughout this process. Additional thanks to Frank Ventura, Jerry Berrier, David Kingsbury, John Smith, and Jeanette **LASTNAME** and for their INDISPENSABLE help during this adventure. The insights they provided about our design helped us craft a product that is actually usable. Lastly, thank you to the MIT Visually Impaired and Blind User Group for hosting us and letting us pick their brains regarding our printer and braille in general.
