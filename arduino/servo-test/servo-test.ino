#include <Servo.h>

// サーボのピン番号
const int SERVO_PIN = 8;

// サーボのインスタンス
Servo servo;

// INITがtrueの時は、モーターの位置を0にするだけ
const bool INIT = false;//true;
//const bool INIT = true;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);  
  servo.attach(SERVO_PIN);
  servo.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (INIT) return;
  Serial.print("start\n");
  servo.write(0);
  Serial.print("0\n");
  delay(2000);
  servo.write(180);
  Serial.print("180\n");
  delay(2000);
  servo.write(90);
  Serial.print("90\n");
  delay(2000);
  servo.writeMicroseconds(1000);
  delay(2000);
  servo.writeMicroseconds(2000);
  delay(2000);
  servo.writeMicroseconds(1500);
  delay(4000);
}
