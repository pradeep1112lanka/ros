#!usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("test_node")  #name of the node running in ros master
    rospy.loginfo("hello there")  #msg info
    rospy.logerr("this is a warning") #msg error
    rospy.logwarn("this is an warning")  #msg warning

    rospy.sleep(0.5)    #sleep for 0.5 sec 
    rate = rospy.Rate(1.0)
    while not rospy.is_shutdown():   #this runs untill the rospy file is not stopped 
        rospy.loginfo("this is the first node written by pradeep")
        rate.sleep()  #sleep @rate
    rospy.loginfo("end of the program")  #end note after closing program
