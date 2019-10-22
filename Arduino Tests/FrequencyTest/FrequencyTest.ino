/*
Program to test viable punching frequency for one solenoid

Created by Colin and Meg on 10/21
*/

long Frequency = 2;
int SolenoidPin = 2;
bool Solenoid = false;
// int time = millis();

void setup(){
    // Set baud rate
    Serial.begin(15200);
    pinMode(SolenoidPin,OUTPUT);

}


void loop(){

    getString();

    runSolenoid();





}


void getString(){
    if (Serial.available() > 0) {
        // read the incoming byte:
        String str = Serial.readString();

        if (str.charAt(0) == 'f'){

            if (str.charAt(1) == '?'){
                Serial.println(String("Frequency is : " +String(Frequency)));
            }
            else{
            
            str = str.substring(2);
            double value = str.toDouble();
            Serial.println(String("Frequency is : " +String( value)));
            Frequency = value;
            }
        }
    }
}

void runSolenoid(){
    int delayTime = int(1000./Frequency);

    digitalWrite(SolenoidPin, LOW);
    delay(delayTime*3/5);
    digitalWrite(SolenoidPin, HIGH);
    delay(delayTime*2/5);


    // if (millis() % delayTime == 0)
    // {
    //     if (Solenoid){
    //         digitalWrite(SolenoidPin, LOW);
    //         Solenoid = false;
    //     }
    //     else{
    //         digitalWrite(SolenoidPin, HIGH);
    //         Solenoid = true;
    //     }
        
    // }



}
