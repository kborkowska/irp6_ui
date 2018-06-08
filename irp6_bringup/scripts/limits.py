#!/usr/bin/env python

from irpos.IRPOS_T import *

#MAIN


#motors
#lower_limits: [-470.0, -110.0, -80.0, -70.0, -80.0, -1000.0]
#upper_limits: [450.0, 100.0, 100.0, 380.0, 490.0, 3000.0]

#joints
#lower_limits: [-0.45, -2.2689280276, -0.6108652382, -1.5707963268, -10.0, -2.88]
#upper_limits: [2.9670597284, -0.872664626, 0.6981317008, 1.6057029118, 10.0, 2.93]

if __name__ == '__main__':
	
	irpos = IRPOS_T("IRpOS", "Irp6p", 6, "irp6p_manager")
	#irpos.move_to_motor_position([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 5.0)
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
	#print irpos.get_joint_position()
	irpos.move_to_motor_position_trapezoid_velocity(\
								  [400.0, 0.0, 0.0,\
								   0.0, 0.0, 0.0],\
								  [25, 35, 35,\
								   35, 35, 35],\
								  [10, 20, 20,\
								   20, 20, 20],\
								    True, False)
	'''points = []
	points.append(JointTrajectoryPoint([-0.10, -1.0, 0.019,\
									   -1.55, -8.0, -2.74],
									   [0.0, 0.0, 0.0,\
									   0.0, 0.0, 0.0],
									   [0.0, 0.0, 0.0,\
									   0.0, 0.0, 0.0],[], rospy.Duration(3.0)))
	points.append(JointTrajectoryPoint([2.0, -1.1, 0.0,\
									   1.0, 4.0, 2.0],
									   [0.0, 0.0, 0.0,\
									   0.0, 0.0, 0.0],
									   [0.0, 0.0, 0.0,\
									   0.0, 0.0, 0.0],[], rospy.Duration(3.0)))
	points.append(JointTrajectoryPoint([-0.1, -1.7, 0.6,\
									   1.0, 4.0, 2.0],
									   [0.0, 0.0, 0.0,\
									   0.0, 0.0, 0.0],
									   [0.0, 0.0, 0.0,\
									   0.0, 0.0, 0.0],[], rospy.Duration(3.0)))
	points.append(JointTrajectoryPoint([-0.10063291139240507, -1.5419428654532268, 0.019737556833721442,\
									   1.1335183568246088, 3.658072916666667, -2.7381185214159984],
									   [0.0, 0.0, 0.0,\
									   0.0, 0.0, 0.0],
									   [0.0, 0.0, 0.0,\
									   0.0, 0.0, 0.0],[], rospy.Duration(3.0)))
	irpos.move_along_joint_trajectory_trapezoid_velocity(\
								     points,\
								     [0.30, 0.30, 0.30,\
									  0.30, 0.30, 0.30],\
									 [0.20, 0.20, 0.20,\
									  0.20, 0.20, 0.20],
									 False, True)'''

	'''irpos.move_to_joint_position_trapezoid_duration([1.40, -1.0, 0.02,\
								   -1.55, 1.0, -2.0],\
								   True, True)'''

	'''							[0.30, 0.30, 0.30,\
								   0.30, 0.30, 0.30],\
								  [0.20, 0.20, 0.20,\
								   0.20, 0.20, 0.20],'''

	'''[0.3, 0.3, 0.3,\
								   0.3, 0.3, 0.3],\
								  [0.2, 0.2, 0.2,\
								   0.2, 0.2, 0.2],'''

	'''irpos.move_along_motor_trajectory_trapezoid_duration(\
								     points,\
									 False, False)'''
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
	print irpos.get_motor_position()
	#print irpos.get_motor_position()