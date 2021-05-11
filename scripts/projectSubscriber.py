#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32


class FastSubscriber:
    def __init__(self, topic_name):
        self.sub = rospy.Subscriber(topic_name, Float32, self.fastCallback)

    def fastCallback(self, ros_data):
        rospy.loginfo("FastCallback: " +str(ros_data.data))


class SlowSubscriber:
    def __init__(self, topic_name):
        # Subscribing to topic_name, using float32 and slowCallback which is a method of the class, reason for "self"
        self.sub = rospy.Subscriber(topic_name, Float32, self.slowCallback, queue_size=1)

    def slowCallback(self, ros_data): # accept variables of itself (under OOP) and ros_data which is the data received

        rate = rospy.Rate(1)
        for i in xrange(0, 5): # loop to wait for 5 secs and after that we will print
            rate.sleep()
        
        rospy.loginfo("SlowCallback: " + str(ros_data.data))



if __name__ == "__main__":
    rospy.init_node("double_subscriber") # Create a node called "double_subscriber"

    subscriber_fast = FastSubscriber("topic_1") #calling the class for the two subscriber
    subscriber_slow = SlowSubscriber("topic_2")

    rospy.spin() # Keep executing until press ctrl+C
