#include <SPI.h>
#include <Ethernet.h>
// Netwoking ver 2. Nguyen Hoang Hai.
// network configuration. dns server, gateway and subnet are optional.

byte mac[] = { 0x98, 0x4F, 0xEE, 0x00, 0x6D, 0x16 }; // Galileo MAC address
//the IP address for the Galileo: (will be used if there’s no DHCP server on your network)
IPAddress ip(192, 168, 0, 115);
boolean Networking;

// the dns server ip
IPAddress dnServer(192, 168, 0, 1);
// the router's gateway address:
IPAddress gateway(192, 168, 0, 1);
// the subnet:
IPAddress subnet(255, 255, 255, 0);

//the IP address is dependent on your network
int led = 13;

void setup() {
  Serial.begin(9600);

  // initialize the ethernet device
  Ethernet.begin(mac, ip, dnServer, gateway, subnet);
  //print out the IP address
  Serial.print("IP = ");
  Serial.println(Ethernet.localIP());
  pinMode(led, OUTPUT); // setting led for
}

void loop() {
  // blink so that you know your board is work
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(1000); 
  // end of blink
  Serial.print("IP = ");
  Serial.println(Ethernet.localIP()); // tell the local IP
}
