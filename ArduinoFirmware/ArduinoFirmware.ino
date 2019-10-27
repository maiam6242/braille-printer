// Firmware for Braille Printer on Arduino
// Created by Colin Snow on 10/27/19



// Stepper class creates basic functionalities for a stepper motor
class Stepper{

    protected:
        int stepPin;
        int directionPin;
        int enablePin;
        int position;

    public:

        Stepper(int step_pin, int direction_pin, int enable_pin){
            stepPin = step_pin;
            directionPin = direction_pin;
            enablePin = enable_pin;

        }

        int getPosition() {return position;}
        void setPosition(int value) {position = value;}
        int getStepPin() {return stepPin;}
        void setStepPin(int value) {stepPin = value;}
        int getDirectionPin() {return directionPin;}
        void setDirectionPin(int value) {directionPin = value;}
        int getEnablePin() {return enablePin;}
        void setEnablePin(int value) {enablePin = value;}

        void activate(){digitalWrite(enablePin, HIGH);}
        void deactivate(){digitalWrite(enablePin, LOW);}


        // Steps the stepper once
        void stepOnce(){
            digitalWrite(stepPin, HIGH);
            digitalWrite(stepPin, LOW);
        }

        // Moves the stepper the specified number of steps at the given speed
        // Direction is away from home if positive or towards home if negative
        void step(int steps, int stepsPerSecond){

            if (steps >= 0){digitalWrite(directionPin, HIGH);}
            if (steps < 0){digitalWrite(directionPin, LOW);}

            for (int i = 1; i<steps; i++){

                stepOnce();
                delay(1000 / stepsPerSecond);
            }
            position += steps;
        }

        void goTo(int targetPosition, int stepsPerSecond){
            
            int stepsToGo = targetPosition - position;

            step(stepsToGo, stepsPerSecond);
        }

};


Stepper stepper(2, 3, 4);

void setup(){

    Serial.begin(9600);
}

void loop(){

    // stepper.activate();
    // stepper.step(100, 5);
    // stepper.deactivate();

    delay(1000);

}



