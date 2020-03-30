#!/usr/bin/env python

import rospy
from joystick_msgs.msg import JoystickMsg
from geometry_msgs.msg import Twist

class ControlRobot:
    def __init__(self):
        rospy.init_node('control_robot')
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/joystick_publisher', JoystickMsg, self.callback)
        self.x_mpd = 0.0
        self.y_mpd = 0.0
        self.rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            data_ = Twist()
            data_.linear.x = self.y_mpd
            data_.linear.y = 0.0
            data_.linear.z = 0.0

            data_.angular.x = 0.0
            data_.angular.y = 0.0
            data_.angular.z = self.x_mpd

            self.pub.publish(data_)
            self.rate.sleep()

    def map_(self, num, in_min, in_max, out_min, out_max):
        return (((num+0.0) - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def callback(self, data):
        self.x_mpd = self.map_(data.x, 0, 1023, 3.14, -3.14)
        self.y_mpd = self.map_(data.y, 0, 1023, -5, 5)

if __name__ == '__main__':
    try:
        ControlRobot()
    except rospy.ROSInterruptException:
        pass