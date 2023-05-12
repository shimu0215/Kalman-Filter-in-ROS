#!/usr/bin/env python
import random

import rospy
from std_msgs.msg import String, Int16


def talker():
    pub = rospy.Publisher('chatter', Int16, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        input_str = raw_input("Assumed robot position: ")
        user_int = int(input_str)
        user_int = int(random.gauss(user_int, 2))
        rospy.loginfo(user_int)
        pub.publish(user_int)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
