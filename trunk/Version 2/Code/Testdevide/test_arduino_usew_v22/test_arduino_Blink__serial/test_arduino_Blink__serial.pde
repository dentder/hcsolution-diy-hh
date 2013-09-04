/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
  Send the serial signal through FDTI
  This example code is in the public domain.
 */

void setup() {                
  // initialize the digital pin as an output.
  // Pin 17 has an LED connected on most Arduino boards:
  pinMode(13, OUTPUT);     
    Serial.begin(9600);
}



void loop() {
  digitalWrite(13, HIGH);   // set the LED on
  delay(1000);              // wait for a second
  digitalWrite(13, LOW);    // set the LED off
  delay(1000);              // wait for a second
  Serial.print(" Arduino is testing ... \n");
 Serial.print(" ---===  waiting 5 secong then resend this message ===--- \n");  
 delay(1000);
}
