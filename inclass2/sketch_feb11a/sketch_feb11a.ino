/*

 */


byte i;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(57600);
}

// the loop routine runs over and over again forever:
void loop() {
  int val = analogRead(A0);
  byte val_byte = map(val, 0, 1023, 0, 255);
  Serial.write(val_byte);
  delay(1);
}

