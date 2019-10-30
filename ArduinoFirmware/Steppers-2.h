// Stepper control module v2
// Created by Colin Snow on 10/29/19


#include <AccelStepper.h>

// A stepper object which has added functionality for moving to characters and homing
class HorizontalStepper :  public AccelStepper {

    protected:
        int homePin;
        int stepsPerCharacter = 20; // How many steps it needs to move to move one character over
        int stepsToFirstCharacter = 30; // Steps needed to get to origin

    public:

        HorizontalStepper (int step, int direction, int enable, int home_pin, int maxSpeed, int accel) : AccelStepper(step, direction){
            
            homePin = home_pin;
            setEnablePin(enable);
            setPinsInverted(false,false,true);
            setMaxSpeed(maxSpeed);
            setAcceleration(accel);
        }

        // Moves the stepper to the specified character
        // @param desiredCharacter The character to go to
        // @param stepsPerSecond The speed of the motor in steps/second
        void goToCharacter(int desiredCharacter, int speed){
            int desiredPosition = desiredCharacter * stepsPerCharacter;
            setMaxSpeed(speed);
            runToNewPosition(desiredPosition);
        }

        // Homes the horizontal axis
        void home(int speed){



            enableOutputs();
            setMaxSpeed(speed);

            while (! digitalRead(homePin)){

                int position = currentPosition();
                runToNewPosition(position -1);
            }

            setMaxSpeed(speed / 2);

            int position = currentPosition();
            runToNewPosition(position + 30);


            while (! digitalRead(homePin)){
                int position = currentPosition();
                runToNewPosition(position -1);
            }

            runToNewPosition(stepsToFirstCharacter);

            setCurrentPosition(0);

            

            disableOutputs();
        }

};

// A stepper object which handles paper controls such as going to character and loading
class PaperStepper : public AccelStepper{

    protected:
    int loadSteps = 50; // Number of steps needed to load in Paper
    int unloadSteps = 100; // Number of steps needed to unload Paper
    int stepsPerCharacter = 40; // Number of steps to move up one chaacter

    public:

        PaperStepper (int step, int direction, int enable, int maxSpeed, int accel) : AccelStepper(step, direction){
            setEnablePin(enable);
            setPinsInverted(false,false,true);
            setMaxSpeed(maxSpeed);
            setAcceleration(accel);
        }

        // Loads paper into the machine
        // @params stepsPerSecond The motor speed in steps/second
        void load(int speed){
            setCurrentPosition(0);
            setMaxSpeed(speed);
            runToNewPosition(loadSteps);
            setCurrentPosition(0);
        }

        // Unloads paper from the machine
        // @params stepsPerSecond The motor speed in steps/second
        void unload(int speed){
            int position = currentPosition();
            setMaxSpeed(speed);
            runToNewPosition(position + unloadSteps);
        }

        // Moves the stepper to the specified character
        // @param desiredCharacter The character to go to
        // @param stepsPerSecond The speed of the motor in steps/second
        void goToCharacter(int desiredCharacter, int speed){
            int desiredPosition = desiredCharacter * stepsPerCharacter;
            setMaxSpeed(speed);
            runToNewPosition(desiredPosition);
        }
};
