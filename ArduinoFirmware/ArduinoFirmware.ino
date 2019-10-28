// Firmware for Braille Printer on Arduino
// Created by Colin Snow on 10/27/19

#include "Steppers.h"
#include "Solenoid.h"

class GcodeInterpreter{

    public:

        void executeCommand(HorizontalStepper horizontalStepper, PaperStepper paperStepper, Solenoid solenoid){

            // Serial.println("here");
            /*

            Commands:

            G28                     Home horizontal axis
            M17                     Enable all steppers
            M18                     Disable all steppers
            M701                    Load paper
            M702                    Unload paper
            G0 x val                Controlled move to character on x axis
            G0 y val                Controlled move to character on y axis
            



            */

            //    Serial.println("working");


            if (Serial.available() > 0) {
                Serial.println("Available");
                // read the incoming byte:
                String str = Serial.readString();
                Serial.println(str);
                // char input = str.toCharArray();


                if ( str.charAt(0) == 'G' && str.charAt(1) == '2' && str.charAt(2) == '8'){
                    Serial.println("Homing Horizontal Axis");
                    horizontalStepper.home();
                }

                if ( str.charAt(0) == 'M' && str.charAt(1) == '1' && str.charAt(2) == '7'){
                    Serial.println("Enabling all steppers");
                    horizontalStepper.activate();
                    paperStepper.activate();
                }

                if ( str.charAt(0) == 'M' && str.charAt(1) == '1' && str.charAt(2) == '8'){
                    Serial.println("Enabling all steppers");
                    horizontalStepper.deactivate();
                    paperStepper.deactivate();
                }
                if ( str.charAt(0) == 'M' && str.charAt(1) == '7' && str.charAt(2) == '0' && str.charAt(2) == '1'){
                    Serial.println("Enabling all steppers");
                    paperStepper.load(30);
                }
                if ( str.charAt(0) == 'M' && str.charAt(1) == '7' && str.charAt(2) == '0' && str.charAt(2) == '1'){
                    Serial.println("Enabling all steppers");
                    paperStepper.unload(30);
                }

                if ( str.charAt(0) == 'G' && str.charAt(1) == '0'){
                    Serial.println(str);
                    if (str.charAt(3) == 'x'){
                        str = str.substring(4);
                        int value = str.toDouble();
                        horizontalStepper.goToCharacter(value, 30);
                    }
                    if (str.charAt(3) == 'y'){
                        str = str.substring(4);
                        int value = str.toDouble();
                        paperStepper.goToCharacter(value, 30);
                    }
                }


            }
        }




};

int selectedPins[] = {24,25,26,27,28,29,30,31,32,33,34,35,36,37};
Solenoid solenoid(selectedPins);
HorizontalStepper horizontalStepper(3,2,4,5);
PaperStepper paperStepper(6,7,8);
GcodeInterpreter interpreter; 

void setup(){

    Serial.begin(115200); 

}

void loop(){


    // interpreter.executeCommand(horizontalStepper, paperStepper, solenoid);

    horizontalStepper.step(5, 30);



    // getString();


    delay(100);



    // bool solenoidsToFire[14] =  {1,1,0,0,0,0,0,0,0,0,0,0,0,0};

    // solenoid.fire(solenoidsToFire, 20);


    // delay(100000000);
}

void getString(){
    if (Serial.available() > 0) {
        // read the incoming byte:
        String str = Serial.readString();
        Serial.println(str);
    }
}




