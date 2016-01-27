/*

 */


byte i;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(57600);
  i=0;
}

// the loop routine runs over and over again forever:
void loop() {
 
  // print out the value:
  Serial.write(i);
  i += 1;
  
  if(i>=255)
    i=0;
  
  delay(10);        // delay in between reads for stability
}
