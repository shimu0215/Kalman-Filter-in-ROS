#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    talker(data)


def talker(data):
    new_prediction = 0 + 0.2 * data.data

    pub = rospy.Publisher('chatter2', Int16, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo(new_prediction)
        pub.publish(new_prediction)
        rate.sleep()


def listener():

    rospy.init_node('talker_listener', anonymous=True)

    rospy.Subscriber('chatter', Int16, callback)

    rospy.spin()


if __name__ == '__main__':
    listener()
