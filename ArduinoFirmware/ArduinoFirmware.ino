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

    int selectedPins[] = {24,25,26,27,28,29,30,31,32,33,34,35,36,37};
    Solenoid solenoid;
    solenoid.setPins(selectedPins);
    HorizontalStepper horizontalStepper(3, 2, 4, 5, 2000, 4000);
    PaperStepper paperStepper(6,7,8, 200, 4000);
    GcodeInterpreter interpreter;

    while (1){
        interpreter.executeCommand(horizontalStepper, paperStepper, solenoid);
    }
}