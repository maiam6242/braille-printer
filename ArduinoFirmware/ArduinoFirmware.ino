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

        // Stepper(int step_pin, int direction_pin, int enable_pin){
        //     stepPin = step_pin;
        //     directionPin = direction_pin;
        //     enablePin = enable_pin;
        //     pinMode(stepPin, OUTPUT);
        //     pinMode(directionPin,OUTPUT);
        //     pinMode(enablePin,OUTPUT);

        // }

        int getPosition() {return position;}
        void setPosition(int value) {position = value;}
        int getStepPin() {return stepPin;}
        void setStepPin(int value) {stepPin = value;}
        int getDirectionPin() {return directionPin;}
        void setDirectionPin(int value) {directionPin = value;}
        int getEnablePin() {return enablePin;}
        void setEnablePin(int value) {enablePin = value;}

        void activate(){digitalWrite(enablePin, LOW);}
        void deactivate(){digitalWrite(enablePin, HIGH);}


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

            for (int i = 1; i<abs(steps); i++){

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

// A stepper object which has added functionality for moving to one of eight positions
class HorizontalStepper :  public Stepper {

    protected:
        int homePin;
        int stepsPerCharacter = 20; // How many steps it needs to move to move one character over
        int stepsToFirstCharacter = 30; // Steps needed to get to origin

    public:

        HorizontalStepper(int step_pin, int direction_pin, int enable_pin, int home_pin){
            stepPin = step_pin;
            directionPin = direction_pin;
            enablePin = enable_pin;
            homePin = home_pin;
            pinMode(stepPin, OUTPUT);
            pinMode(directionPin,OUTPUT);
            pinMode(enablePin,OUTPUT);
            pinMode(homePin,INPUT);
        }

        void home(){

            activate();

            digitalWrite(directionPin, LOW);

            while (! digitalRead(homePin)){
                stepOnce();
                delay(1000/30);
            }

            step(30, 10);

            digitalWrite(directionPin, LOW);

            while (! digitalRead(homePin)){
                stepOnce();
                delay(1000/10);
            }

            step(stepsToFirstCharacter, 10);

            position = 0;

            deactivate();
        }

        void goToCharacter(int desiredCharacter, int stepsPerSecond){

            int desiredPosition = desiredCharacter * stepsPerCharacter;

            goTo(desiredPosition, stepsPerSecond);
        }
};


class PaperStepper : Stepper{

    protected:
    int loadSteps = 50; // Number of steps needed to load in Paper
    int unloadSteps = 100; // Number of steps needed to unload Paper
    int stepsPerCharacter = 40; // Number of steps to move up one chaacter


    public:
        PaperStepper(int step_pin, int direction_pin, int enable_pin){
            stepPin = step_pin;
            directionPin = direction_pin;
            enablePin = enable_pin;
            pinMode(stepPin, OUTPUT);
            pinMode(directionPin,OUTPUT);
            pinMode(enablePin,OUTPUT);
        }

        load(int stepsPerSecond){
            step(loadSteps, stepsPerSecond);
            position = 0;
        }

        unload(int stepsPerSecond){
            step(unloadSteps, stepsPerSecond);
        }

        void goToCharacter(int desiredCharacter, int stepsPerSecond){

            int desiredPosition = desiredCharacter * stepsPerCharacter;

            goTo(desiredPosition, stepsPerSecond);
        }
};


PaperStepper stepper(3, 2, 4);

void setup(){

    Serial.begin(9600);
}

void loop(){

    // stepper.activate();
    // stepper.goTo(100, 20);
    // delay(1000);
    // stepper.goTo(0, 20);
    // stepper.deactivate();
    // delay(1000);

    stepper.load(40);

    delay(100000000);
}



