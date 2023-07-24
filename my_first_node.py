#!usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("test_node")  #name of the node running in ros master
    rospy.loginfo("hello there")
    rospy.logerr("this is a warning")
    rospy.logwarn("this is an warning")

    rospy.sleep(0.5)
    rate = rospy.Rate(1.0)
    while not rospy.is_shutdown():
        rospy.loginfo("this is the first node written by pradeep")
        rate.sleep()
    rospy.loginfo("end of the program")