#!usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__=='__main__':
    rospy.init_node("draw_circle")  #used to initate the node with custom name which is independent of the file name
    rospy.loginfo("this node has been started")  #loginfo to show the msg on the terminal

    pub = rospy.Publisher("/turtle1/cmd_vel" , Twist , queue_size=10)  #defining the publisher

    rate = rospy.Rate(1.0) #refresh rate @10hz

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x=5
        msg.linear.y =1
        msg.angular.z=3
        pub.publish(msg)   #publishing the topic msg
        rate.sleep()
