#include <Servo.h>

// サーボのピン番号
const int SERVO_PIN = 8;

// サーボのインスタンス
Servo servo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);  
  servo.attach(SERVO_PIN);
  servo.write(0);
  Serial.print("start!\n");
  delay(1000);
}

void loop() {
  servo.write(90);
}
