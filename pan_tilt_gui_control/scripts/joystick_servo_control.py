#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64

def callback(data):
    pan = data.axes[0] * 1.57
    tilt = data.axes[1] * 0.78
    rospy.loginfo(f"Pan: {pan:.2f}, Tilt: {tilt:.2f}")
    pan_pub.publish(pan)
    tilt_pub.publish(tilt)

if __name__ == '__main__':
    rospy.init_node('joystick_servo_control')
    pan_pub = rospy.Publisher('/pan_controller/command', Float64, queue_size=10)
    tilt_pub = rospy.Publisher('/tilt_controller/command', Float64, queue_size=10)
    rospy.Subscriber("/joy", Joy, callback)
    rospy.spin()
