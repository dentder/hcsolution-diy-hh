/*
  AnalogReadSerial
 Reads an analog input on pin 0, prints the result to the serial monitor 
 
 This example code is in the public domain.
 */

void setup() {
  Serial.begin(9600);
}

void loop() {
 Serial.print(" Arduino is testing ... \n");
 Serial.print(" ---===  waiting 5 secong then resend this message ===--- \n");  
 delay(5000);
 
}
