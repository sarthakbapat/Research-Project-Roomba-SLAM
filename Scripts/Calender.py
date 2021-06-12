#!/usr/bin/python3
import paho.mqtt.client as mqtt  
import time
import json
from datetime import datetime, date, timedelta

import rospy
import yaml
import goal_navigate as navi        #import the script that has navigation function.

topicEntries = "calendar/fhg.iao.vslab@gmail.com/entriesToday"
topicState = "calendar/fhg.iao.vslab@gmail.com/state"
calender_entries = dict()
roomState = " "
roomFree = "STATE_FREE"
roomFreeLongTerm = "STATE_FREE_LONGTERM"
messageReceivedFlag = False

class CalenderMQTT:
    """ 
    This is a class to handle the MQTT connection and messages to the Calendar server.

    """    
    
    def __init__(self, broker, port): 
        self.broker = broker  
        self.port  =  port          
        self.client = mqtt.Client("Roomba1")

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        """ The callback to check the MQTT connection status with the server.

        Args:
            client (object): The client object consisting of several flags.
            userdata (String): Private userdata as set in client().
            flags ([type]): response flags sent by the broker.
            rc (int): The result of the client connection.
        """        
        if rc==0:
            client.connected_flag = True 
            print("connected OK")
        else:
            print("Bad connection Returned code=",rc)

    @staticmethod
    def on_message(client, userdata, message):
        """ The callback to handle the MQTT messages.

        Args:
            client (object): The client object.
            userdata (String): Private userdata as set in client().
            message (MQTTMessage object): Instance of MQTTMessage containing topic, payload, qos, retain.
        """        
        if message.topic == topicEntries:
            global calender_entries, messageReceivedFlag
            messageReceivedFlag = True
            calender_entries = json.loads(str(message.payload.decode("utf-8")))
    
        elif message.topic == topicState:
            global roomState
            roomState = str(message.payload.decode("utf-8"))
            

    def connectionToBroker(self):
        """ A method that establishes connection to the MQTT server.

        Returns:
            MQTT client object: This is the MQTT client object after a successful connection is established.
        """        
        mqtt.Client.connected_flag = False #create flag in class

        self.client.username_pw_set(username= "pepper-talk", password="aC*TnO*T$M#83V6")
        self.client.on_connect = CalenderMQTT.on_connect  #bind call back function
        self.client.loop_start()

        print("Connecting to server ",self.broker)
        self.client.connect(self.broker, self.port, keepalive=60)      #connect to broker

        while not self.client.connected_flag: #wait in loop
            print("Waiting to establish connection.....")
            time.sleep(1)

        return self.client

if __name__ == '__main__':
    """ This is the main method that executes a forever while loop to handle the MQTT messages and 
    invoke the ROS navigation commands to the move_base server.
    """    

    try:
        broker = "137.251.108.69"
        port = 80

        obj = CalenderMQTT(broker,port)
        ret = obj.connectionToBroker()

        ret.subscribe([(topicState,0), (topicEntries,0)])
        ret.loop_start()
        while(1):
            ret.on_message=CalenderMQTT.on_message 
            print ("RoomState: ", roomState)
            if messageReceivedFlag == True:
                currentTime = datetime.now().time()
                currentDate = date.today()
                fourty_fiveMins = timedelta(hours=0,minutes=45)
                calender_data = calender_entries['entries'][0]['entry']

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

                if (roomState == roomFree or roomState == roomFreeLongTerm):
                    print ("Checked room state")
                    if (currentTime >= cleaningTime):
                        print ("---- Cleaning will start now -------")
                        try:
                            rospy.init_node("navigation_goal", anonymous = False)

                            with open (r'coordinates.yaml') as file_descriptor:

                                goal_coordinates = yaml.load(file_descriptor)

                            #Parse the yaml file to get the goal locations.
                            xGoal = goal_coordinates["xGoal"]
                            yGoal = goal_coordinates["yGoal"]
                            xOri = goal_coordinates["xOri"]
                            yOri = goal_coordinates["yOri"]
                            zOri = goal_coordinates["zOri"]
                            wOri = goal_coordinates["wOri"]

                            #Instantiate the NavigateToGoal class and call the method movebase_client.
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