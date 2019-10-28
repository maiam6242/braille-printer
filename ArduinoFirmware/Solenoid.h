// Solenoid control module
// Created by Colin Snow on 10/27/19

class Solenoid {

    protected:
        int solenoidNumber = 14;
        int pins[]; 

    public:
        void setPins(int *givenPins){

            for (int i=0; i < solenoidNumber; i++){

                pins[i] = givenPins[i];
                // Serial.println(pins[i]);
                pinMode(pins[i], OUTPUT);

            }
        }

        // Fires specified solenoids for specified amount of time
        // @param givenPins An array of booleans which determines which solenoids to fire
        // @param time The amount of time to hold the pin down
        void fire(bool *givenPins, int time){
            for (int i=0; i < sizeof(givenPins); i++){

                if (givenPins[i] == 1){
                    digitalWrite(pins[i], HIGH);
                    Serial.print("Solenoid fired:");
                    Serial.println(pins[i]);

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
