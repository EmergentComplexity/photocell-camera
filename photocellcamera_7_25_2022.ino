





void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);


  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
}


void loop() {

  for( int i = 0; i < 8; i++) {
    digitalWrite(3, i & 0b001);
    digitalWrite(4, i & 0b010);
    digitalWrite(5, i & 0b100);
  
 
  int sensorValue0 = analogRead(A0);
  int sensorValue1 = analogRead(A1);
  int sensorValue2 = analogRead(A2);
  int sensorValue3 = analogRead(A3);
  int sensorValue4 = analogRead(A4);
  int sensorValue5 = analogRead(A5);
  // print out the value you read:

  int SENSE = 1023;
  int pixelValue0 = map(sensorValue0, 0, SENSE, 0, 255);
  int pixelValue1 = map(sensorValue1, 0, SENSE, 0, 255);
  int pixelValue2 = map(sensorValue2, 0, SENSE, 0, 255);
  int pixelValue3 = map(sensorValue3, 0, SENSE, 0, 255);
  int pixelValue4 = map(sensorValue4, 0, SENSE, 0, 255);
  int pixelValue5 = map(sensorValue5, 0, SENSE, 0, 255);

  
  Serial.print(pixelValue0);
  if(pixelValue0 < 10)
    Serial.print(" ");
  if(pixelValue0 < 100)
    Serial.print(" ");
  Serial.print(" ");

  Serial.print(pixelValue1);
  if(pixelValue1 < 10)
    Serial.print(" ");
  if(pixelValue1 < 100)
    Serial.print(" ");
  Serial.print(" ");

  Serial.print(pixelValue2);
  if(pixelValue2 < 10)
    Serial.print(" ");
  if(pixelValue2 < 100)
    Serial.print(" ");
  Serial.print(" ");

  Serial.print(pixelValue3);
  if(pixelValue3 < 10)
    Serial.print(" ");
  if(pixelValue3 < 100)
    Serial.print(" ");
  Serial.print(" ");

  Serial.print(pixelValue4);
  if(pixelValue4 < 10)
    Serial.print(" ");
  if(pixelValue4 < 100)
    Serial.print(" ");
  Serial.print(" ");

  Serial.print(pixelValue5);
  if(pixelValue5 < 10)
    Serial.print(" ");
  if(pixelValue5 < 100)
    Serial.print(" ");
  Serial.print(" ");
    delay(10);
    
  }  
  Serial.println(" ");
  delay(1000);   
}
