#!/usr/bin/env python

import rospy
from std_msgs import Float32

def callback_ReceiveBatteryStatus(batteryCharge):
    if (batteryCharge <= 85.0):
        # Shut the robot down.

        # Give the cleaning command.



if __name__ == '__main__':
    rospy.init_node('battery_monitor')

    sub = rospy.Subscriber("/robot1/battery/charge", Float32, callback_ReceiveBatteryStatus)

    rospy.spin()