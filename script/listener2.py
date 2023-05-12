#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16


def callback(data):
    rospy.loginfo(rospy.get_caller_id() +
                  'result of Kalman Filter %s', data.data)


def listener():

    rospy.init_node('listener2', anonymous=True)

    rospy.Subscriber('chatter2', Int16, callback)

    rospy.spin()


if __name__ == '__main__':
    listener()
