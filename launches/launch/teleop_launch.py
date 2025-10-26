import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    navpkg = "autocar_nav"

    teleop = os.path.join(
        get_package_share_directory(navpkg), "config", "teleop_twist_joy.yaml"
    )
    twist_mux = os.path.join(
        get_package_share_directory(navpkg), "config", "twist_mux.yaml"
    )

    return LaunchDescription(
        [
            # Joystick input
            Node(
                package="joy",
                executable="joy_node",
                parameters=[teleop],
            ),
            # Teleop Twist from joystick
            Node(
                package="teleop_twist_joy",
                executable="teleop_node",
                name="teleop_node",
                parameters=[teleop],
                remappings=[("/cmd_vel", "/cmd_vel_joy")],
            ),
            # Twist Mux to manage velocity commands
            Node(
                package="twist_mux",
                executable="twist_mux",
                name="twist_mux",
                parameters=[twist_mux],
                remappings=[
                    ("cmd_vel_out", "autocar/cmd_vel"),
                ],
            ),
        ]
    )
