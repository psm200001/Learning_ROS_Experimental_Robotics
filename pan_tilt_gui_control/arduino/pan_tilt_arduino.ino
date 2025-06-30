#include <Servo.h>
#include <ros.h>
#include <std_msgs/Float64.h>

Servo panServo;
Servo tiltServo;

ros::NodeHandle nh;

void pan_cb(const std_msgs::Float64 &msg) {
  int angle = constrain((int)(msg.data * 180.0 / 3.1415), 0, 180);
  panServo.write(angle);
}

void tilt_cb(const std_msgs::Float64 &msg) {
  int angle = constrain((int)(msg.data * 180.0 / 3.1415), 0, 180);
  tiltServo.write(angle);
}

ros::Subscriber<std_msgs::Float64> sub_pan("/pan_controller/command", pan_cb);
ros::Subscriber<std_msgs::Float64> sub_tilt("/tilt_controller/command", tilt_cb);

void setup() {
  nh.initNode();
  nh.subscribe(sub_pan);
  nh.subscribe(sub_tilt);

  panServo.attach(9);
  tiltServo.attach(10);
}

void loop() {
  nh.spinOnce();
  delay(10);
}
