import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command

def generate_launch_description():

    # Kinect driver launch
    kinect_driver = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('azure_kinect_ros_driver'),
                'launch', 'driver.launch.py'
            )
        ])
    )

    # RViz with pointcloud config
    rviz_config = os.path.join(
        get_package_share_directory('abb_kinect_description'),
        'launch', 'kinect_pointcloud.rviz'
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config] if os.path.exists(rviz_config) else [],
    )

    return LaunchDescription([
        kinect_driver,
        rviz,
    ])
