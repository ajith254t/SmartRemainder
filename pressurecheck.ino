int sensorPin = A0;
int sensorValue = 0;
int threshold = 100;  // Adjust based on testing

void setup() {
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(sensorPin);
  Serial.print("Sensor Value: ");
  Serial.println(sensorValue);

  if (sensorValue > threshold) {
    Serial.println("Person Sitting");
  } else {
    Serial.println("Person Left");
  }

  delay(500);
}
