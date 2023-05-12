#!/usr/bin/env python
from __future__ import print_function
import sys
import rospy

from hw1_1.srv import *
from hw1_1.msg import stateVector


def client():
    rospy.wait_for_service('srv1')
    sensor = rospy.ServiceProxy('srv1', srv1)
    res = sensor()
    return res


if __name__ == "__main__":
    print("Call empty srv, srv1")
    result = client()
    print(result.output_data)
