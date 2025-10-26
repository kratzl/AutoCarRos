import os
import subprocess

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    descpkg = "autocar_description"
    urdf = os.path.join(get_package_share_directory(descpkg), "urdf", "autocar.xacro")

    use_sim_time = LaunchConfiguration("use_sim_time", default="True")

    try:
        urdf_content = subprocess.check_output(["xacro", urdf]).decode("utf-8")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to process xacro file '{urdf}': {e}")

    return LaunchDescription(
        [
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="screen",
                parameters=[
                    {"use_sim_time": use_sim_time},
                    {"robot_description": urdf_content},
                ],
            ),
        ]
    )
