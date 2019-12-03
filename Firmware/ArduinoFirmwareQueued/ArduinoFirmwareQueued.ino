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

    // int selectedPins[] = {23,25,27,29,31,33,35,37,39,41,43,45,47,49};
    int selectedPins[] = {37,41,39,47,49,45,43,31,23,35,33,27,25,29};
    // int selectedPins[] = {2,3,4,5,6,7,35,37,39,41,43,45,47,49};
    Solenoid solenoid;
    solenoid.setPins(selectedPins);
    HorizontalStepper horizontalStepper(26, 28, 24, 36, 2000, 8000);
    PaperStepper paperStepper(32,34,30,42, 200, 8000);
    GcodeInterpreter interpreter;

    while (1){
        interpreter.executeCommand(horizontalStepper, paperStepper, solenoid);
    }
}