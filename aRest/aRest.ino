// Libraries
#include <SPI.h>
#include <Ethernet.h>
#include <aREST.h>
#include <avr/wdt.h>

// Enter a MAC address for your controller below.
byte mac[] = { 0x90, 0xA2, 0xDA, 0x0E, 0xFE, 0x40 };

// IP address in case DHCP fails
IPAddress ip(172,16,0,2);

// Ethernet server
EthernetServer server(80);

// Create aREST instance
aREST rest = aREST();

// Declare functions to be exposed to the API
int initialize();

void setup(void)
{
  // Start Serial
  Serial.begin(9600);
  Serial.println("Initializing relays");
  initialize();

  // Give name & ID to the device (ID should be 6 characters long)
  rest.set_id("000001");
  rest.set_name("power_relay");

  // Start the Ethernet connection and the server
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    // no point in carrying on, so do nothing forevermore:
    // try to congifure using IP address instead of DHCP:
    Ethernet.begin(mac, ip);
  }
  
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());

  // Start watchdog
  wdt_enable(WDTO_4S);
}

void loop() {

  // listen for incoming clients
  EthernetClient client = server.available();
  rest.handle(client);
  wdt_reset();

}

int initialize() {

  for (int i = 22; i <=29; i++) {
    pinMode(i,OUTPUT);
    digitalWrite(i,HIGH);
  }

  for (int i = 39; i <=46; i++) {
    pinMode(i,OUTPUT);
    digitalWrite(i,HIGH);
  }

}
