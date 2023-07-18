#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry

# Node initialization
rospy.init_node('init_pose')
publisher_node = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size = 1)

# Construct message
initial_pose = PoseWithCovarianceStamped() #fetches position data at real position of robot
initial_pose.header.frame_id = "map" 

# fetching initial position and orientation from Gazebo
odometry_msg = rospy.wait_for_message('/odom', Odometry)
initial_pose.pose.pose.orientation.x = odometry_msg.pose.pose.orientation.x
initial_pose.pose.pose.orientation.y = odometry_msg.pose.pose.orientation.y
initial_pose.pose.pose.orientation.z = odometry_msg.pose.pose.orientation.z
initial_pose.pose.pose.orientation.w = odometry_msg.pose.pose.orientation.w
initial_pose.pose.pose.position.x = odometry_msg.pose.pose.position.x
initial_pose.pose.pose.position.y = odometry_msg.pose.pose.position.y


# Delay
rospy.sleep(1)

# Publish message
rospy.loginfo("setting initial pose")
publisher_node.publish(initial_pose)
rospy.loginfo("initial pose is set")



# first run init_pose, then dont move the 2d pose estimate
# then teleop to the goal position, record that position in the goal_pose 
# script, then telop back to the init pose position and run goa_pose script
# fix local cost map inflation radius before running goal_pose
