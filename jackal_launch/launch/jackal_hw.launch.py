from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, GroupAction
from launch.substitutions import LaunchConfiguration, EnvironmentVariable
from launch.conditions import IfCondition
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare#, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # Declare arguments
    # ouster_arg = DeclareLaunchArgument('ouster', default_value='False')
    # realsense_arg = DeclareLaunchArgument('realsense', default_value='False')
    # cams_arg = DeclareLaunchArgument('cams', default_value='False')

    # Include jackal_description launch
    jackal_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('jackal_description'), '/launch/description.launch.py'
        ])
    )

    # # Robot state publisher node
    # robot_state_publisher_node = Node(
    #     package='robot_state_publisher',
    #     executable='robot_state_publisher'
    # )

    # Jackal node
    # jackal_node = Node(
    #     package='jackal_base',
    #     executable='jackal_node',
    #     name='jackal_node',
    #     parameters=[{
    #         'require.publishers': ['status', 'feedback', 'imu/data_raw', 'navsat/nmea_sentence'],
    #         'require.subscribers': ['cmd_drive', 'wifi_connected'],
    #         'wireless_interface': EnvironmentVariable('JACKAL_WIRELESS_INTERFACE', default_value='wlp2s0')
    #     }]
    # )

    # Rosserial message info node
    microros_node = Node(
            package='micro_ros_agent',
            executable='micro_ros_agent',
            arguments=['serial', '--dev', '/dev/jackal'],
            output='screen'
        )

    # NMEA topic driver node
    # nmea_topic_driver_node = Node(
    #     package='nmea_navsat_driver',
    #     executable='nmea_topic_driver',
    #     namespace='navsat'
    # )

    # Include jackal_control launch
    jackal_control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('jackal_control'), '/launch/control.launch.py'
        ])
    )
    
    # Include jackal_robot accessories
    # jackal_accesories = IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource(PathJoinSubstitution(
    #             [FindPackageShare('jackal_robot'), 'launch', 'accessories.launch.py']
    #         ))
    #     )

    # Include jackal_teleop launch
    jackal_teleop_base = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('jackal_teleop'), '/launch/teleop_base.launch.py'
        ])
    )
    
    jackal_teleop_joy = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('jackal_teleop'), '/launch/teleop_joy.launch.py'
        ])
    )
    
    # Include jackal_robot diagnostics
    # jackal_diagnostics = IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource(PathJoinSubstitution(
    #             [FindPackageShare('jackal_robot'), 'launch', 'diagnostics.launch.py']
    #         ))
    #     )

    # Include rosbridge_server launch
    # rosbridge_server = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         FindPackageShare('rosbridge_server'), '/launch/rosbridge_websocket.launch.py'
    #     ])
    # )

    # Ouster group
    # ouster_group = GroupAction([
    #     Node(
    #         package='tf2_ros',
    #         executable='static_transform_publisher',
    #         arguments=['0', '0', '0', '0', '0', '0', '1', 'base_link', 'ouster/os_sensor']
    #     ),
    #     IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource([
    #             FindPackageShare('ouster_decoder'), '/launch/decoder.launch.py'
    #         ]),
    #         launch_arguments={
    #             'imu_frame': 'ouster/os_imu',
    #             'lidar_frame': 'ouster/os_lidar',
    #             'sensor_frame': 'ouster/os_sensor'
    #         }.items()
    #     ),
    #     IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource([
    #             FindPackageShare('ouster_decoder'), '/launch/driver.launch.py'
    #         ]),
    #         launch_arguments={'tf_prefix': 'ouster'}.items()
    #     )
    # ], condition=IfCondition(LaunchConfiguration('ouster')))

    # RealSense group
    # realsense_group = GroupAction([
    #     Node(
    #         package='tf2_ros',
    #         executable='static_transform_publisher',
    #         arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'camera_link']
    #     ),
    #     IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource([
    #             FindPackageShare('realsense2_camera'), '/launch/rs_launch.py'
    #         ])
    #     ),
    #     Node(
    #         package='topic_tools',
    #         executable='throttle',
    #         arguments=['messages', '/camera/color/image_raw', '5']
    #     ),
    #     Node(
    #         package='topic_tools',
    #         executable='throttle',
    #         arguments=['messages', '/camera/color/image_raw/compressed', '5', '/camera/color/image_raw_throttle/compressed'],
    #         parameters=[{'lazy': True}]
    #     )
    # ], condition=IfCondition(LaunchConfiguration('realsense')))

    # Cameras group
    # cams_group = GroupAction([
    #     IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource([
    #             FindPackageShare('spinnaker_camera_driver'), '/launch/quad.launch.py'
    #         ])
    #     )
    # ], condition=IfCondition(LaunchConfiguration('cams')))

    return LaunchDescription([
        # ouster_arg,
        # realsense_arg,
        # cams_arg,
        jackal_description,
        # robot_state_publisher_node,
        # jackal_node,
        microros_node,
        # nmea_topic_driver_node,
        jackal_control,
        jackal_teleop_base,
        jackal_teleop_joy,
        # rosbridge_server,
        # ouster_group,
        # realsense_group,
        # cams_group
    ])