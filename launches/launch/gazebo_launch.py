import os
import subprocess

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument


def generate_launch_description():

    gzpkg = "autocar_gazebo"

    pkg_gazebo = get_package_share_directory("gazebo_ros")

    world = os.path.join(
        get_package_share_directory(gzpkg), "worlds", "autocar_city.world"
    )

    subprocess.run(["killall", "gzserver"])
    subprocess.run(["killall", "gzclient"])

    gzserver = os.path.join(pkg_gazebo, "launch", "gzserver.launch.py")
    gzclient = os.path.join(pkg_gazebo, "launch", "gzclient.launch.py")

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "use_sim_time",
                default_value="false",
                description="Use simulation (Gazebo) clock if true",
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(gzserver),
                launch_arguments={"world": world}.items(),
            ),
            IncludeLaunchDescription(PythonLaunchDescriptionSource(gzclient)),
        ]
    )


def main():

    generate_launch_description()


if __name__ == "__main__":
    main()
