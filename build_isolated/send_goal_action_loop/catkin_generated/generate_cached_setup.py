# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/noetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/noetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/ros/robot/devel_isolated/rosserial_xbee;/home/ros/robot/devel_isolated/rosserial_windows;/home/ros/robot/devel_isolated/rosserial_vex_v5;/home/ros/robot/devel_isolated/rosserial_vex_cortex;/home/ros/robot/devel_isolated/rosserial_tivac;/home/ros/robot/devel_isolated/rosserial_test;/home/ros/robot/devel_isolated/rosserial_server;/home/ros/robot/devel_isolated/rosserial_python;/home/ros/robot/devel_isolated/rosserial_embeddedlinux;/home/ros/robot/devel_isolated/rosserial_client;/home/ros/robot/devel_isolated/rosserial_msgs;/home/ros/robot/devel_isolated/rosserial_mbed;/home/ros/robot/devel_isolated/rosserial_chibios;/home/ros/robot/devel_isolated/rosserial_arduino;/home/ros/robot/devel_isolated/rosserial;/home/ros/robot/devel_isolated/odom;/home/ros/robot/devel_isolated/hector_trajectory_server;/home/ros/robot/devel_isolated/hector_slam_launch;/home/ros/robot/devel_isolated/hector_slam;/home/ros/robot/devel_isolated/hector_map_server;/home/ros/robot/devel_isolated/hector_geotiff_plugins;/home/ros/robot/devel_isolated/hector_geotiff;/home/ros/robot/devel_isolated/hector_nav_msgs;/home/ros/robot/devel_isolated/hector_marker_drawing;/home/ros/robot/devel_isolated/hector_mapping;/home/ros/robot/devel_isolated/hector_compressed_map_transport;/home/ros/robot/devel_isolated/hector_map_tools;/home/ros/robot/devel_isolated/hector_imu_tools;/home/ros/robot/devel_isolated/hector_imu_attitude_to_tf;/home/ros/robot/devel_isolated/hector_geotiff_launch;/home/ros/robot/devel;/home/ros/catkin_ws/devel;/opt/ros/noetic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python3/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/ros/robot/devel_isolated/send_goal_action_loop/env.sh')

output_filename = '/home/ros/robot/build_isolated/send_goal_action_loop/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
