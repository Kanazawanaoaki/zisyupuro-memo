#include <Servo.h>

// サーボのピン番号
const int SERVO_PIN1 = 8;
const int SERVO_PIN2 = 9;
// サーボのインスタンス
Servo servo1;
Servo servo2;

// INITがtrueの時は、モーターの位置を0にするだけ
const bool INIT = false;
//const bool INIT = true;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);  
  servo1.attach(SERVO_PIN1);
  servo1.write(0);
  servo2.attach(SERVO_PIN2);
  servo2.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
  servo1.write(0);
  servo2.write(0);
  if (INIT) return;
  Serial.print("start\n");
  servo1.write(0);
  Serial.print("0\n");
  delay(2000);
  servo1.write(180);
  Serial.print("180\n");
  delay(2000);
  servo1.write(90);
  Serial.print("90\n");
  delay(2000);
  servo1.writeMicroseconds(1000);
  servo2.write(90);
  delay(2000);
  servo1.writeMicroseconds(2000);
  delay(2000);
  servo1.writeMicroseconds(1500);
  servo2.write(180);
  delay(4000);
}
