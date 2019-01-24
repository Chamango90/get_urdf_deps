#!/usr/bin/env python

import rospy
import os


def wait_for_param(param, sleep_rate=1):
    rate = rospy.Rate(sleep_rate)
    while not (rospy.is_shutdown() or rospy.has_param(param)):
        rospy.loginfo("Waiting for param '%s' ...", param)
        rate.sleep()
    return


def read_param(param, sleep_rate=1):
    wait_for_param(param, sleep_rate)
    return rospy.get_param(param)


def save_to_file(content, path, filename):
    fpath = path + "/" + filename
    rospy.loginfo("RESULT:\n%s" % content)
    if not os.path.exists(path):
        os.makedirs(path)
    with open(fpath, "w") as f:
        f.write(content)
        rospy.loginfo("Saved to file %s!" % fpath)
