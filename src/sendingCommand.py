#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String 

class TextCommandNode:
    def __init__(self) -> None:
        rospy.init_node('text_command_node', anonymous=True)
        
        self.text_command_pub = rospy.Publisher('/text_command', String, queue_size=1)
        
    

    def run(self):
        rospy.loginfo("Ready")
        
        while not rospy.is_shutdown():
            
            user_input = input("Type forward, back, right, left or stop: ")
            
            text_command_obj = String()
            text_command_obj.data = user_input 
            
            
            self.text_command_pub.publish(text_command_obj)
            
            
if __name__ == '__main__':
    console = TextCommandNode()
    console.run()
    
    