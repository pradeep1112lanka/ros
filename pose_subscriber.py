#!usr/bin/env python3
import rospy
from turtlesim.msg import Pose 

def pose_callback(msg: Pose):
    rospy.loginfo("(" +str(msg.x) + "," +str(msg.y)+ ")")   #writing the loginfo in another format
    rospy.sleep(0.5)
if __name__ == '__main__':
    rospy.init_node("turtle_pose_subscriber")
    sub = rospy.Subscriber("/turtle1/pose", Pose , callback=pose_callback)   #defining the subscriber node  
    rospy.loginfo("Node has been started")

    rospy.spin()  #Blocks until ROS node is shutdown. Yields activity to other threads
