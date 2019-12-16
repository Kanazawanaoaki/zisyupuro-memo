#include <Servo.h>

// サーボのピン番号
const int SERVO_PIN = 8;

// サーボのインスタンス
Servo servo;

// スイッチ用
const int SWITCH_PIN = 4;
int state = 1;

// INITがtrueの時は、モーターの位置を0にするだけ
const bool INIT = false;
//const bool INIT = true;

void setup(){
  pinMode( SWITCH_PIN, INPUT );
  Serial.begin( 9600 );
  servo.attach(SERVO_PIN);
  servo.write(0);
}


void angle_test(){
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

  
}



void loop(){
  if (digitalRead( SWITCH_PIN ) ==  0){
    if (state == 1) {
      state = 0;
    }
    else {
      state = 1;
      Serial.println("stop!");
      delay(2000);
       
    }
  }

  if (state == 0){
    Serial.println(state);  
    angle_test();
  }
}
