#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def clbk_laser(msg):
    regions = [
        min(min(msg.ranges[0:240]),10),
        min(min(msg.ranges[240:480]),10),
        min(min(msg.ranges[480:720]),10)
    ]
    rospy.loginfo(regions)

def main():
    rospy.init_node('reading_sensor')
    sub = rospy.Subscriber('/mybot/laser/scan', LaserScan, clbk_laser)
    rospy.spin()

if __name__ == '__main__':
    main()
