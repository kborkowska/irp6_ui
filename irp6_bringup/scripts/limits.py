#!/usr/bin/env python

from irpos import *

#MAIN

if __name__ == '__main__':
	
	irpos = IRPOS("IRpOS", "Irp6p", 6, "irp6p_manager")
	#irpos.move_to_motor_position([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 10.0)
	irpos.move_to_joint_position([1.0, -1.5418065817051163,\
								  0.0, 1.5, 1.57, 0.0], 3.0)
	#irpos.move_to_joint_position([1.0, -1.5418065817051163,\
	#							  0.0, 1.5, 1.57, 0.0], 3.0)
	#irpos.move_to_joint_position([1.0, -1.5418065817051163,\
	#							  0.0, 1.5, 1.57, 1.0], 3.0)
	irpos.move_to_joint_position_reserch([-0.3, -1.5418065817051163,\
								  0.0, 1.5, 1.57, 1.0], [0.05, 1.0,\
								  1.0, 1.0, 1.0, 0.05],[0.1, 3.0,\
								  3.0, 3.0, 3.0, 0.1])