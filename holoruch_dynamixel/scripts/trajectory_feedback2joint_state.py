#!/usr/bin/env python

from __future__ import print_function

import rospy
import argparse

from sensor_msgs.msg import JointState
from control_msgs.msg import FollowJointTrajectoryFeedback

trajectory_feedback_sub = None
joint_state_pub = None

def on_trajectory_feedback(feedback_msg):
  joint_msg = JointState()
  joint_msg.header = feedback_msg.header
  joint_msg.name = feedback_msg.joint_names
  joint_msg.position = feedback_msg.actual.positions
  joint_msg.velocity = feedback_msg.actual.velocities
  joint_msg.effort = feedback_msg.actual.effort

  joint_state_pub.publish(joint_msg)


def main():
  #parser = argparse.ArgumentParser()
  #args = parser.parse_args(rospy.myargv()[1:])

  rospy.init_node('trajectory_feedback2joint_state')

  global joint_state_pub
  joint_state_pub = rospy.Publisher('joint_states', JointState, queue_size = 1)
  global trajectory_feedback_sub
  trajectory_feedback_sub = rospy.Subscriber('state', FollowJointTrajectoryFeedback, on_trajectory_feedback, queue_size = 1)

  rospy.loginfo('Spinning')
  rospy.spin()


if __name__ == '__main__':
  main()
