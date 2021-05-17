# This is a python script to navigate a robot to a goal location by sending the co-ordinates to the ROS Navigation stack.

import sys 
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

class NavigateGoal:

    def __init__(self, xGoal, yGoal, orientation_x=0.0, orientation_y=0.0, orientation_z=0.0, orientation_w=0.0):
        self.xGoal = xGoal
        self.yGoal = yGoal
        self.orientation = [orientation_x, orientation_y, orientation_z, orientation_w]
        

    def movebase_client(self):
        #Create a actionlib client object.
        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

        while (not client.wait_for_server(rospy.Duration.from_sec(10.0))):
            rospy.loginfo ("Waiting for the move_base action server to come up")

        goal = MoveBaseGoal()

        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        goal.target_pose.pose.position = Point(self.xGoal, self.yGoal, 0)
        goal.target_pose.pose.orientation.x = self.orientation[0]
        goal.target_pose.pose.orientation.y = self.orientation[1]
        goal.target_pose.pose.orientation.z = self.orientation[2]
        goal.target_pose.pose.orientation.w = self.orientation[3]

        rospy.loginfo ("Sending goal location")
        client.send_goal(goal)

        client.wait_for_result()

        if (client.get_state() == GoalStatus.SUCCEEDED):
            rospy.loginfo("Goal Reached !")
        else:
            rospy.loginfo("Failed to reach the destination")

if __name__ == '__main__':
    try:
        rospy.init_node("/navigation_goal", anonymous = False)

        xGoal = (float)(sys.argv[1])
        yGoal = (float)(sys.argv[2])
        xOri = (float)(sys.argv[3])
        yOri = (float)(sys.argv[4])
        zOri = (float)(sys.argv[5])
        wOri = (float)(sys.argv[6])

        navigate = NavigateGoal(xGoal, yGoal, xOri, yOri, zOri, wOri)
        navigate.movebase_client()

        rospy.spin()
        
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished - interrupted !!")

