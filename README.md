# ROS_Speed
This project is implemented for a Robot with different speed limit

## Overview
The project contains a publisher and a subscriber class which two different speed subscribers. The subscribe message help control the speed and limit of the robot.

## Dependencies
* The project uses Ubuntu 20.04.
* The project make us of the ROS OS Noetic. To install, follow the link.
* The project uses catkin build system.
* The project uses the gazebo simulation.

## Running the codes
1. Run roscore on a new terminal
2. Create a catkin workspace
3. cd ~/catkin_ws/
4. Run source ~/catkin_ws/devel/setup.bash (A good practice)
5. Cloning this repository

### Run the Publisher
* On a different terminal, at the script level “roscd scripts” Run chmod +x *.py
* In cd catkin_ws, we will source the devel setup.bash file with the code - source/devel/setup.bash
* The projectPublisher.py can be run using the code - rosrun my_robot_tuturial projectPublisher.py
* Then launch the husky robot with gazebo using the code - roslaunch husky_gazebo husky_playpen.launch

### Run the subscriber
* Run roscore on a different terminal (if not running)
* Run source ~/catkin_ws/devel/setup.bash (A good practice)
* On a different terminal, at the script level “roscd scripts” Run chmod +x *.py
* At the scripts level, run “rosrun my_robot_tutorial projectSubscriber.py”
* On another terminal, at the scripts level, run - rostopic pub -r 10 /topic_1 std_msgs/Float32 “data:1.0”
* On a different terminal, at the scripts level, run - rostopic pub -r 10 /topic_2 std_msgs/Float32 “data:2.0”
