class GcodeInterpreter{

    protected:
        int numSolenoids = 14;
        int solenoidTime = 200;
        int defaultSpeed = 2000;

    public:

        // Execute the command which is typed into the serial monitor
        // @args horizontalStepper The horizontal stepper object
        // @args paperStepper The paper stepper object
        // @args solenoid The solenoid object
        void executeCommand(HorizontalStepper& horizontalStepper, PaperStepper& paperStepper, Solenoid& solenoid){
            /*

            Commands:

            G28                     Home horizontal axis
            M17                     Enable all steppers
            M18                     Disable all steppers
            M701                    Load paper
            M702                    Unload paper
            G0 x val                Fast move to character on x axis
            G0 y val                Fast move to character on y axis
            G1 x val                Controlled move to character on x axis
            G1 y val                Controlled move to character on y axis
            F array(values(14))     Fire all solenoids with a 1 as their value
            
            */

            if (Serial.available() > 0) {
                Serial.println("Available");
                // read the incoming byte:
                String str = Serial.readString();
                Serial.println(str);
                // char input = str.toCharArray();


                if ( str.charAt(0) == 'G' && str.charAt(1) == '2' && str.charAt(2) == '8'){
                    Serial.println("Homing Horizontal Axis");
                    horizontalStepper.home(defaultSpeed);
                }

                if ( str.charAt(0) == 'M' && str.charAt(1) == '1' && str.charAt(2) == '7'){
                    Serial.println("Enabling all steppers");
                    horizontalStepper.enableOutputs();
                    paperStepper.enableOutputs();
                }

                if ( str.charAt(0) == 'M' && str.charAt(1) == '1' && str.charAt(2) == '8'){
                    Serial.println("Disabling all steppers");
                    horizontalStepper.disableOutputs();
                    paperStepper.disableOutputs();
                }
                if ( str.charAt(0) == 'M' && str.charAt(1) == '7' && str.charAt(2) == '0' && str.charAt(2) == '1'){
                    Serial.println("Loading paper");
                    paperStepper.load(defaultSpeed);
                }
                if ( str.charAt(0) == 'M' && str.charAt(1) == '7' && str.charAt(2) == '0' && str.charAt(2) == '2'){
                    Serial.println("Unloading paper");
                    paperStepper.unload(defaultSpeed);
                }

                if ( str.charAt(0) == 'G' && str.charAt(1) == '0'){
                    if (str.charAt(3) == 'x'){
                        str = str.substring(5);
                        int value = str.toDouble();
                        Serial.print("Going to x value: ");
                        Serial.println(value);
                        horizontalStepper.goToCharacter(value, defaultSpeed);
                    }
                    if (str.charAt(3) == 'y'){
                        str = str.substring(5);
                        int value = str.toDouble();
                        Serial.print("Going to y value: ");
                        Serial.println(value);
                        paperStepper.goToCharacter(value, defaultSpeed);
                    }
                }
                if ( str.charAt(0) == 'G' && str.charAt(1) == '1'){
                    if (str.charAt(3) == 'x'){
                        str = str.substring(5);
                        int value = str.toDouble();
                        Serial.print("Going to x value: ");
                        Serial.println(value);
                        horizontalStepper.goToCharacter(value, defaultSpeed / 2);
                    }
                    if (str.charAt(3) == 'y'){
                        str = str.substring(5);
                        int value = str.toDouble();
                        Serial.print("Going to y value: ");
                        Serial.println(value);
                        paperStepper.goToCharacter(value, defaultSpeed / 2);
                    }
                }

                if ( str.charAt(0) == 'F'){
                    String commandList = str.substring(2);
                    char solenoidFire[numSolenoids];
                    commandList.toCharArray(solenoidFire, numSolenoids+1);  // Need to add one because char arrays have 0 as default last value
                    int intFire[numSolenoids];
                    for (int i=0; i<numSolenoids; i++){
                        if (solenoidFire[i] == '1'){

                            intFire[i] = 1;
                        }
                        else{

                            intFire[i] = 0;
                        }
                        
                    }
                    solenoid.fire(intFire, solenoidTime);
                }
            }
        }




};