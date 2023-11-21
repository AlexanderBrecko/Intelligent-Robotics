#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():

    rospy.init_node('turtle_move', anonymous=True)
    velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    print("Let's move your robot")
    speed = input("Input your speed:")
    distance = input("Type your distance:")
    isForward = input("Forward?:") #True or False

    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)

    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    while(current_distance < distance):
        velocity_publisher.publish(vel_msg)
        t1=rospy.Time.now().to_sec()
        current_distance = speed*(t1-t0)
        rospy.loginfo(current_distance)

    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            move()
    except rospy.ROSInterruptException: pass