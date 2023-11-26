#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String 
from geometry_msgs.msg import Twist 



class Commander:
    def __init__(self) -> None:
        
        rospy.init_node("Commander" , anonymous=True)
        
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        
        rospy.Subscriber('/text_command', String, self.do_some_work)
    
    def do_some_work(self, data):
        
        command = data.data 
        command = command.lower()
        
        rospy.loginfo(f"Paisi:- {command}")
    
    
        twist_cmd = Twist()
        
    
        if command == "forward":
            twist_cmd.linear.x = 0.5
        elif command == "backward":
            twist_cmd.linear.x = -0.5
        elif command == "right":
            twist_cmd.angular.z = 0.5 
        elif command == "left":
            twist_cmd.angular.z = -0.5 
        
        
        self.cmd_vel_pub.publish(twist_cmd)
            
         

    def run(self):
        rospy.spin()
        

if __name__ =='__main__':
    a = Commander()
    a.run()
    