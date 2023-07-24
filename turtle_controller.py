#!usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen

previous_x = 0    #defining a global variable
def call_set_pen_Service(r ,g ,b ,width ,off):  #defining a function to set colour thickness of the line drawn by turtle
    try: 
        set_pen = rospy.ServiceProxy("/turtle1/set_pen" , SetPen)
        response = set_pen(r,g,b,width,off)
    except rospy.ServiceException as e:
        rospy.logwarn(e)    

def pose_callback(pose: Pose):    #function to move turle and change colout
    cmd = Twist()
    if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0 :
        cmd.linear.x =  1
        cmd.angular.z = 1.4
    else :
        cmd.linear.x =  5.0
        cmd.angular.z = 0.0
    pub.publish(cmd)
    global previous_x
    if pose.x >= 5.5 and previous_x <5.5 :
        rospy.loginfo("colour set to red")
        call_set_pen_Service(250 , 0 , 0, 3, 0)
    elif pose.x<5.5 and previous_x >=5.5:
        rospy.loginfo("clour set to green")
        call_set_pen_Service(0, 250 , 0, 3, 0)
    previous_x = pose.x

if __name__ == '__main__':
    rospy.init_node("turtle_controller")
    rospy.wait_for_service("/turtle1/set_pen")
    pub = rospy.Publisher("/turtle1/cmd_vel" , Twist , queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose" , Pose , callback=pose_callback)
    rospy.loginfo("Node has been started")

    rospy.spin()
