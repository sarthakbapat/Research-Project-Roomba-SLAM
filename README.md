iRobot Roomba SLAM, Swarming and Scheduling.
---------------------------------------------

The project consists of creation of a Robotic swarm system of two robots using iRobot's Roomba (Vaccum cleaning robot). The idea is to run a ROS master on one robot and launch both the robots in different namespaces so that the recognition of each individual robot is easy. We are not working with ROS2 and hence no use case of multiple ROS masters here.

The project also contains the scheduling of individual robots based on the meeting entries in the calendar. The idea here is to schedule the robots navigation exactly 45 mins before the meeting time and this happens only once. The meeting time and the calendar data is fetched using the MQTT protocol and integrated with the ROS functionality of moving the robot.

The folder catkin_ws contains all the necessary ROS packages. It also contains the code to launch the robot in a namespace. This setup is for one robot, the same code and setup can be used with another robot. Only the catkin_ws files containing the namespace have to be modified (only the namespace name).

The python scripts are in the folder Scripts. The file Calender.py is the main file and goal_navigate.py contains the code for navigation of the robot. The coordinates.yaml file contains the coordinates of the goal location in the mapped region.


The details of the implementation are included in the Project Report: (https://github.com/sarthakbapat/Research-Project-Roomba-SLAM/blob/main/ProjectReport/Project_Report.pdf)
