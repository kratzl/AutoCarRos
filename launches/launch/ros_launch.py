import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    SetEnvironmentVariable,
    IncludeLaunchDescription,
)
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    # Paths to the smaller launch files
    launchpkg = "autocar"

    robot_state_publisher_launch = os.path.join(
        get_package_share_directory(launchpkg),
        "launch",
        "robot_state_publisher_launch.py",
    )
    rviz_launch = os.path.join(
        get_package_share_directory(launchpkg), "launch", "rviz_launch.py"
    )
    teleop_launch = os.path.join(
        get_package_share_directory(launchpkg), "launch", "teleop_launch.py"
    )

    use_sim_time = LaunchConfiguration("use_sim_time", default="True")

    return LaunchDescription(
        [
            SetEnvironmentVariable(
                "RCUTILS_CONSOLE_OUTPUT_FORMAT", "[{severity}]: {message}"
            ),
            SetEnvironmentVariable("RCUTILS_COLORIZED_OUTPUT", "1"),
            DeclareLaunchArgument(
                "use_sim_time",
                default_value="true",
                description="Use simulation (Gazebo) clock if true",
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(robot_state_publisher_launch),
                launch_arguments={"use_sim_time": use_sim_time}.items(),
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(rviz_launch),
                launch_arguments={"use_sim_time": use_sim_time}.items(),
            ),
            IncludeLaunchDescription(PythonLaunchDescriptionSource(teleop_launch)),
        ]
    )
