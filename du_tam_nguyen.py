#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
PI = 3.1415926535897

class TurtleBot:
     
    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(10)
    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def move(self, speed,distance):

        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
        vel_msg = Twist()
        #speed = 3
        vel_msg.linear.x = speed
        vel_msg.linear.y = 0
        vel_msg.linear.z=0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        

        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        if speed > 0:
            while(current_distance < distance):
                velocity_publisher.publish(vel_msg)
                t1=rospy.Time.now().to_sec()
                current_distance = speed*(t1-t0)
        elif speed < 0:
            while(current_distance > distance):
                velocity_publisher.publish(vel_msg)
                t1=rospy.Time.now().to_sec()
                current_distance = speed*(t1-t0)

            
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
    
    
    
    
    
    def moveDia(self,x):
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
        vel_msg = Twist()
        speed = 3
        distance = 2
        vel_msg.linear.x = x
        vel_msg.linear.y = -0.3
        vel_msg.linear.z= 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < distance):
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance = speed*(t1-t0)

        vel_msg.linear.y = 0
        velocity_publisher.publish(vel_msg)
    
    
    def moveDown(self, dire):
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
        vel_msg = Twist()
        speed = 3
        distance = 2
        vel_msg.linear.x = 0
        vel_msg.linear.y = dire
        vel_msg.linear.z= 0
        vel_msg.angular.x = 0.2
        vel_msg.angular.y = 0.3
        vel_msg.angular.z = 0
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < distance):
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance = speed*(t1-t0)

        vel_msg.linear.y = 0
        velocity_publisher.publish(vel_msg)

    def rotate(self, clockwise):
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
        vel_msg = Twist()
        speed = 2
        angle = 6
        angular_speed = speed*2*PI/360
        relative_angle = angle*2*PI/360


        vel_msg.linear.x=0
        vel_msg.linear.y=0
        vel_msg.linear.z=0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        
        if clockwise:
            vel_msg.angular.z = -abs(angular_speed)
        else: 
            vel_msg.angular.z = abs(angular_speed)

        t0 = rospy.Time.now().to_sec()
        current_angle = 0

        while(current_angle < relative_angle):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed*(t1 - t0)

        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        #rospy.spin()  

if __name__ == '__main__':
    try:
        #Testing our function
        x = TurtleBot()
        x.move(3,2)
        x.rotate(True)
        x.moveDia(0.3)
        x.moveDown(-3)
        x.rotate(False)
        x.moveDia(-0.3)
        x.move(-3, -1.5)
        x.moveDown(0.4)
        x.move(0.2, 0.3)
        x.moveDown(2.8)
        x.move(-0.2, -0.3)
        x.moveDown(0.5)
        x.move(0.2,0.4)
    except rospy.ROSInterruptException: pass

