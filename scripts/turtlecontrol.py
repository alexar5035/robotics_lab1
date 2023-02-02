#!/usr/bin/env python3

# import ROS for developing the node
import rospy

# import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist

# we are going to read turtlesim/Pose messages this time
from turtlesim.msg import Pose

# message we created
from robotics_lab1.msg import Turtlecontrol

pos_msg = Turtlecontrol();
# declare variables for the proportional controller equation
kp = 0
xd = 0
xt = 0
# recieves position information
def pose_callback(data):
	global pos_msg
	global xt
	# convert x 
	pos_msg.xt = data.x #TURTLECONTROL OBJECT HAS NO ATTRIBUTE "X"
		
def user_control_callback(data):
	global pos_msg
	global xd
	global kp
	# convert xd and kp
	pos_msg.xd = data.x 
	pos_msg.kp = data.y 
	

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('turtlecontrol.py', anonymous = True)
	
	# add a subscriber to it to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	
	# add a subscriber to it to read the user control information
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol, user_control_callback)
	
	# add a publisher
	pos_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	
	# 10Hz freq
	loop_rate = rospy.Rate(10)
	
	# declare a variable of type Twist for sending control commands
	vel_cmd = Twist()
	
	while not rospy.is_shutdown():
		# pos_pub.publish(pos_msg)
		# set the linear (forward/backward) velocity command to 0.5 m/s
		vel_cmd.linear.x = kp * (xd - xt) # proportional control equation
		# set the angular (heading) velocity command to 0.5 radians/s
		vel_cmd.angular.z = kp * (xd - xt) # proportional control equation
		# publish the command to the defined topic
		pos_pub.publish(vel_cmd)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
	




