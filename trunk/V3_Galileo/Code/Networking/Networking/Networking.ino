#include <SPI.h>
#include <Ethernet.h>
// MAC address for the Galileo (there’s a sticker on the Ethernet connector)
//byte mac[] = { 0x??, 0x??, 0x??, 0x??, 0x??, 0x?? };
byte mac[] = { 0x98, 0x4F, 0xEE, 0x00, 0x6D, 0x16 };
//the IP address for the Galileo: (will be used if there’s no DHCP server on your network)
byte ip[] = { 192, 168, 0, 115 };
boolean Networking;
void setup() 
{
  delay(5000); //let the time time to open the serial monitor
  Networking = false;
  Serial.begin(9600);
  Serial.println("Attempting to configure Ethernet using DHCP");
  if (Ethernet.begin(mac) == 0) 
    {

      Serial.println("Failed to configure Ethernet using DHCP");
      Serial.println("Attempting to configure Ethernet using Static IP");
      Ethernet.begin(mac, ip);
      Serial.println(" Please check ifconfig");
      system("ifup eth0"); // load Ethernet interface!
      Networking = false;
    }
    else 
    {
      Serial.println("Sounds good");
     
      Networking = true;
    }
}
void loop () 
{
  if (Networking)
  {
          Serial.println("Connected to network");
  }
  else
  {
          Serial.println("Can not Connect to network");
  }
  
}

