#include <Servo.h>

const int SERVO_PIN1 = 2;
const int SERVO_PIN2 = 3;
const int SERVO_PIN3 = 4;
const int SERVO_PIN4 = 5;
const int SERVO_PIN5 = 6;
const int SERVO_PIN6 = 7;
const int SERVO_PIN7 = 8;
const int SERVO_PIN8 = 9;

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
Servo servo7;
Servo servo8;

void setup()
{ 
  Serial.begin(9600);
  
  servo1.attach(SERVO_PIN1);
  servo2.attach(SERVO_PIN2);
  servo3.attach(SERVO_PIN3);
  servo4.attach(SERVO_PIN4);
  
  servo5.attach(SERVO_PIN5);
  servo6.attach(SERVO_PIN6);
  servo7.attach(SERVO_PIN7);
  servo8.attach(SERVO_PIN8);

  servo1.write(90);
  servo2.write(90);
  servo3.write(90);
  servo4.write(90);
  
  servo5.write(90);
  servo6.write(90);
  servo7.write(90);
  servo8.write(90);
  
  Serial.print("start!");
  delay(1000);
}

void loop()
{  
}
