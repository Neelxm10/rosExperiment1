#!/usr/bin/env python
#Libraries used for navigation task
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

#All potential function Callbacks

def task_status(status, result): #Callback that shows the status of the program
    if status == 3:
        rospy.loginfo("target reached")
    if status == 2 or status == 8:
        rospy.loginfo("target cancelled")
    if status == 4:
        rospy.loginfo("target aborted")

def sensor_feedback(feedback): #Call back for localization
    rospy.loginfo("Current pose: "+str(feedback))

def task_active(extra): #callback for task being actively processed
    rospy.loginfo("Goal pose being processed")
    

rospy.init_node('target_position')

path_charter = actionlib.SimpleActionClient('move_base',MoveBaseAction)
path_charter.wait_for_server()

# Hard Coded navigation goal
result_goal = MoveBaseGoal()
result_goal.target_pose.header.frame_id = "map"
result_goal.target_pose.header.stamp = rospy.Time.now()
#Desired Position and Orientation
result_goal.target_pose.pose.position.x = -0.6166 
result_goal.target_pose.pose.position.y = 0.5498
result_goal.target_pose.pose.position.z = 0.0
result_goal.target_pose.pose.orientation.x = 0.0
result_goal.target_pose.pose.orientation.y = 0.0
result_goal.target_pose.pose.orientation.z = 0.8698
result_goal.target_pose.pose.orientation.w = 0.4933

#send goal function will send the desired result_goal position, parameters are obtained through ROS topic
path_charter.send_goal(result_goal, task_status, task_active, sensor_feedback) 
stop_flag = path_charter.wait_for_result()

if not stop_flag:
    rospy.logerr("Action server not available!")
else:
    rospy.loginfo ( path_charter.get_result())