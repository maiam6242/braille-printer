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
            G0 x val                Fast move to character on x axis
            G0 y val                Fast move to character on y axis
            G1 x val                Controlled move to character on x axis
            G1 y val                Controlled move to character on y axis
            



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
                    Serial.println("Disabling all steppers");
                    horizontalStepper.deactivate();
                    paperStepper.deactivate();
                }
                if ( str.charAt(0) == 'M' && str.charAt(1) == '7' && str.charAt(2) == '0' && str.charAt(2) == '1'){
                    Serial.println("Loading paper");
                    paperStepper.load(30);
                }
                if ( str.charAt(0) == 'M' && str.charAt(1) == '7' && str.charAt(2) == '0' && str.charAt(2) == '2'){
                    Serial.println("Unloading paper");
                    paperStepper.unload(30);
                }

                if ( str.charAt(0) == 'G' && str.charAt(1) == '0'){
                    Serial.println(str);
                    if (str.charAt(3) == 'x'){
                        str = str.substring(5);
                        int value = str.toDouble();
                        Serial.print("Going to x value: ");
                        Serial.println(value);
                        horizontalStepper.goToCharacter(value, 40);
                    }
                    if (str.charAt(3) == 'y'){
                        str = str.substring(5);
                        int value = str.toDouble();
                        Serial.print("Going to y value: ");
                        Serial.println(value);
                        paperStepper.goToCharacter(value, 40);
                    }
                }
                if ( str.charAt(0) == 'G' && str.charAt(1) == '1'){
                    Serial.println(str);
                    if (str.charAt(3) == 'x'){
                        str = str.substring(5);
                        int value = str.toDouble();
                        Serial.print("Going to x value: ");
                        Serial.println(value);
                        horizontalStepper.goToCharacter(value, 20);
                    }
                    if (str.charAt(3) == 'y'){
                        str = str.substring(5);
                        int value = str.toDouble();
                        Serial.print("Going to y value: ");
                        Serial.println(value);
                        paperStepper.goToCharacter(value, 20);
                    }
                }


            }
        }




};