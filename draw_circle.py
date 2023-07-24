#!usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__=='__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("this node has been started")

    pub = rospy.Publisher("/turtle1/cmd_vel" , Twist , queue_size=10)

    rate = rospy.Rate(1.0)

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x=5
        msg.linear.y =1
        msg.angular.z=3
        pub.publish(msg)
        rate.sleep()