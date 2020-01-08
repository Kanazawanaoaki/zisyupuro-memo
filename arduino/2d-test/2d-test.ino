#include <ros.h>
#include <trajectory_msgs/JointTrajectory.h>

ros::NodeHandle  nh;

void messageCb(const trajectory_msgs::JointTrajectory& msg){
  Serial.print(msg.joint_names[0]);
  Serial.print(msg.points[0].positions[0]);
}

ros::Subscriber<trajectory_msgs::JointTrajectory> sub("2d_human_joint", &messageCb );

void setup()
{ 
  Serial.begin(9600);
  nh.initNode();
  nh.subscribe(sub);
  Serial.print("start!");
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
