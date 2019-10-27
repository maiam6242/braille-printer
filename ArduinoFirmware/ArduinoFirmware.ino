// Firmware for Braille Printer on Arduino
// Created by Colin Snow on 10/27/19

#include "Steppers.h"
#include "Solenoid.h"


// Stepper class creates basic functionalities for a stepper motor

int pins[] = {5,6,7,8,9,10,11,12,13,14,15,16,17,18};
Solenoid solenoid(pins);
void setup(){

    Serial.begin(9600);
}

void loop(){

    bool solenoidsToFire[14] =  {1,1,0,0,0,0,0,0,0,0,0,0,0,0};

    solenoid.fire(solenoidsToFire, 20);


    delay(100000000);
}



