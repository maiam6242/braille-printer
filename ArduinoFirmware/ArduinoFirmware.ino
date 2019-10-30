// Firmware for Braille Printer on Arduino
// Created by Colin Snow on 10/27/19

#include "Steppers-2.h"
#include <AccelStepper.h>
#include "Solenoid.h"
#include "GcodeInterpreter.h"

void setup(){
    Serial.begin(115200); 
}

void loop(){

    Solenoid solenoid;
    HorizontalStepper horizontalStepper(3, 2, 4, 5, 2000, 2000);
    PaperStepper paperStepper(6,7,8, 200, 2000);
    GcodeInterpreter interpreter;

    while (1){
        interpreter.executeCommand(horizontalStepper, paperStepper, solenoid);
    }
}