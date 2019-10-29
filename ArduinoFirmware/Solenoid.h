// Solenoid control module
// Created by Colin Snow on 10/27/19

class Solenoid {


    int solenoidNumber = 14;
        // int pins[solenoidNumber] = {24,25,26,27,28,29,30,31,32,33,34,35,36,37};
    int pins[14];

        

    public:


        void setPins(int *givenPins){

            for (int i=0; i < solenoidNumber; i++){

                pins[i] = givenPins[i];
                Serial.print(pins[i]);
                Serial.print(" , ");
                Serial.println(givenPins[i]);
                pinMode(pins[i], OUTPUT);

            }
        }

        // Fires specified solenoids for specified amount of time
        // @param givenPins An array of booleans which determines which solenoids to fire
        // @param time The amount of time to hold the pin down
        void fire(int *triggeredPins, int time){
            for (int i=0; i < solenoidNumber; i++){

                Serial.print(pins[i]);
                Serial.print(" , ");
                Serial.println(triggeredPins[i]);

                if (triggeredPins[i] == 1){
                    digitalWrite(pins[i], HIGH);
                    Serial.print("Solenoid fired:");
                

                }

            }

            delay(time);

            for (int i=0; i < solenoidNumber; i++){
                digitalWrite(pins[i], LOW);
                Serial.print("Solenoid retracted:");
                Serial.println(pins[i]);
            }
        }
};
