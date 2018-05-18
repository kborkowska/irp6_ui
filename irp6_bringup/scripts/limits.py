#!/usr/bin/env python

from irpos import *

#MAIN

#lower_limits: [-470.0, -110.0, -80.0, -70.0, -80.0, -1000.0]
#upper_limits: [450.0, 100.0, 100.0, 380.0, 490.0, 3000.0]


if __name__ == '__main__':
	
	irpos = IRPOS("IRpOS", "Irp6p", 6, "irp6p_manager")
	irpos.move_to_motor_position([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 5.0)
	'''irpos.move_to_joint_position([1.3, -1.5,\
								  0.1575, 1.5, 1.57, 0.0], 7.0)'''
	#irpos.move_to_joint_position([1.0, -1.5418065817051163,\
	#							  0.6, 1.5, 1.57, 0.0], 3.0)
	#irpos.move_to_joint_position([-0.3, -1.5,\
	#							  0.0, 1.5, 1.57, 1.0], 3.0)
	#irpos.move_to_joint_position([1.0, -1.5418065817051163,\
	#							  0.0, 1.5, 1.57, 0.0], 3.0)
	'''irpos.move_to_joint_position([1.0, -1.5418065817051163,\
								  0.0, 1.5, 1.57, 0.0], 3.0)'''
	print irpos.get_motor_position()
	points = []
	points.append(JointTrajectoryPoint([300.0, 75.0, -80.0,\
									   200.0, 150.0, -500.0],
									   [0.0, 0.0, 0.0,\
									   0.0, 0.0, 0.0],
									   [0.0, 0.0, 0.0,\
									   0.0, 0.0, 0.0],[], rospy.Duration(3.0)))
	points.append(JointTrajectoryPoint([0.0, 0.0, 0.0,\
									   0.0, 0.0, 500.0],
									   [0.0, 0.0, 0.0,\
									   0.0, 0.0, 0.0],
									   [0.0, 0.0, 0.0,\
									   0.0, 0.0, 0.0],[], rospy.Duration(3.0)))
	irpos.move_along_motor_trajectory_research(\
								     points,\
								  [30, 35, 35,\
								   35, 35, 35],\
								  [20, 20, 20,\
								   20, 20, 20])
	'''irpos.move_to_joint_position_research(\
								  [0.5, -1.5, 0.1575,\
								   1.5, 1.57, 0.0],\
								  [0.35, 0.35, 0.05,\
								   0.35, 0.35, 0.35],\
								  [0.2, 0.2, 0.05,\
								   0.2, 0.2, 0.2])'''
	'''irpos.move_to_motor_position_research(\
								  [0.0, 0.0, 0.0,\
								   0.0, 0.0, -1000.0],\
								  [30, 35, 35,\
								   35, 35, 35],\
								  [20, 20, 20,\
								   20, 20, 20])
	irpos.move_to_motor_position_research(\
								  [0.0, 0.0, 0.0,\
								   0.0, 0.0, 3000.0],\
								  [30, 35, 35,\
								   35, 35, 35],\
								  [20, 20, 20,\
								   20, 20, 20])'''
	'''irpos.move_to_joint_position_trapezoid([0.7, -1.5418065817051163,\
								  0.0, 1.5, 1.57, 0.0])
	irpos.move_to_joint_position_trapezoid([0.7, -1.7,\
								  0.2, 1.5, 1.57, 0.0])'''
	#print irpos.get_motor_position()
	print irpos.get_motor_position()