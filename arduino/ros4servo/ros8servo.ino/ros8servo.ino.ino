
#include <Servo.h>
#include <ros.h>
#include <std_msgs/UInt8MultiArray.h>

ros::NodeHandle  nh;

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

void messageCb(const std_msgs::UInt8MultiArray& msg){
  Serial.print(msg.data[0]);
  
  servo1.write(msg.data[0]);
  servo2.write(msg.data[1]);
  servo3.write(msg.data[2]);
  servo4.write(msg.data[3]);
 
  servo5.write(msg.data[4]);
  servo6.write(msg.data[5]);
  servo7.write(msg.data[6]);
  servo8.write(msg.data[7]);
  
  delay(100);
}

ros::Subscriber<std_msgs::UInt8MultiArray> sub("arduino_angle", &messageCb );

void setup()
{ 
  Serial.begin(9600);
  nh.initNode();
  nh.subscribe(sub);
  
  servo1.attach(SERVO_PIN1);
  servo2.attach(SERVO_PIN2);
  servo3.attach(SERVO_PIN3);
  servo4.attach(SERVO_PIN4);
  
  servo5.attach(SERVO_PIN5);
  servo6.attach(SERVO_PIN6);
  servo7.attach(SERVO_PIN7);
  servo8.attach(SERVO_PIN8);

  servo1.write(145);
  servo2.write(135);
  servo3.write(35);
  servo4.write(45);
  
  servo5.write(160);
  servo6.write(110);
  servo7.write(20);
  servo8.write(70);
  
  Serial.print("start!");
  delay(1000);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
