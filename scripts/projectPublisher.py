#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist # Import the geometry_msgs from Twist


class RemoteController: # A call called RemoteController
    def __init__(self):
        
        self.cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1) # Create an object for the pulisher with the name of the topic, Twist (type of the topic)

    
    def control(self, linear_vel, angular_vel):
        
        msg = Twist() # Define the velocity of robot
        msg.linear.x = linear_vel  # linear velocity of robot
        msg.angular.z = angular_vel # velocity for robot to rotate aroun z

        self.cmd_pub.publish(msg)  # publish the msg and send it to the node topic "cmd_vel"



if __name__ == '__main__':
    rospy.init_node("robot_controller") #Creating a node named "robot_controller"
    controller = RemoteController() 

    vel = -2 #-2m/s, define velocity

    rate = rospy.Rate(10) #frequency 

    counter = 0

    try:
        while not rospy.is_shutdown():

            if counter == 20: # above counting to 2seconds, reset the counter 
                vel = -vel
                counter = 0

            controller.control(vel, 0)
            rate.sleep()
            counter += 1 #increment counter
    except rospy.ROSInterruptException:
        rospy.loginfo("Got interrupt request")
    
    rospy.loginfo("Closing remote controller")