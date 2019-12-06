#include <Servo.h>

//拾ったサーボ用のやつ

// サーボのピン番号
const int SERVO_PIN = 8;

Servo servo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);  
  servo.attach(SERVO_PIN);
  servo.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("start\n");
  servo.write(0);
  Serial.print("0\n");
  delay(2000);
  servo.write(200);
  Serial.print("150\n");
  delay(2000);
}
