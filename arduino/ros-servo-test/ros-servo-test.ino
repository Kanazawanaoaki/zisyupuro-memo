/* 
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <std_msgs/Empty.h>
#include <Servo.h>

ros::NodeHandle  nh;

// サーボのピン番号
const int SERVO_PIN = 8;

// サーボのインスタンス
Servo servo;

int angle;

void messageCb( const std_msgs::Empty& toggle_msg){
  digitalWrite(LED_BUILTIN, HIGH-digitalRead(LED_BUILTIN));   // blink the led
  if (angle < 180){
    angle += 10;
  }else {
    angle = 0;
  }
  servo.write(angle);
  Serial.print(angle);
}

ros::Subscriber<std_msgs::Empty> sub("toggle_led", &messageCb );

void setup()
{ 
  pinMode(LED_BUILTIN, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
  angle = 0;
  Serial.begin(9600);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
