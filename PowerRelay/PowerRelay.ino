struct powerCommand {
  int relay;
  int command;
};

struct powerCommand newCommand;

void readCommand() {
  String r = Serial.readStringUntil(' ');
  String c = Serial.readString();
  newCommand.relay=r.toInt();
  newCommand.command=c.toInt();
}

void setup() {
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
  pinMode(A0,OUTPUT);
  pinMode(A1,OUTPUT);
  pinMode(A2,OUTPUT);
  pinMode(A3,OUTPUT);
  digitalWrite(2,HIGH);
  digitalWrite(3,HIGH);
  digitalWrite(4,HIGH);
  digitalWrite(5,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(7,HIGH);
  digitalWrite(8,HIGH);
  digitalWrite(9,HIGH);
  digitalWrite(10,HIGH);
  digitalWrite(11,HIGH);
  digitalWrite(12,HIGH);
  digitalWrite(13,LOW);
  digitalWrite(A0,LOW);
  digitalWrite(A1,LOW);
  digitalWrite(A2,LOW);
  digitalWrite(A3,LOW);
}

void loop() {
  if (Serial.available() > 0) {
    readCommand();
    switch (newCommand.relay){
      case 1:
        Serial.println("relay 1");
        if (newCommand.command) {
          digitalWrite(2, LOW);
        }
        else {
          digitalWrite(2,HIGH);
        }
        break;
      case 2:
        Serial.println("relay 2");
        if (newCommand.command) {
          digitalWrite(3, LOW);
        }
        else {
          digitalWrite(3,HIGH);
        }
        break;
      case 3:
        Serial.println("relay 3");
        if (newCommand.command) {
          digitalWrite(4, LOW);
        }
        else {
          digitalWrite(4,HIGH);
        }
        break;
      case 4:
        Serial.println("relay 4");
        if (newCommand.command) {
          digitalWrite(5, LOW);
        }
        else {
          digitalWrite(5,HIGH);
        }  
      break;
      case 5:
        Serial.println("relay 5");
        if (newCommand.command) {
          digitalWrite(6, LOW);
        }
        else {
          digitalWrite(6,HIGH);
        }
        break;
      case 6:
        Serial.println("relay 6");
        if (newCommand.command) {
          digitalWrite(7, LOW);
        }
        else {
          digitalWrite(7,HIGH);
        }
        break;
      case 7:
        Serial.println("relay 7");
        if (newCommand.command) {
          digitalWrite(8, LOW);
        }
        else {
          digitalWrite(8,HIGH);
        }
        break;
      case 8:
        Serial.println("relay 8");
        if (newCommand.command) {
          digitalWrite(9, LOW);
        }
        else {
          digitalWrite(9,HIGH);
        }
        break;
      case 9:
        Serial.println("relay 9");
        if (newCommand.command) {
          digitalWrite(10, LOW);
        }
        else {
          digitalWrite(10,HIGH);
        }
        break;
      case 10:
        Serial.println("relay 10");
        if (newCommand.command) {
          digitalWrite(11, LOW);
        }
        else {
          digitalWrite(11,HIGH);
        }
        break;
      case 11:
        Serial.println("relay 11");
        if (newCommand.command) {
          digitalWrite(12, LOW);
        }
        else {
          digitalWrite(12,HIGH);
        }
        break;
      case 12:
        Serial.println("relay 12");
        if (newCommand.command) {
          digitalWrite(13, LOW);
        }
        else {
          digitalWrite(13,HIGH);
        }
        break;
      case 13:
        Serial.println("relay 13");
        if (newCommand.command) {
          digitalWrite(A0, LOW);
        }
        else {
          digitalWrite(A0,HIGH);
        }
        break;
      case 14:
        Serial.println("relay 14");
        if (newCommand.command) {
          digitalWrite(A1, LOW);
        }
        else {
          digitalWrite(A1,HIGH);
        }
        break;
      case 15:
        Serial.println("relay 15");
        if (newCommand.command) {
          digitalWrite(A2, LOW);
        }
        else {
          digitalWrite(A2,HIGH);
        }
        break;
      case 16:
        Serial.println("relay 16");
        if (newCommand.command) {
          digitalWrite(A3, LOW);
        }
        else {
          digitalWrite(A3,HIGH);
        }
        break;
    }
    // say what you got:
    //Serial.print("I received: ");
    //Serial.println(val,DEC);
  }
}
