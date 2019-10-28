// Stepper control module
// Created by Colin Snow on 10/27/19

// Base class for controlling stepper motors
class Stepper{

    protected:

        int stepPin;
        int directionPin;
        int enablePin;
        int position;

    public:

        // getters and setters

        int getPosition() {return position;}
        void setPosition(int value) {position = value;}
        int getStepPin() {return stepPin;}
        void setStepPin(int value) {stepPin = value;}
        int getDirectionPin() {return directionPin;}
        void setDirectionPin(int value) {directionPin = value;}
        int getEnablePin() {return enablePin;}
        void setEnablePin(int value) {enablePin = value;}

        // Activates stepper
        void activate(){digitalWrite(enablePin, LOW);}
        // Deactivates stepper
        void deactivate(){digitalWrite(enablePin, HIGH);}


        // Steps the stepper once
        void stepOnce(){
            digitalWrite(stepPin, HIGH);
            digitalWrite(stepPin, LOW);
        }

        // Moves the stepper the specified number of steps at the given speed
        // @param steps Number of steps to move
        // @param stepsPerSecond The speed of the motor in steps/second
        void step(int steps, int stepsPerSecond){

            if (steps >= 0){digitalWrite(directionPin, HIGH);}
            if (steps < 0){digitalWrite(directionPin, LOW);}

            for (int i = 1; i<abs(steps); i++){

                stepOnce();
                delay(1000 / stepsPerSecond);
            }
            position += steps;
        }

        // Moves the stepper to an absolute position
        // @param targetPosition The position to move to
        // @param stepsPerSecond The speed of the motor in steps/second
        void goTo(int targetPosition, int stepsPerSecond){

            int stepsToGo = targetPosition - position;
            step(stepsToGo, stepsPerSecond);
        }

};

// A stepper object which has added functionality for moving to characters and homing
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

        // Homes the horizontal axis
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

        // Moves the stepper to the specified character
        // @param desiredCharacter The character to go to
        // @param stepsPerSecond The speed of the motor in steps/second
        void goToCharacter(int desiredCharacter, int stepsPerSecond){

            int desiredPosition = desiredCharacter * stepsPerCharacter;

            goTo(desiredPosition, stepsPerSecond);
        }
};

// A stepper object which handles paper controls such as going to character and loading
class PaperStepper : public Stepper{

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

        // Loads paper into the machine
        // @params stepsPerSecond The motor speed in steps/second
        void load(int stepsPerSecond){
            step(loadSteps, stepsPerSecond);
            position = 0;
        }

        // Unloads paper from the machine
        // @params stepsPerSecond The motor speed in steps/second
        void unload(int stepsPerSecond){
            step(unloadSteps, stepsPerSecond);
        }

        // Moves the stepper to the specified character
        // @param desiredCharacter The character to go to
        // @param stepsPerSecond The speed of the motor in steps/second
        void goToCharacter(int desiredCharacter, int stepsPerSecond){

            int desiredPosition = desiredCharacter * stepsPerCharacter;

            goTo(desiredPosition, stepsPerSecond);
        }
};
