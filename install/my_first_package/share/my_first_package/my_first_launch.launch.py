from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command, LaunchConfiguration

# This file is used to launch the following nodes:
# - simple_publisher
# - simple_subscriber

def generate_launch_description():
    my_first_package_dir = get_package_share_directory("my_first_package") # Get the package directory
    
    publisher_node = Node(
        package='my_first_package',
        executable='simple_publisher',        
        )
    
    subscriber_node = Node(
        package='my_first_package',
        executable='simple_subscriber',
        )
    
    return LaunchDescription([
        publisher_node, 
        subscriber_node,
    ])