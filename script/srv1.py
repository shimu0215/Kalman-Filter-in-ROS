#!/usr/bin/env python

from __future__ import print_function

from hw1_1.srv import srv1, srv1Response
from hw1_1.msg import stateVector
import rospy


def handle(req):
    result = stateVector()
    result.position = 0
    result.velocity = 1
    print("handle")
    return srv1Response(result)


def server():
    rospy.init_node('srv1')
    s = rospy.Service('srv1', srv1, handle)
    print("srv1")
    rospy.spin()


if __name__ == "__main__":
    server()
