# iRobot Roomba SLAM, Swarming and Scheduling.
The project consists of creation of a Robotic swarm system of two robots using iRobot's Roomba (Vaccum cleaning robot). The idea is to run a ROS master on one robot and launch both the robots in different namespaces so that the recognition of each individual robot is easy. We are not working with ROS2 and hence no use case of multiple ROS masters here.

The project also contains the scheduling of individual robots based on the meeting entries in the calendar. The idea here is to schedule the robots navigation exactly 45 mins before the meeting time and this happens only once. The meeting time and the calendar data is fetched using the MQTT protocol and integrated with the ROS functionality of moving the robot.
## Folders
### - catkin_ws 
The folder catkin_ws contains all the necessary ROS packages. It also contains the code to launch the robot in a namespace. This setup is for one robot, the same code and setup can be used with another robot. Only the catkin_ws files containing the namespace have to be modified (only the namespace name).
### - Scripts
The python scripts are in the folder Scripts. The file Calender.py is the main file and goal_navigate.py contains the code for navigation of the robot. The coordinates.yaml file contains the coordinates of the goal location in the mapped region.
### - ProjectReport
The details of the implementation are included in the Project Report: [Link](https://github.com/sarthakbapat/Research-Project-Roomba-SLAM/blob/main/ProjectReport/Project_Report.pdf "Link") 

## Instructions for use

### ROS Master Configuration

To configure a single ROS master system for our swarm, we have to set a variable
ROS_MASTER_URI with the appropriate IP address in the bashrc file on both the Roombas as well as the linux PC. The IP address of the robot which is the master has to be set in ROS_MASTER_URI variable in bashrc file on the second robot and the linux system that runs the rviz tool. Following example assumes ROS master is running on Robot_1.

#### Robot_1 bashrc

`$ export ROS_MASTER_URI = http://10.36.28.212:11311`

`$ export ROS_HOSTNAME = http://10.36.28.212`

#### Robot_2 bashrc

`$ export ROS_MASTER_URI = http://10.36.28.212:11311`

`$ export ROS_HOSTNAME = http://10.36.28.216`

#### Linux PC bashrc

`$ export ROS_MASTER_URI = http://10.36.28.212:11311`

`$ export ROS_HOSTNAME = http://10.36.28.213`

## Using the Roomba Swarm
Once the ROS master configuration is done then the roombas are accessed in the following manner.

The map vsLabFinalMap.pgm and vsLabFinalMap.yaml files are included and the cmd to launch the map server is already written in move_base.launch file. So no need to launch the map server explicitly.

######  Launch the create2 
   `$  roslaunch ca_driver create_2.launch`
   
######  Launch ydlidar   
   `$  roslaunch ydlidar lidar.launch`
   
######    Launch the move_base and the map server
   `$  roslaunch roomba_2dnav move_base.launch`
   
######    Start the RVIZ on linux PC
   `$   rosrun rviz rviz `

The 'Script' folder can be placed outside the catkin_ws on both the Roombas.  The Scripts folder is kept at the /home/Ubuntu/Documents location in both the Roombas. To start the navigation of the robots to their goal locations, run

    python Calender.py

Follow the similar steps on the second robot (except launching the RVIZ) and the robots will work as expected.

   
