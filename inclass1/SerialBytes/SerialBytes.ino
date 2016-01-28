/*

 */


byte i;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  i=0;
}

// the loop routine runs over and over again forever:
void loop() {
  int val = analogRead(A0);
  val = map(val, 0, 1023, 0, 255);
  Serial.write(val);
  
  // print out the value:
  /*Serial.write(i);
  i += 1;
  
  if(i>=255)
    i=0;
  
  delay(10);        // delay in between reads for stability
  */
}
