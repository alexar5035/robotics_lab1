#!/usr/bin/env python3

# import ROS for developing the node
import rospy

# import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist

# we are going to read turtlesim/Pose messages this time
from turtlesim.msg import Pose

# message we created
from robotics_lab1.msg import Turtlecontrol

# for radians to degrees conversions
import math

pos_msg = Turtlecontrol();

# recieves position information
def pose_callback(pos_callback):
	# convert x and y to cm
	pos_msg.x = data.x * 100
	pos_msg.y = data.y * 100
	
	
def user_control(Turtlecontrol_callback):
	# convert x and y to cm
	pos_msg.xd = data.x * 100
	pos_msg.kp = data.y * 100
	

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('pos_converter', anonymous = True)
	
	# add a subscriber to it to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	
	# add a subscriber to it to read the user control information
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol, Turtlecontrol_callback)
	
	# add a publisher
	pos_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	
	# 10Hz freq
	loop_rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		pos_pub.publish(pos_msg)
		loop_rate.sleep()
	# declare a variable of type Twist for sending control commands
	vel_cmd = Twist()
	
	# initialize the node
	rospy.init_node('turtlecontrol.py', anonymous = True)

	# set up loop that runs at a 10Hz frequency
	while not rospy.is_shutdown():
		# set the linear (forward/backward) velocity command to 0.5 m/s
		vel_cmd.linear.x = 0.5
		# set the angular (heading) velocity command to 0.5 radians/s
		vel_cmd.angular.z = 0.5
		# publish the command to the defined topic
		cmd_pub.publish(vel_cmd)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
	




