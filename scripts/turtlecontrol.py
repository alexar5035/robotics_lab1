#!/usr/bin/env python3

# import ROS for developing the node
import rospy

# import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist

# we are going to read turtlesim/Pose messages this time
from turtlesim.msg import Pose

# message we created
from robotics_lab1.msg import Turtlecontrol


pos_msg = Pose()
ctrl_msg = Turtlecontrol();

# recieves position information
def pose_callback(data):
	global pos_msg
	# turtle position variable
	pos_msg.x = data.x 

		
def user_control_callback(data):
	global ctrl_msg
	ctrl_msg.xd = data.xd
	ctrl_msg.kp = data.kp
	

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('turtlecontrol', anonymous = True)
	
	# add a subscriber to it to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	
	# add a subscriber to it to read the user control information
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol, user_control_callback)
	
	# add a publisher
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	
	# 10Hz freq
	loop_rate = rospy.Rate(10)
	
	# declare a variable of type Twist for sending control commands
	vel_cmd = Twist()
	
	while not rospy.is_shutdown():
		# proportional control equation
		vel_cmd.linear.x = ctrl_msg.kp * (ctrl.msg.xd - pos_msg.x)
	
		# publish the command to the defined topic
		cmd_pub.publish(vel_cmd)
	
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
	




