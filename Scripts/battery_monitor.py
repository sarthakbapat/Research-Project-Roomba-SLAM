#!/usr/bin/env python

import rospy
from std_msgs import Float32

import yaml
import time
from datetime import datetime, date, timedelta

import Calender.py as cal
import goal_navigate.py as navi

topicEntries = "calendar/fhg.iao.vslab@gmail.com/entriesToday"
topicState = "calendar/fhg.iao.vslab@gmail.com/state"
roomFree = "STATE_FREE"
roomFreeLongTerm = "STATE_FREE_LONGTERM"
batteryStatusRobot1 = " "
batteryStatusRobot2 = " "

def callback_ReceiveBatteryStatusRobot1(batteryCharge):
    if (batteryCharge <= 2.0):
        global batteryStatusRobot1
        batteryStatusRobot1 = "LOW"
    
    batteryStatusRobot1 = "OK"
        
def callback_ReceiveBatteryStatusRobot2(batteryCharge):
    if (batteryCharge <= 2.0):
        global batteryStatusRobot2
        batteryStatusRobot2 = "LOW"

    batteryStatusRobot2 = "OK"


if __name__ == '__main__':
    rospy.init_node('battery_monitor')

    sub1 = rospy.Subscriber("/robot1/battery/charge", Float32, callback_ReceiveBatteryStatusRobot1)
    sub2 = rospy.Subscriber("/robot2/battery/charge", Float32, callback_ReceiveBatteryStatusRobot2)

    rospy.loginfo ("Created both the subscribers....")

    try:
        broker = "137.251.108.69"
        port = 80

        obj = cal.CalenderMQTT(broker,port)
        ret = obj.connectionToBroker()

        ret.subscribe([(topicState,0), (topicEntries,0)])
        ret.loop_start()
        while(1):
            ret.on_message=cal.CalenderMQTT.on_message 
            print ("RoomState: ", cal.roomState)
            if messageReceivedFlag == True:
                currentTime = datetime.now().time()
                currentDate = date.today()
                fourty_fiveMins = timedelta(hours=1,minutes=30)
                calender_data = cal.calender_entries['entries'][0]['entry']

                for item in range(len(calender_data)):
                    meetingData = calender_data[item]['begin']
                    meetingDateTime = datetime.strptime(meetingData, '%Y/%m/%d %H:%M:%S')
                    meetingTime = datetime.strptime(meetingData, '%Y/%m/%d %H:%M:%S').time()
                    if currentTime < meetingTime:
                        break

                cleaningTime = (meetingDateTime - fourty_fiveMins).time()

                print ("cleaning time: ", cleaningTime)
                print ("current time: ", currentTime)
                print ("Meeting date time: ", meetingDateTime)

                if (cal.roomState == roomFree or cal.roomState == roomFreeLongTerm):
                    print ("Checked room state")
                    if (currentTime >= cleaningTime):
                        print ("---- Cleaning will start now -------")
                        try:
                            rospy.init_node("navigation_goal", anonymous = False)

                            with open (r'coordinates.yaml') as file_descriptor:

                                goal_coordinates = yaml.load(file_descriptor)

                            xGoal = goal_coordinates["xGoal"]
                            yGoal = goal_coordinates["yGoal"]
                            xOri = goal_coordinates["xOri"]
                            yOri = goal_coordinates["yOri"]
                            zOri = goal_coordinates["zOri"]
                            wOri = goal_coordinates["wOri"]

                            objNavigateToGoal = navi.NavigateToGoal(xGoal, yGoal, xOri, yOri, zOri, wOri)
                            objNavigateToGoal.movebase_client()

                            rospy.spin()
        
                        except rospy.ROSInterruptException:
                            rospy.loginfo("Navigation test finished - interrupted !!")

                messageReceivedFlag = False
            time.sleep(3)

        print("Should never reach here .....")
    except:
        print ("An error occured!")
