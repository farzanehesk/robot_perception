cd ~/ws_moveit
colcon build --packages-select abb_kinect_description
source install/setup.bash

ros2 launch abb_kinect_description kinect_pointcloud_rviz.launch.py