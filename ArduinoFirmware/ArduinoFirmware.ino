// Firmware for Braille Printer on Arduino
// Created by Colin Snow on 10/27/19

#include "Steppers.h"
#include "Solenoid.h"
#include "GcodeInterpreter.h"


// int selectedPins[] = {24,25,26,27,28,29,30,31,32,33,34,35,36,37};
// Solenoid solenoid(selectedPins);
// HorizontalStepper horizontalStepper(3,2,4,5);
// PaperStepper paperStepper(6,7,8);
// GcodeInterpreter interpreter; 



void setup(){

    Serial.begin(115200); 
    


}

void loop(){

    Solenoid solenoid;
    HorizontalStepper horizontalStepper;
    PaperStepper paperStepper;
    GcodeInterpreter interpreter;
    int selectedPins[] = {24,25,26,27,28,29,30,31,32,33,34,35,36,37};
    solenoid.setPins(selectedPins);
    horizontalStepper.setPins(3,2,4,5);
    paperStepper.setPins(6,7,8);

    while (1){
        
        interpreter.executeCommand(horizontalStepper, paperStepper, solenoid);
        delay(100);
    }

}

// void getString(){
//     if (Serial.available() > 0) {
//         // read the incoming byte:
//         String str = Serial.readString();
//         Serial.println(str);
//     }
// }




