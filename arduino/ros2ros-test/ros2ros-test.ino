#include <ros.h>
#include <std_msgs/UInt8MultiArray.h>

ros::NodeHandle  nh;

//std_msgs::UInt8MultiArray num_msg;
//ros::Publisher chatter("chatter", &num_msg);


void messageCb(const std_msgs::UInt8MultiArray& msg){
  Serial.println("statr");
  Serial.print(msg.data[0]);

//  num_msg.data = msg.data;
//  chatter.publish( &num_msg );

  delay(100);
}

ros::Subscriber<std_msgs::UInt8MultiArray> sub("arduino_angle", &messageCb );

void setup()
{ 
  Serial.begin(9600);
  nh.initNode();
  nh.subscribe(sub);
    
  Serial.print("start!");
  delay(1000);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
