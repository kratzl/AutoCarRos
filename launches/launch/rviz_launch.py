import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    # Define the path to the rviz file in the src directory
    workspace_dir = os.getenv("COLCON_PREFIX_PATH", "").split(":")[0]  # Base workspace
    rviz = os.path.join(
        os.path.dirname(workspace_dir),
        "src",
        "AutoCarROS2",
        "autocar_description",
        "rviz",
        "view.rviz",
    )

    use_sim_time = LaunchConfiguration("use_sim_time", default="True")

    return LaunchDescription(
        [
            Node(
                package="rviz2",
                executable="rviz2",
                name="rviz2",
                arguments=["-d", rviz],
                output={"both": "log"},
                parameters=[{"use_sim_time": use_sim_time}],
            ),
        ]
    )


def main():
    generate_launch_description()


if __name__ == "__main__":
    main()
