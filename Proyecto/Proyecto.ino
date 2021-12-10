#include <SPI.h>
#include <SD.h>

File file;

#define echoPin 2 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 3 //attach pin D3 Arduino to pin Trig of HC-SR04

// defines variables
double duration; // variable for the duration of sound wave travel
double distance; // variable for the distance measurement
double t;
double T;
//double vals[2];

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
}
void loop() {
  //if (Serial.available() > 0){
  // Clears the trigPin condition
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
    distance = duration * 0.034 / 2.0; // Speed of sound wave divided by 2 (go and back)
    t = millis();
    T = t/1000.0;
    file = SD.open("data.dat", FILE_WRITE);
  // Displays the distance on the Serial Monitor
  //Serial.print("Distance: ");
    Serial.print(distance);
    Serial.print('\n');
    Serial.println(T);
  //Serial.print(vals);
  //Serial.println(" ms");
    delay(300); // Send results every 300 millisecond 
  //}
}

