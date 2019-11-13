class GcodeInterpreter{

    protected:
        int numSolenoids = 14;
        int solenoidTime = 200;
        int defaultSpeed = 8000;
        bool machineMode = false; // Mode determines whether it is in human or machine interaction mode. Defaults to human

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
            M21                     Toggle machine-read mode
            M114                    Print Positions
            G0 x val                Fast move to character on x axis
            G0 y val                Fast move to character on y axis
            G1 x val                Controlled move to character on x axis
            G1 y val                Controlled move to character on y axis
            F array(values(14))     Fire all solenoids with a 1 as their value


            I hate all of this code please fix
            
            */

            if (Serial.available() > 0) {
                // read the incoming byte:
                String str = Serial.readString();
                // if (machineMode){
                //     Serial.println(str);
                // }

                if ( str.charAt(0) == 'M' && str.charAt(1) == '2' && str.charAt(2) == '1'){
                    machineMode = !machineMode;
                    if (machineMode){
                        Serial.println('0');
                    }
                }
                if ( str.charAt(0) == 'G' && str.charAt(1) == '2' && str.charAt(2) == '8'){
                    if (!machineMode){
                        Serial.println("Homing Horizontal Axis");
                    }
                    horizontalStepper.home(defaultSpeed);
                    if (machineMode){
                        Serial.println('0');
                    }
                }
                if ( str.charAt(0) == 'M' && str.charAt(1) == '1' && str.charAt(2) == '7'){
                    if (!machineMode){
                        Serial.println("Enabling all steppers");
                    }
                    horizontalStepper.enable();
                    paperStepper.enable();
                    if (machineMode){
                        Serial.println('0');
                    }
                }
                if ( str.charAt(0) == 'M' && str.charAt(1) == '1' && str.charAt(2) == '8'){
                    if (!machineMode){
                        Serial.println("Disabling all steppers");
                    }
                    horizontalStepper.disable();
                    paperStepper.disable();
                    if (machineMode){
                        Serial.println('0');
                    }
                }
                if ( str.charAt(0) == 'M' && str.charAt(1) == '7' && str.charAt(2) == '0' && str.charAt(3) == '1'){
                    if (!machineMode){
                        Serial.println("Loading paper");
                    }
                    paperStepper.load(defaultSpeed);
                    if (machineMode){
                        Serial.println('0');
                    }
                }
                if ( str.charAt(0) == 'M' && str.charAt(1) == '7' && str.charAt(2) == '0' && str.charAt(3) == '2'){
                    if (!machineMode){
                        Serial.println("Unloading paper");
                    }
                    paperStepper.unload(defaultSpeed);
                    if (machineMode){
                        Serial.println('0');
                    }
                }
                if ( str.charAt(0) == 'G' && str.charAt(1) == '0'){
                    if (str.charAt(3) == 'x'){
                        str = str.substring(5);
                        double value = str.toDouble();
                        if (!machineMode){
                            Serial.print("Going to x value: ");
                            Serial.println(value);
                        }
                        horizontalStepper.goTomm(value, defaultSpeed);
                        if (machineMode){
                        Serial.println('0');
                        }
                    }
                    if (str.charAt(3) == 'y'){
                        str = str.substring(5);
                        double value = str.toDouble();
                        if (!machineMode){
                            Serial.print("Going to y value: ");
                            Serial.println(value);
                        }
                        paperStepper.goTomm(value, defaultSpeed);
                        if (machineMode){
                        Serial.println('0');
                        }
                    }
                }
                if ( str.charAt(0) == 'G' && str.charAt(1) == '1'){
                    if (str.charAt(3) == 'x'){
                        str = str.substring(5);
                        double value = str.toDouble();
                        if (!machineMode){
                            Serial.print("Going to x value: ");
                            Serial.println(value);
                        }
                        horizontalStepper.goTomm(value, (defaultSpeed / 8));
                        if (machineMode){
                            Serial.println('0');
                        }
                    }
                    if (str.charAt(3) == 'y'){
                        str = str.substring(5);
                        double value = str.toDouble();
                        if (!machineMode){
                            Serial.print("Going to y value: ");
                            Serial.println(value);
                        }
                        paperStepper.goTomm(value, (defaultSpeed / 8));
                        if (machineMode){
                            Serial.println('0');
                        }
                    }
                }
                if ( str.charAt(0) == 'F'){
                    String commandList = str.substring(2);
                    char solenoidFire[numSolenoids+1];
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
                    solenoid.fire(intFire, solenoidTime, machineMode);
                    if (machineMode){
                        Serial.println('0');
                    }
                }
                if ( str.charAt(0) == 'M' && str.charAt(1) == '1' && str.charAt(2) == '1' && str.charAt(3) == '4'){
                    if (!machineMode){
                        Serial.print("Position:");
                        Serial.print(horizontalStepper.currentmm());
                        Serial.print(",");
                        Serial.println(paperStepper.currentmm());
                    }
                    if (machineMode){
                        Serial.print("Position: ");
                        Serial.print(horizontalStepper.currentmm());
                        Serial.print(",");
                        Serial.println(paperStepper.currentmm());
                    }
                }
            }
        }
};