#!/usr/bin/python3
import paho.mqtt.client as mqtt  #import the client1
import time
import json
from datetime import datetime, date, timedelta

from yaml import load_all
import goal_navigate as navi

topicEntries = "calendar/fhg.iao.vslab@gmail.com/entriesToday"
topicState = "calendar/fhg.iao.vslab@gmail.com/state"
calender_entries = dict()
roomState = " "
roomFree = "STATE_FREE"
roomFreeLongTerm = "STATE_FREE_LONGTERM"
messageReceivedFlag = False

class CalenderMQTT:

    def __init__(self, broker, port): 
        self.broker = broker    #"137.251.108.69"
        self.port  =  port          #80
        self.client = mqtt.Client("Roomba1")

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc==0:
            client.connected_flag=True #set flag
            print("connected OK")
        else:
            print("Bad connection Returned code=",rc)

    @staticmethod
    def on_message(client, userdata, message):
        if message.topic == topicEntries:
            global calender_entries, messageReceivedFlag
            messageReceivedFlag = True
            calender_entries = json.loads(str(message.payload.decode("utf-8")))
    
        elif message.topic == topicState:
            global roomState
            roomState = str(message.payload.decode("utf-8"))
            #print ("Received State is: ", (roomState))

    def connectionToBroker(self):
        mqtt.Client.connected_flag=False #create flag in class

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
                fourty_fiveMins = timedelta(minutes=45)
                calender_data = calender_entries['entries'][0]['entry'][0]['begin']
                meetingDateTime = datetime.strptime(calender_data, '%Y/%m/%d %H:%M:%S')
                meetingDate = datetime.strptime(calender_data, '%Y/%m/%d %H:%M:%S').date()
                cleaningTime = (meetingDateTime - fourty_fiveMins).time()

                if (roomState == roomFree or roomState == roomFreeLongTerm):
                    if (currentTime == cleaningTime):
                        try:
                            rospy.init_node("navigation_goal", anonymous = False)

                            with open (r'coordinates.yaml') as file_descriptor:

                                goal_coordinates = yaml.load(file_descriptor, Loader=load_all)

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

        print("Successfully executed try block")
    except:
        print ("An error occured!")