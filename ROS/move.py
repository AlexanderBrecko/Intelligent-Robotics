#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

pub = None


def clbk_laser(msg):
    regions = {
        'vpravo': min(min(msg.ranges[0:240]), 10),
        'predok': min(min(msg.ranges[240:480]), 10),
        'vlavo': min(min(msg.ranges[480:720]), 10)
    }

    take_action(regions)


def take_action(regions):
    msg = Twist()
    linear_x = 0
    angular_z = 0

    stav = ""

    if regions['vpravo'] > 0.5 and regions['vlavo'] > 0.5 and regions['predok'] > 0.5:
        stav = "bez prekazky"
        linear_x = 1
        angular_z = 0
    elif regions['vpravo'] < 1.5 and regions['vlavo'] > 1.5 and regions['predok'] > 0.5:
        stav = "prekazka vpravo"
        linear_x = 0
        angular_z = -1
    elif regions['vpravo'] > 1.5 and regions['vlavo'] < 1.5 and regions['predok'] > 0.5:
        stav = "prekazka vlavo"
        linear_x = 0
        angular_z = -1
    elif regions['vpravo'] > 1.5 and regions['vlavo'] > 1.5 and regions['predok'] < 0.5:
        stav = "prekazka vpredu"
        linear_x = 0
        angular_z = -1
    elif regions['vpravo'] < 1.5 and regions['vlavo'] < 1.5 and regions['predok'] > 0.5:
        state_description = "prekazka po stranach robota"
        linear_x = 0.5
        angular_z = 0
    elif regions['vpravo'] < 1.5 and regions['vlavo'] < 1.5 and regions['predok'] < 0.5:
        tate_description = "prekazka vsade"
        linear_x = 0
        angular_z = -1
    elif regions['vpravo'] < 1.5 and regions['vlavo'] > 1.5 and regions['predok'] < 0.5:
        stav = "prekazka predok a pravo"
        linear_x = 0
        angular_z = -1
    else:
        state_description = "neznamy stav"
        rospy.loginfo(regions)

    msg.linear.x = linear_x
    msg.angular.z = angular_z
    pub.publish(msg)


def main():
    global pub

    rospy.init_node('reading_laser')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    sub = rospy.Subscriber('/mybot/laser/scan', LaserScan, clbk_laser)
    rospy.spin()


if __name__ == '__main__':
    main()