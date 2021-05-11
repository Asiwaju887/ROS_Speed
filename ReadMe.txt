README
For Additional Project 1 and 2 below: projectPublisher & projectSubscriber
ROS Command - This code is meant to be implemented with the husky robot
1. To run the projectPublisher.py code with the husky robot on gazebo simulator, we can
follow the following steps:
a. Run roscore on a different terminal
b. Run source ~/catkin_ws/devel/setup.bash (A good practice)
c. On a different terminal, at the script level “roscd scripts” Run chmod +x *.py
d. In cd catkin_ws, we will source the devel setup.bash file with the code -
source/devel/setup.bash
e. The projectPublisher.py can be run using the code - rosrun my_robot_tuturial
projectPublisher.py
f. Then launch the husky robot with gazebo using the code - roslaunch
husky_gazebo husky_playpen.launch
All things being equal the robot will be moving with the code on the gazebo simulator.
2. To run the projectPublisher.py and projectSubscriber.py, with the following steps:
a. Run roscore on a different terminal
b. Run source ~/catkin_ws/devel/setup.bash (A good practice)
c. On a different terminal, at the script level “roscd scripts” Run chmod +x *.py
d. At the scripts level, run “rosrun my_robot_tutorial projectSubscriber.py”
e. On another terminal, at the scripts level, run - rostopic pub -r 10 /topic_1
std_msgs/Float32 “data:1.0”
f. On a different terminal, at the scripts level, run - rostopic pub -r 10 /topic_2
std_msgs/Float32 “data:2.0”